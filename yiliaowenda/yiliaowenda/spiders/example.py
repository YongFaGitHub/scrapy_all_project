# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from scrapy.http import Request
import time

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.yiliaoask.net/']
    start_urls = ['http://www.yiliaoask.net/']

    def parse(self, response):
        item= {}
        div_list = response.xpath("//div[@class='category-nav']/div")
        for div in div_list:
            li_list = div.xpath("./ul/li")
            for li in li_list:
                item["titleClass"] = li.xpath("./a/text()").extract_first()
                url = li.xpath("./a/@href").extract_first()
                yield Request(url,callback=self.parse_next,meta={"item":deepcopy(item)},dont_filter=True)
                time.sleep(1)


    def parse_next(self,response):
        item = response.meta["item"]
        time.sleep(0.3)
        # print("%%%")
        a_list = response.xpath("//tbody/tr/td[@class='title']/div/div/a/@href").extract()
        for a in a_list:
            yield  Request(a,callback=self.parse_two,meta={"item":deepcopy(item)},dont_filter=True)
    def parse_two(self,response):
        time.sleep(0.5)
        item = response.meta["item"]
        question_raw = response.xpath("//div[@class='questionbox']/div[@class='description']/text()").extract_first()
        question = str(question_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '').replace("[", "").replace("]", "").replace(" ","")
        item["question"]=question


        answer_raw = response.xpath("//ul[@class='net-answer-list']/li/div/div[@class='anscontent']/text()").extract()
        answer = str(answer_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '').replace("[", "").replace("]", "").replace(" ","")
        item["answer"] = answer
        yield item


