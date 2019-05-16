# -*- coding: utf-8 -*-
import scrapy
import csv
from scrapy import Request
from copy import deepcopy
import os


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['nipic.com/']
    start_urls = []

    def start_requests(self):
        item = {}
        file = open("F:/pycharmproject/project/caipu_img/nituwang/nituwang/spiders/title.csv", "rt", encoding="utf-8")
        read = csv.reader(file)
        for line in read:
            item["title"] = line[0]
            url = "http://soso.nipic.com/?q={}&g=3&or=0&y=40".format(line[0])
            yield Request(url, callback=self.parse, dont_filter=True, meta={"item": deepcopy(item)})

    def parse(self, response):
        item = response.meta["item"]
        li_list = response.xpath("//ul[@class='clearfix']/li")
        if li_list is not None:
            for li in li_list:
                url_raw = li.xpath("./a/@href").extract_first()
                if url_raw is not None:
                    if "html" in url_raw:
                        # print(url_raw, "!!!"*100)
                        yield Request(url_raw, callback=self.parse_disease, dont_filter=True, meta={"item": deepcopy(
                            item)})

        next_url_raw = response.xpath(
            "//div[@class='common-page-box mt10 align-center']/a[text()='下一页']/@href").extract_first()
        if next_url_raw is not None:
            next_url = "http://soso.nipic.com" + next_url_raw

            yield Request(next_url, callback=self.parse, dont_filter=True, meta={"item": deepcopy(item)})

    def parse_disease(self,response):
        item = response.meta["item"]
        img_url = response.xpath(
            "//img[@class='works-img']/@src").extract_first()
        # print(img_url, "$"*100)
        if img_url is not None:
            name = img_url.replace(".jpg", "").replace(":", "").replace("/", "")
            item["name"] = name
            # print(item)

            yield Request(img_url, callback=self.parse_img, dont_filter=True, meta={"item": deepcopy(item)})

    def parse_img(self, response):
        item = response.meta["item"]
        try:
            os.mkdir("H:/caipu_img/nituwang/{}".format(item["title"]))
        except:
            pass

        print(item["title"], "*"*50)
        with open("H:/caipu_img/nituwang/{}/{}.jpg".format(item["title"], item["name"]), "wb") as f:
            f.write(response.body)
