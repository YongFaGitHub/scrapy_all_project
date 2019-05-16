#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import platform
import multiprocessing
from daemon import daemonize
from threadpool import ThreadPool
from threadpool import makeRequests
from threading import Thread
import time
from logger import logger
from proxy_crawler import Crawler
from validator import Validator
from DumpClient import redis_client


class ProxyPool:
    def __init__(self, redis_key_http, redis_key_https, redis_distinct_set_http, redis_distinct_set_https):
        self.Crawler = Crawler()
        self.redis_key_http = redis_key_http
        self.redis_key_https = redis_key_https
        self.redis_distinct_set_http = redis_distinct_set_http
        self.redis_distinct_set_https = redis_distinct_set_https
        self.Validator = Validator(
            redis_key_http=self.redis_key_http,
            redis_key_https=self.redis_key_https,
            redis_distinct_set_http=self.redis_distinct_set_http,
            redis_distinct_set_https=self.redis_distinct_set_https
        )

    def _crawl(self):
        logger.info('Crawl proxy begin')
        start = time.time()
        proxies = self.Crawler.run()
        logger.info("Crawl proxy consume time is {0}".format(time.time()-start))
        return proxies

    def _validator(self,proxy):
        available_proxy_http, available_proxy_https = self.Validator.run(proxy)
        if available_proxy_http:
            self._validator_distinct(available_proxy=available_proxy_http, proxy=proxy)
        if available_proxy_https:
            self._validator_distinct(available_proxy=available_proxy_https, proxy=proxy)

    def _validator_distinct(self, available_proxy, proxy):
        if available_proxy["check_type"] == "http":
            redis_key = self.redis_key_http
        else:
            redis_key = self.redis_key_https
        change_available_proxy = {
            "ip": available_proxy["ip"],
            "port": available_proxy["port"],
            "type": available_proxy["type"],
            "timestamp": available_proxy["timestamp"],
        }
        checked_code = self.put_redis_set(proxy=proxy, check_type=available_proxy["check_type"])
        import pdb;pdb.set_trace()
        if checked_code:
            redis_client.zadd(redis_key, available_proxy["speed"], change_available_proxy)
        else:
            ip_list = redis_client.zrange(redis_key, 0, -1)
            for item in ip_list:
                ip_dict = eval(item)
                ip_port = ip_dict.get("ip") + ':' + ip_dict.get("port")
                if proxy == ip_port:
                    code = redis_client.zrem(redis_key, item)
                    if code == 1:
                        redis_client.zadd(redis_key, available_proxy["speed"], change_available_proxy)

    # def _put_redis(self):
    #     proxies = self._crawl()
    #     if proxies:
    #         logger.info("begin validate proxy")
    #         start_time = time.time()
    #         pool = ThreadPool(len(proxies))
    #         requests = makeRequests(self._validator, proxies)
    #         [pool.putRequest(req) for req in requests]
    #         pool.wait()
    #         logger.info("validate proxy consume time is {0}".format(time.time()-start_time))
    #     else:
    #         logger.info("proxies is None!")

    def _clear_before_five_minutes_redis(self):
        logger.info("begin delete")
        now_time=time.time()

        ip_list_http = redis_client.zrange(self.redis_key_http, 0, -1)
        ip_list_https = redis_client.zrange(self.redis_key_https, 0, -1)

        logger.info('delete before http ip count is %d' % len(ip_list_http))
        logger.info('delete before https ip count is %d' % len(ip_list_https))

        delete_count_http = self.re_redis(now_time=now_time, ip_list=ip_list_http,
                                          redis_key=self.redis_key_http, type="http")
        delete_count_https = self.re_redis(now_time=now_time, ip_list=ip_list_https,
                                           redis_key=self.redis_key_https, type="https")

        logger.info('delete http ip count is %d' % delete_count_http)
        logger.info('delete https ip count is %d' % delete_count_https)
        logger.info("delete consume time is {0}".format(time.time() - now_time))

    def re_redis(self, now_time, ip_list, redis_key, type):
        delete_count = 0
        ip_port_dict = {}
        delete_ip_list = []
        if type == "http":
            distinct_set = self.redis_distinct_set_http
        else:
            distinct_set = self.redis_distinct_set_https

        for ip in ip_list:
            ip_dict = eval(ip)
            timestamp = ip_dict.get("timestamp")
            ip_port = ip_dict.get("ip") + ':' + ip_dict.get("port")
            if timestamp < (now_time - 5 * 60):
                redis_client.zrem(redis_key, ip)
                redis_client.srem(distinct_set, ip_port)
                delete_ip_list.append(ip_port)
                delete_count += 1
            else:
                ip_port_dict[ip] = ip_port

        for del_ip in ip_port_dict:
            if ip_port_dict[del_ip] in delete_ip_list:
                redis_client.zrem(redis_key, del_ip)
                delete_count += 1
        return delete_count

    def put_redis_set(self, proxy, check_type):
        if check_type == "http":
            return redis_client.sadd(self.redis_distinct_set_http, proxy)
        elif check_type == "https":
            return redis_client.sadd(self.redis_distinct_set_https, proxy)

    def run(self):
        """
        开1000个线程，一个用做IP的爬取，验证，放入redis，
        并且线程的十分钟重启
        用于维护代理池里IP的五分钟鲜活性
        """
        while True:
            logger.info('begin getting and available ip')
            s = time.time()
            try:
                proxies = self._crawl()
                thread_list = list()
                if proxies:
                    logger.info("begin validate proxy")
                    start_time = time.time()
                    for proxy in proxies:
                        t = Thread(target=self._validator, args=(proxy,))
                        thread_list.append(t)
                    for t in thread_list:
                        t.start()
                    for t in thread_list:
                        t.join(120)
                    logger.info("validate proxy consume time is {0}".format(time.time() - start_time))
                else:
                    logger.info("proxies is None!")
                # p=multiprocessing.Process(target=self._put_redis)
                # p.start()
                # p.join(240)
                self._clear_before_five_minutes_redis()
            except Exception as e:
                logger.error("Run error: %s", e)
            logger.info("A batch consume time is {0}".format(time.time()-s))


if __name__ == '__main__':
    pass
