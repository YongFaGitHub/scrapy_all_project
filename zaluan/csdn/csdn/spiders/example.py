# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['csdn.net']
    start_urls = ['https://www.csdn.net/']

    def parse(self, response):
        response.xpath("//div[@class='']")


