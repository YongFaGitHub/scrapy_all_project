# -*- coding: utf-8 -*-
import scrapy
import csv
from scrapy import Request
from copy import deepcopy
import os


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ["meishi.cc/"]
    start_urls = []

    def start_requests(self):
        item = {}
        file = open("F:/pycharmproject/project/meishijie/meishijiecaipuimg/meishijiecaipuimg/spiders/title.csv",
                    "rt", encoding="utf-8")
        read = csv.reader(file)
        for line in read:
            item["old_title"] = line[0]
            url = "https://so.meishi.cc/index.php?q={}".format(line[0])
            yield Request(url, callback=self.parse, dont_filter=True,
                          meta={"item": deepcopy(item)})

    def parse(self, response):
        item = response.meta["item"]
        div_list = response.xpath("//div[@class='search2015_cpitem_w clearfix']/div")
        for div in div_list:
            img_name = div.xpath("./a[@class='img']/@title").extract_first()
            if item["old_title"] in img_name:
                url_details = div.xpath("./a[@class='img']/@href").extract_first()
                yield Request(url_details, callback=self.parse_details, dont_filter=True,
                              meta={"item": deepcopy(item)})

        next_url_raw = response.xpath("//div[@class='search_page']/a[text()='下一页']/@href").extract_first()
        if next_url_raw is not  None:
            next_url = "https://so.meishi.cc" + next_url_raw
            yield Request(next_url, callback=self.parse, dont_filter=True,
                          meta={"item": deepcopy(item)})

    def parse_details(self, response):
        item = response.meta["item"]
        img_url = response.xpath("//div[@class='cp_headerimg_w']/img/@src").extract_first()
        if img_url is not None:
            img_name = str(img_url).replace(".", "").replace("/", "").replace(':', "").replace("jpg", "")
            item["img_name"] = img_name

            yield Request(img_url, callback=self.parse_img, dont_filter=True,
                          meta={"item": deepcopy(item)})

    def parse_img(self, response):
        item = response.meta["item"]

        try:
            os.mkdir("H:/caipu_img/meishijie/{}".format(item["old_title"]))
        except:
            pass

        with open("H:/caipu_img/meishijie/{}/{}.jpg".format(item["old_title"], item["img_name"]), "wb") as f:
            f.write(response.body)

        print(item["old_title"])
