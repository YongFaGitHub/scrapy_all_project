# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['image.baidu.com']
    start_urls = []

    def start_requests(self):
        list_name = ["人像照片男", "人像照片女"]
        for list_one in list_name:
            for i in range(1, 334):

                url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30&gsm=1e&1556170389793=".format(list_one, list_one, i*30)

                yield Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = {}
        content = json.loads(response.body)
        data_list = content["data"]
        for dict_one in data_list:

            try:
                url = dict_one["hoverURL"]
                item["name"] = url.split("/")[-1]
                print(url)
                print(item["name"])
                yield Request(url, callback=self.parse_img, dont_filter=True, meta={"item": deepcopy(item)})

            except:pass

    def parse_img(self, response):
        item = response.meta["item"]

        with open("F:/img/baidu_img/{}".format(item["name"]), "wb") as f:
            f.write(response.body)
