# -*- coding: utf-8 -*-
import scrapy
import csv
import re
from scrapy import Request
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['http://ovationhealth.enn.cn']
    start_urls = []


    def start_requests(self):
        file = open("H:/pycharmproject/project/img_18720/img_18720/spiders/img.txt","rt")

        read = csv.reader(file)
        item = {}
        for line in read:
            url = line[0]

            name_raw = re.findall("filePath=(.*?)=",url)
            name = name_raw[0]
            item["name"] = name

            yield Request(url,callback=self.parse,meta={"item":deepcopy(item)},dont_filter=True)




    def parse(self, response):
        item = response.meta["item"]

        with open("I:/img/{}.jpeg".format(item["name"]),"wb") as f:
            f.write(response.body)




