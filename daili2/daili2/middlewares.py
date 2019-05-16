# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy import signals
import pymysql


class Daili2SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Daili2DownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

import csv
class ProxyMiddleware2(object):

    def process_request(self, request, spider):
        # conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="jing1995", charset='utf8',
        #                        database="daili", )
        # cs1 = conn.cursor()
        #
        # connt = cs1.execute("select ip from daili_pool")
        # res = cs1.fetchall()
        # list = []
        # for one in res:
        #     list.append("http://" + one[0])
        # ip = random.choice(list)
        ip_list = ["117.191.11.110:8080",
                   "118.89.138.129:59460",
                   "116.209.53.83:9999",
                   "116.209.59.107:9999",
                   "117.191.11.111:80",
                   "111.11.100.13:8060",
                   "117.191.11.74:8080", "116.209.57.238:9999",
                   "117.191.11.79:8080", "139.199.108.78:808",
                   "103.205.26.57:57010",
                   "125.123.142.234:9999",
                   "116.209.53.96:9999",
                   "114.119.116.92:61066",
                   "117.191.11.102:80",
                   "222.91.126.166:8060",
                   "139.129.207.72:808",
                   "116.209.52.119:9999",
                   "117.191.11.113:80",
                   "116.209.58.143:9999",
                   "112.95.26.135:8088",
                   "125.123.140.201:9999",
                   "125.123.143.81:9999",
                   "111.177.186.38:9999",
                   "211.87.234.39:3128",
                   "115.239.24.247:9999",
                   "39.137.168.229:8080",
                   "125.123.137.180:9000",
                   "125.123.140.157:9999",
                   "111.177.183.45:9999",
                   "116.209.53.237:9999",
                   "58.144.150.35:8888",
                   "125.123.123.217:9000",
                   "116.209.54.110:9999",
                   "125.123.141.249:9999",
                   "218.77.183.125:8080",
                   "180.104.107.46:45700",
                   "123.132.232.254:61017",
                   "222.222.236.207:8060",
                   "119.29.224.144:8118",
                   "222.222.153.171:808",
                   "221.193.222.7:8060",
                   "125.123.20.45:9000",
                   "221.6.32.206:41816",
                   "218.89.14.142:8060",
                   "117.40.114.163:8118",
                   "219.159.38.197:56210",
                   "14.20.235.131:9797",
                   "116.209.53.186:9999",
                   "118.24.3.29:8118",
                   "221.181.8.168:3128",
                   "47.94.221.41:8118",
                   "125.123.126.72:9000",
                   "180.140.191.233:48326",
                   "116.209.54.4:9999",
                   "117.114.149.10:45801",
                   "182.111.64.8:53364",
                   "113.122.169.202:9999",
                   "221.6.32.214:41816",
                   "221.11.105.70:56120",
                   "111.75.193.22:48449",
                   "124.205.155.158:9090",
                   "125.123.125.203:9000",
                   "222.222.250.143:8060",
                   "183.6.130.6:8118",
                   "125.123.136.246:9999",
                   "1.197.204.68:9999",
                   "111.177.173.20:9999",
                   "112.95.16.41:8088",
                   "125.123.142.22:9999",
                   "113.122.168.94:9999",
                   "118.182.33.6:42801",
                   "124.205.155.149:9090",
                   "115.239.25.134:9000",
                   "125.123.137.164:9999",
                   "123.55.98.85:9999",
                   "180.118.73.78:9999",
                   "115.151.1.22:9999",
                   "60.13.42.25:9999",
                   "118.24.100.115:8118",
                   "125.123.136.102:9999",
                   "125.123.125.188:9000",
                   "111.177.185.209:9999",
                   "125.123.123.192:9000",
                   "125.123.121.73:9000",
                   "14.20.235.133:808",
                   "125.123.138.55:9999",
                   "112.95.27.85:8088",
                   "116.208.55.116:9999",
                   "120.79.203.1:3128",
                   "106.12.214.231:80",
                   "103.228.245.91:8080",
                   "125.123.127.151:9000",
                   "115.154.38.147:1080",
                   "118.187.58.34:53281",
                   "121.61.1.124:9999",
                   "119.57.108.73:53281",
                   "119.176.66.90:9999",
                   "118.25.35.202:9999",
                   "114.55.236.62:3128",
                   "139.199.12.150:8888",
                   "123.207.247.86:9999",
                   "119.1.97.193:36751",
                   "59.62.166.168:9999",
                   "117.191.11.110:8080",
                   "124.206.242.127:3128",
                   "125.123.23.200:9000",
                   "117.191.11.71:80",
                   "116.209.55.172:9999",
                   "111.230.113.238:9999",
                   "193.112.128.212:8118",
                   "117.191.11.72:8080",
                   "119.1.97.192:36751",
                   "106.39.45.124:8080",
                   "116.209.52.80:9999",
                   "116.209.53.219:9999",
                   "123.133.41.104:53281",
                   "1.198.73.175:9999",
                   "118.163.120.181:58837",
                   "218.204.81.90:8123",
                   "115.239.25.250:9999",
                   "125.73.220.18:49128",
                   "116.209.59.49:9999",
                   "112.95.24.161:8088",
                   "125.123.141.188:9999",
                   "112.95.27.51:8088",
                   "116.209.56.176:9999",
                   "180.117.100.200:9999",
                   "125.123.136.227:9999",
                   "116.209.55.170:9999",
                   "121.61.3.6:9999",
                   "103.40.48.17:84",
                   "123.207.217.179:1080",
                   "59.62.166.222:9999",
                   "124.205.155.148:9090",
                   "125.123.143.97:9000",
                   "117.91.232.220:9999",
                   "125.123.140.163:9999",
                   "125.123.124.57:9000",
                   "111.177.167.117:9999",
                   "111.177.178.208:9999",
                   "118.24.151.76:8118",
                   "116.209.58.61:9999",
                   "113.122.169.99:9999",
                   "116.209.58.181:9999",
                   "113.122.168.120:9999",
                   "180.118.134.221:9999",
                   "182.88.160.38:8123",
                   "223.85.223.215:8081",
                   "125.123.139.49:9000",
                   "157.0.210.242:53540",
                   "115.239.24.220:9999",
                   "116.209.53.188:9999",
                   "117.191.11.108:80",
                   "112.85.130.240:9999",
                   "112.85.166.161:9999",
                   "116.209.57.154:9999",
                   "60.13.42.214:9999",
                   "116.209.56.187:9999",
                   "111.177.176.118:9999",
                   "119.57.105.25:53281",
                   "125.123.120.54:9000",
                   "115.239.25.52:9999",
                   "115.171.203.114:9000",
                   "115.151.7.166:9999",
                   "103.46.128.41:57345",
                   "111.177.185.92:9999",
                   "113.122.168.230:9999",
                   "60.13.42.235:9999",
                   "182.44.220.2:9999",
                   "111.177.166.63:9999",
                   "117.191.11.74:8080",
                   "222.189.190.111:9999",
                   "125.123.143.115:9999",
                   "58.240.232.122:808",
                   "123.207.215.186:8118",
                   "116.209.54.143:9999",
                   "116.209.55.66:9999",
                   "118.89.246.49:8118",
                   "125.123.143.201:9000",
                   "125.123.142.248:9999",
                   "59.62.164.194:9999",
                   "113.54.157.142:1080",
                   "180.117.102.172:9999",
                   "113.122.169.163:9999",
                   "111.177.167.167:9999",
                   "115.151.3.204:9999",
                   "61.184.189.43:63000",
                   "113.122.169.98:9999",
                   "111.177.173.109:9999",
                   "116.208.53.87:9999",
                   "121.196.197.17:3128",
                   "110.167.30.50:8060",
                   "116.209.53.238:9999",
                   "118.25.16.35:1080",
                   "118.24.61.165:8118",
                   "60.13.42.145:9999",
                   "111.177.186.91:9999",
                   "111.75.193.25:48449",
                   "103.205.14.129:8080",
                   "115.151.2.163:9999",
                   "59.62.164.101:9999",
                   "111.230.237.187:8118",
                   "115.151.6.107:9999",
                   "111.177.190.126:9999",
                   "116.209.53.2:9999",
                   "111.177.175.48:9999",
                   "119.57.108.65:53281",
                   "47.94.104.204:8118",
                   "111.177.168.93:9999",
                   "116.209.55.240:9999",
                   "115.151.0.231:9999",
                   "111.177.188.214:9999",
                   "119.57.108.53:53281",
                   "125.123.22.59:9000",
                   "139.199.176.215:3128",
                   "47.106.166.136:8081",
                   "123.207.55.239:1080",
                   "117.191.11.112:8080",
                   "59.62.164.61:9999"
                   ]

        ip_raw = random.choice(ip_list)

        ip = "http://" + ip_raw
        print(ip)
        request.meta['download_timeout'] = 5
        request.meta["proxy"] = ip
