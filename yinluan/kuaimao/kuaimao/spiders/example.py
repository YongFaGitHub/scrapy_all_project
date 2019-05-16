# -*- coding: utf-8 -*-
import scrapy
'''
找不到快猫的接口
'''

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['3.com']
    start_urls = ['http://3.com/']

    def parse(self, response):
        pass
