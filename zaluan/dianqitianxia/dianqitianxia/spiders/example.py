# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['test.dq123.com/']
    start_urls = ['http://wx.dq123.com/data2/2/z_p/1895.jss']

    def parse(self, response):
        print(response.body.decode("gbk"))
