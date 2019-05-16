# -*- coding: utf-8 -*-
import scrapy
import json
import csv
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['dajiazhongyi.com']
    start_urls = []

    def start_requests(self):
        item = {}
        file = open("C:/Users/root/Desktop/xuewei_url.csv","rt", encoding="utf-8")

        read = csv.reader(file)

        for line in read:

            if len(line[2]) > 20:
                item["wen"] = line[1]
                item["name"] = line[0]
                url = line[2]
                yield scrapy.Request(url, callback=self.parse,
                                     dont_filter=True, meta={"item": deepcopy(item)})

    def parse(self, response):
        item = response.meta["item"]
        with open("H:/大家中医_穴位_img/{}/{}.jpg".format(item["wen"], item["name"]), "wb") as f:
            f.write(response.body)