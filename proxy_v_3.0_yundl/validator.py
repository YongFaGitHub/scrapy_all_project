#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
gevent协程验证IP是否有效
验证网站  7-13号开始没有HEADER无法登陆。
"""
from DumpClient import redis_client
import urllib2
from logger import logger
import time
import pyip
import requests
from config import VALIDATE_CONFIG, HEADER


class Validator:
    def __init__(self, redis_key_http, redis_key_https, redis_distinct_set_http, redis_distinct_set_https):
        #  VALIDATE_CONFIG['HTTP_TARGET']: 'http://fetch.bestzsj.com/v1/validate_ip_https',
        #  VALIDATE_CONFIG['HTTPS_TARGET']: 'https://fetch.bestzsj.com/v1/validate_ip_https',
        # VALIDATE_CONFIG['TIMEOUT'] :20
        self.http_target = VALIDATE_CONFIG['HTTP_TARGET']
        self.https_target = VALIDATE_CONFIG['HTTPS_TARGET']
        self.timeout = VALIDATE_CONFIG['TIMEOUT']
        self.ip = self._get_self_ip()
        # self.IPL = pyip.IPLocator('QQWry.Dat')

    def run(self, proxy):  # proxy: 'ip:port'
        if not self.ip:
            logger.error('Validating fail, self ip is empty')
            return None
        available_proxy_http=self.validate(proxy, check_type="http")
        available_proxy_https=self.validate(proxy, check_type="https")
        return available_proxy_http, available_proxy_https

    def validate(self, proxy, check_type):
        try:
            start = time.time()
            if check_type == "http":
                target_url = self.http_target
                proxies = {'http': 'http://%s' % proxy}
            else:
                target_url = self.https_target
                proxies = {'https': 'http://%s' % proxy}

            # response = requests.get(target_url, headers=HEADER,
            #                         proxies=proxies,
            #                         timeout=self.timeout)

            proxy_handler = urllib2.ProxyHandler(proxies)
            opener = urllib2.build_opener(proxy_handler)
            urllib2.install_opener(opener)
            req = urllib2.Request(target_url, headers=HEADER)
            response = urllib2.urlopen(req, timeout=self.timeout)

            timestamp = time.time()
            speed = timestamp - start

            # if response.ok:
            if response.code == 200:
                # data = eval(response.content)
                data = eval(response.read())
                REMOTE_ADDR = data['REMOTE_ADDR']
                HTTP_VIA = data['HTTP_VIA']
                HTTP_X_FORWARDED_FOR = data['HTTP_X_FORWARDED_FOR']

                if REMOTE_ADDR and REMOTE_ADDR != self.ip:
                    if  HTTP_X_FORWARDED_FOR =='':
                        if  HTTP_VIA == '':
                            type = 3  # 高匿名
                    elif HTTP_X_FORWARDED_FOR != self.ip:
                        type = 2  # 普通匿名或者欺骗性匿名
                    else:
                        type = 1  # 透明

                    logger.info('Validating %s, success, type:%s, time:%ss check_type: %s',
                                proxy, type, speed, check_type + "_success")

                    value_dict = {
                            'check_type': '',
                            'ip': '',
                            'port': '',
                            'type': type,
                            'speed': speed,
                            'timestamp': timestamp,
                    }

                    host_port = proxy.split(':')
                    value_dict["check_type"] = check_type
                    value_dict["ip"] = host_port[0]
                    value_dict["port"] = host_port[1]
                    return value_dict

        except Exception as e:
            logger.debug('Validating %s, fail: %s check_type: %s', proxy, e, check_type + "_fail")
            pass
        return None

    def _get_self_ip(self):
        # 获取自身外网ip
        try:
            r = requests.get(VALIDATE_CONFIG['HTTP_TARGET'], headers=HEADER, timeout=self.timeout)
            if r.ok:
                data = eval(r.content)
                ip = data['REMOTE_ADDR']
                logger.info('Get self ip success: %s' % ip)
                return ip
        except Exception, e:
            logger.warn('Get self ip fail, %s ' % e)
            return ''


if __name__ =='__main__':
    # validate=Validator()
    # print validate.run(["186.93.77.203:8080"])
    pass
