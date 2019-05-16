#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import traceback
import urlparse
import requests
from logger import logger
from config import HEADER, CRAWLER_CONFIG, API_CONFIG
from proxysites import get_proxy_sites
import datetime

class Crawler(object):
    def run(self):
        proxy_url = get_proxy_sites()[0]['url']
        return self.crawl(proxy_url)

    def crawl(self, site_url):
        proxies = []
        try:
            r = requests.get(site_url, headers=HEADER, timeout=CRAWLER_CONFIG['TIMEOUT'])
            now = datetime.datetime.now()
            day_time = now.strftime('%Y-%m-%d_%H_%M_%S')
            day = now.strftime('%Y-%m-%d')
            # param_list = list()
            if r.status_code == 200:
                logger.info(' %s get %s proxies' % (urlparse.urlparse(site_url).netloc, len(r.json())))
                for i in r.json():
                    ip_port = str(i.get("Ip")) + ':' + str(i.get("Port"))
                    proxies.append(ip_port)
                    time_str = now.strftime('%Y-%m-%d %H:%M:%S')

                    with open('logs/proxyIp_%s.log' % day,'a') as f:
                        f.write(ip_port + '\t' + time_str + '\n')

                    with open('logs/proxyIp_%s.log' % day_time,'a') as f:
                        f.write(ip_port + '\t' + time_str + '\n')
                    # param_list.append((ip_port, time_str))

                # p = Process(target=insert_mysql, args=("yundl_history_ip", param_list))
                # p.start()
                # insert_mysql(db_name="yundl_history_ip", param_list=param_list)
                checked_proxies = self.distinct_proxies_list(proxies)
                logger.info('distinct proxies %s' % len(checked_proxies))
                return checked_proxies
            else:
                logger.info('crawl error code: %s, content: %s' % (r.status_code, r.content))
                return None
        except Exception as e:
            logger.error("connection error msg: %s", e)
            return None

    def distinct_proxies_list(self, proxies):
        proxies_dict = {}
        for i in proxies:
            proxies_dict[i] = i
        return proxies_dict.keys()

if __name__ == '__main__':
     print Crawler().run()
