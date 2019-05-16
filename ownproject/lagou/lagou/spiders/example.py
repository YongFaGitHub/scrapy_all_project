# -*- coding: utf-8 -*-
import scrapy
'''
拉钩网站需要带上 headers进行访问，才会返回数据
'''

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.lagou.com']
    start_urls = ['http://www.lagou.com/zhaopin/']

    def parse(self, response):
        print(response.body.decode())
