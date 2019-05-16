# -*- coding: utf-8 -*-
import random
# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class XianghaSpiderMiddleware(object):
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


class XianghaDownloaderMiddleware(object):
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
class ProxyMiddleware2(object):
    def process_request(self, request, spider):
        ip_list = ["222.222.250.143:8060",
                   "125.123.140.201:9999",
                   "47.106.166.136:8081",
                   "117.191.11.102:80",
                   "118.187.58.34:53281",
                   "116.209.58.181:9999",
                   "116.209.54.143:9999",
                   "117.40.114.163:8118",
                   "116.209.53.237:9999",
                   "125.123.143.115:9999",
                   "117.191.11.72:8080",
                   "117.191.11.111:80",
                   "218.89.14.142:8060",
                   "116.209.53.238:9999",
                   "118.89.138.129:59460",
                   "39.137.168.229:8080",
                   "117.191.11.110:8080",
                   "123.207.247.86:9999",
                   "103.205.26.57:57010",
                   "113.122.169.99:9999",
                   "111.177.185.209:9999",
                   "139.129.207.72:808",
                   "117.191.11.108:80",
                   "117.191.11.79:8080",
                   "117.191.11.112:8080",
                   "222.222.236.207:8060",
                   "193.112.128.212:8118",
                   "125.73.220.18:49128",
                   "119.29.224.144:8118",
                   "119.1.97.193:36751",
                   "118.24.61.165:8118",
                   "111.230.113.238:9999",
                   "113.122.168.94:9999",
                   "117.191.11.71:80",
                   "117.114.149.10:45801",
                   "116.209.59.49:9999",
                   "117.191.11.74:8080",
                   "116.209.53.186:9999",

                   ]

        ip_raw = random.choice(ip_list)

        ip = "http://" + ip_raw
        print(ip)
        request.meta['download_timeout'] = 10
        request.meta["proxy"] = ip
