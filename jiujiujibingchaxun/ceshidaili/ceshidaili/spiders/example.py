# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import random
import time


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['jbk.99.com.cn/']
    start_urls = ['http://jbk.99.com.cn/pinyin/a.html']


    def parse(self, response):
        a_list = response.xpath("//div[@class='ruby-top']/span/a")
        print(response.status)
        #
        # ip = response.xpath("//h1[@id='ipd']//text()").extract()
        # print(ip,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        if response.status != 200:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            time.sleep(1000)
        for a in a_list:
            url = a.xpath("./@href").extract_first()
            yield Request(url,callback=self.parse_one,dont_filter=True)

    def parse_one(self,response):
        item={}
        print(response.status)
        if response.status != 200:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            time.sleep(1000)
        dl_list = response.xpath("//div[@class='part-cont3']/dl")
        for dl in dl_list:
            url = dl.xpath("./dd//h3/a/@href").extract_first()
            yield Request(url,callback=self.parse_two, meta={"item": deepcopy(item)},dont_filter=True)

        #下一页的地址
        next_url = response.xpath("//div[@class='digg']/a[text()='> ']/@href").extract_first()
        if next_url is not  None:
            yield Request(next_url,callback=self.parse_one, meta={"item": deepcopy(item)},dont_filter=True)

    def parse_two(self,response):
        item = response.meta["item"]
        print(response.status)
        if response.status != 200:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            time.sleep(1000)

        url = response.xpath("//div[@id='disease']/ul/li/a[text()='病 因']/@href").extract_first()

        yield Request(url,callback=self.parse_bingyin, meta={"item": deepcopy(item)},dont_filter=True)

    #疾病病因
    def parse_bingyin(self,response):
        item = response.meta["item"]
        print(response.status)
        if response.status != 200:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            time.sleep(1000)

        url = response.xpath("//div[@id='disease']/ul/li/a[text()='症 状']/@href").extract_first()
        yield Request(url, callback=self.parse_zhengzhuang, meta={"item": deepcopy(item)}, dont_filter=True)

    #疾病症状
    def parse_zhengzhuang(self,response):
        item = response.meta["item"]
        print(response.status)
        if response.status != 200:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            time.sleep(1000)
        url = response.xpath("//div[@id='disease']/ul/li/a[text()='检 查']/@href").extract_first()
        yield Request(url, callback=self.parse_jiancha, meta={"item": deepcopy(item)}, dont_filter=True)

    #疾病检查
    def parse_jiancha(self,response):
        item = response.meta["item"]
        print(response.status)
        if response.status != 200:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            time.sleep(1000)
        url = response.xpath("//div[@id='disease']/ul/li/a[text()='预 防']/@href").extract_first()
        yield Request(url, callback=self.parse_yufang, meta={"item": deepcopy(item)}, dont_filter=True)


    #疾病预防
    def parse_yufang(self,response):
        print(response.status)
        if response.status != 200:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            time.sleep(1000)
        url = response.xpath("//div[@id='disease']/ul/li/a[text()='治 疗']/@href").extract_first()
        yield Request(url, callback=self.parse_zhiliao, dont_filter=True)

    #治疗
    def parse_zhiliao(self,response):
        print(response.status)
        if response.status != 200:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            time.sleep(1000)
        url = response.xpath("//div[@id='disease']/ul/li/a[text()='鉴 别']/@href").extract_first()
        yield Request(url, callback=self.parse_jianbie, dont_filter=True)

    #鉴别
    def parse_jianbie(self,response):
        print(response.status)
        if response.status != 200:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            time.sleep(1000)


