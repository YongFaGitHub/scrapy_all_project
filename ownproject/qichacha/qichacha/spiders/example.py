# -*- coding: utf-8 -*-
import scrapy
'''
企查查 需要带上headers进行页面的访问
'''

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.qichacha.com']
    start_urls = ['https://www.qichacha.com/search?key=新奥集团']

    def parse(self, response):
        print(response.body.decode())
