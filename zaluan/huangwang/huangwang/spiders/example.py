# -*- coding: utf-8 -*-
import scrapy
import json

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.gxiao8.com']
    start_urls = ['http://www.gxiao8.com']

    def parse(self, response):
        print(response.body.decode())
