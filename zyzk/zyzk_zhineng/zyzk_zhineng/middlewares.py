# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import requests
import logging
import json
import pymysql
import random

from scrapy import signals


class ZHINENGMiddleWare(object):
    def __init__(self, cookies_pool_url):
        self.logging = logging.getLogger("FENZHENMiddleWare")
        self.cookies_pool_url = cookies_pool_url

    def get_random_cookies(self):
        try:
            response = requests.get(self.cookies_pool_url)
        except Exception as e:
            self.logging.info('Get Cookies failed: {}'.format(e))
        else:
            # 在中间件中，设置请求头携带的Cookies值，必须是一个字典，不能直接设置字符串。
            cookies = json.loads(response.text)
            self.logging.info('Get Cookies success: {}'.format(response.text))
            return cookies

    @classmethod
    def from_settings(cls, settings):
        obj = cls(
            cookies_pool_url=settings['ZHINENG_COOKIES_URL']
        )
        return obj

    def process_request(self, request, spider):
        request.cookies = self.get_random_cookies()
        return None





class ZyzkZhinengSpiderMiddleware(object):
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


class ZyzkZhinengDownloaderMiddleware(object):
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
import time
# class ProxyMiddleware2(object):
#     def __init__(self):
#
#         conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="jing1995",  charset='utf8', database="daili",)
#         self.cs1 = conn.cursor()
#
#     def re_ip(self):
#         connt = self.cs1.execute("select ip,port from daili_pool")
#         proxy_list = []
#         res = self.cs1.fetchall()
#         for one in res:
#             proxy_list.append("http://" + one[0] + ":" + one[1])
#             ip = random.choice(proxy_list)
#             return ip
#
#     def process_request(self, request, spider):
#         ip = self.re_ip()
#         request.meta["proxy"] = ip

