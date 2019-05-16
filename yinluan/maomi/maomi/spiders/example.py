# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['582tt.com/']
    start_urls = ['https://www.582tt.com/index/home.html']

    def parse(self, response):
        pass
