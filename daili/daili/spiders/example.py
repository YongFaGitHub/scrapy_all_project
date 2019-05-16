# -*- coding: utf-8 -*-
import scrapy
import json
from copy import deepcopy
import time


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['gec.ip3366.net']
    start_urls = []

    def start_requests(self):
        while True:
            item = {}
            url = 'http://ged.ip3366.net/api/?key=20181105112519230&getnum=100&anonymoustype=3&area=1&proxytype=0'
            item["header"] = "http"
            yield scrapy.Request(url, callback=self.parse,dont_filter=True,meta={"item":deepcopy(item)})
            time.sleep(5)

    def parse(self, response):
        item = response.meta["item"]
        a = response.body.decode()
        list_ip = a.split("\r\n")
        for ip in list_ip:
            item["ip"] = ip
            print(item)
    #         yield scrapy.Request("http://club.xywy.com/",dont_filter=True,callback=self.parse_cun,meta={"item":deepcopy(item)})
    #
    # def parse_cun(self,response):
    #     item = response.meta["item"]
    #     yield item


