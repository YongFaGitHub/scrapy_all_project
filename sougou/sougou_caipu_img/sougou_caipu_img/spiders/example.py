# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['sogou.com/']
    start_urls = []

    def start_requests(self):
        url = "https://pic.sogou.com/pics?query=%D0%A1%BC%A6%EC%C0%C4%A2%B9%BD&policyType=1&mode=1&start=48&reqType=ajax&reqFrom=result&tn=0"
        yield scrapy.Request(url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        print(response.body)
