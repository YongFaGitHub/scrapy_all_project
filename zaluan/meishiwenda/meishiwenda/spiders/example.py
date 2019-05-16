# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['xinshipu.com/']
    start_urls = []

    def start_requests(self):
        for i in range(1, 834):
            url = "http://www.xinshipu.com/question?page={}".format(i)
            yield Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):

        # print(response.body.decode())
        item = {}
        li_list = response.xpath("//ul[@class='ask-list']/li")
        for li in li_list:
            question = li.xpath("./a/text()").extract()

            item["question"] = str(question).replace("  ", "，").replace("\\n","").replace(",",
            "，").replace(" ", "").replace("['", "").replace("']", "")

            url = "http://www.xinshipu.com/"
            yield Request(url, callback=self.parse_fin, dont_filter=True, meta={"item": deepcopy(item)})

    def parse_fin(self, response):

        item = response.meta["item"]
        # print(item)
        yield item

