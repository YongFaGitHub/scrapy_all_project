# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['news.pconline.com']
    start_urls = ['https://news.pconline.com.cn/it/']

    def parse(self, response):
        print(response.body)
        li_list = response.xpath("//div[@class='list-wrap']/ul/li")
        for li in li_list:
            text = li.xpath(".//a/img/@src").extract_first()
            print(text, "*"*20)