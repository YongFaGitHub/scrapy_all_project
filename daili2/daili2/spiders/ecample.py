# -*- coding: utf-8 -*-
import scrapy
import time
import json

class EcampleSpider(scrapy.Spider):
    name = 'ecample'
    allowed_domains = ['httpbin.org/get']
    start_urls = []

    def start_requests(self):
        while 1:
            url = 'http://fetch.bestzsj.com/v1/validate_ip_https'
            yield scrapy.Request(url, callback=self.parse, dont_filter=True, )
            # time.sleep(3)

    def parse(self, response):
        print("@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(response.body)
        print()






    #     yield scrapy.Request("http://httpbin.org/get",callback=self.ex,dont_filter=True)
    #
    #
    # def ex(self,response):
    #     print("%"*100)
    #
