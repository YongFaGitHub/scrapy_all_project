# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import json
import os
import csv


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['food.boohee.com']
    start_urls = []

    def start_requests(self):
        item = {}
        url ="http://food.boohee.com/fb/v1/search?page=1&order_asc=desc&q={}"

        file = open("E:/pycharmproject/project/bohe/boheapp/boheapp/spiders/name.txt", "rt")
        read = csv.reader(file)

        for line in read:
            name = line[0]
            item["classfy"] = "gi_gl"
            item["name"] = name
            url = "http://food.boohee.com/fb/v1/search?page=1&order_asc=desc&q={}".format(name)
            yield Request(url, callback=self.parse, dont_filter=True, meta={"item": deepcopy(item)})

    def parse(self, response):
        item = response.meta["item"]
        content = json.loads(response.body)
        code = ""
        for one_dict in content["items"]:
            if one_dict["name"] == item["name"]:
                code = one_dict["code"]
                item["img_url"] = one_dict["thumb_image_url"]
                break

        if len(code) > 0:
            url = "http://food.boohee.com/fb/v1/foods/{}".format(code)

            yield Request(url, callback=self.parse_details, dont_filter=True, meta={"item": deepcopy(item)})

    def parse_details(self, response):
        item = response.meta["item"]
        content = json.loads(response.body)

        item["gi"] = content["gi"]

        item["gl"] = content["gl"]
        item["GL"] = content["lights"]["gl"]
        item["GI"] = content["lights"]["gi"]
        if len(item["gl"]) > 0:
            yield item
            yield Request(item["img_url"], callback=self.parse_img, dont_filter=True, meta={"item": deepcopy(item)})

    def parse_img(self, response):
        item = response.meta["item"]
        try:
            os.mkdir("F:/img/bohee/gi_gl/{}".format(item["classfy"]))
        except:pass

        with open("F:/img/bohee/gi_gl/{}/{}.jpg".format(item["classfy"], item["name"]), "wb") as f:
            f.write(response.body)

