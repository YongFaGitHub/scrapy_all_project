# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from copy import deepcopy
import requests

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['ask.familydoctor.com']
    start_urls = ['http://ask.familydoctor.com.cn/v/']

    def parse(self, response):
        item ={}
        a_list = response.xpath("//div[@class='main-sec'][2]/div[@class='cont ly-page-group']/a")
        for a in a_list:
            #进入一个大类别的地址
            url = a.xpath("./@href").extract_first()
            big_class_raw = a.xpath("./text()").extract_first()
            big_class = big_class_raw
            item["big_class"] = big_class
            # print(url,"$$$$")
            yield Request(url, callback=self.parse_one, meta={"item": deepcopy(item)},dont_filter=True)

    def parse_one(self,response):
        item = response.meta["item"]
        dl_list = response.xpath("//div[@class='cont faq-list']/dl")
        for dl in dl_list:
            url = dl.xpath("./dt/p/a/@href").extract_first()
            yield Request(url, callback=self.parse_four,meta={"item": deepcopy(item)}, dont_filter=True)

        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        # print(next_url,"@@@")
        yield Request(next_url, callback=self.parse_one,meta={"item": deepcopy(item)}, dont_filter=True)

    def parse_four(self,response):
        item = response.meta["item"]

        # 问题头部
        question_title_raw = response.xpath("//h3[@class='quest-title']/text()").extract_first()
        question_title = str(question_title_raw).replace(" ","")
        item["question_title"] = question_title

        #里面的疾病名称，可能和small_class1不一样。
        small_class2_raw = response.xpath("//p[@class='illness-type']/a/text()").extract_first()
        small_class2 = str(small_class2_raw).replace(" ","")
        item["small_class2"] = small_class2

        #问题描述
        question_raw = response.xpath("//div[@class='illness-pics']/p/text()").extract_first()
        question = str(question_raw).replace("\r\n","").replace(" ","")
        item["question"] = question
        answer_raw = response.xpath("//div[@class='main-sec']/ul/li/div[@class='cont']/dl/dd/p/text()").extract()
        answer = str(answer_raw).replace("\\r\\n","").replace(" ","")
        item["answer"] = answer
        # print(item)
        yield item







 #根据几大类
    # start_urls = ['http://ask.familydoctor.com.cn/']
    #
    # def parse(self, response):
    #     item = {}
    #     li_list = response.xpath("//div[@class='section']//div[@class='sbj']/div[@class='tabs']/ul/li")
    #     for li in li_list:
    #         url = li.xpath("./a/@href").extract_first()
    #         item["big_class"] = li.xpath("./a/text()").extract_first()
    #
    #         yield Request(url, callback=self.parse_one, meta={"item": deepcopy(item)}, dont_filter=True)
    #
    # def parse_one(self,response):
    #     item = response.meta["item"]
    #     url = response.xpath("//div[@class='cont']//a[@class='more']/@href").extract_first()
    #     yield Request(url, callback=self.parse_two, meta={"item": deepcopy(item)}, dont_filter=True)
    #
    # def parse_two(self,response):
    #     item = response.meta["item"]
    #     url = response.xpath("//div[@class='cont ly-list-href']/a/@href").extract_first()
    #     yield Request(url, callback=self.parse_tree, meta={"item": deepcopy(item)}, dont_filter=True)
    #
    # def parse_tree(self,response):
    #     item = response.meta["item"]
    #     dl_list = response.xpath("//div[@class='cont faq-list']/dl")
    #     for dl in dl_list:
    #         url = dl.xpath("./dt/p/a/@href").extract_first()
    #         print(len(url),"$$$$$")
    #         yield Request(url, callback=self.parse_four, meta={"item": deepcopy(item)}, dont_filter=True)
    #
    # def parse_four(self,response):
    #     pass






