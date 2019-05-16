# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['readlightnovel.org/']
    start_urls = []

    def start_requests(self):
        url_raw = 'http://www.readlightnovel.org/latest-updates/'


    def parse(self, response):
        div_list = response.xpath("//div[@class='article_lists']/div[@class='li']")
        for div in div_list:
            text = div.xpath("./div/a/text()").extract_first()
            url = div.xpath("./div/a/@href").extract_first()

            yield Request(url,callback=self.parse_disease,dont_filter=True)


    def parse_disease(self,response):
        pass



