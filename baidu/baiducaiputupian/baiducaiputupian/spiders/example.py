# -*- coding: utf-8 -*-
import scrapy
import csv
from scrapy import Request
from copy import deepcopy
import json
import math
import os

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['image.baidu.com/']
    start_urls = []

    def start_requests(self):
        # 在初始页中传入各种菜谱的名称，构造出每种菜谱的第一页的地址
        item = {}
        file = open("F:/pycharmproject/project/baidu/title.csv", "rt", encoding="utf-8")
        read = csv.reader(file)
        for line in read:
            for i in range(50):
                item["title"] = line[0]
                url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&word={}&pn={}&rn=30".format(
                    line[0], i*30
                )
                yield Request(url, callback=self.parse, dont_filter=True, meta={"item": deepcopy(item)})

    # def parse(self, response):
    #     # 获得每种菜谱的第一页，从中获得，该种菜谱的图片的个数
    #     item = response.meta["item"]
    #     num_content_raw = json.loads(response.body)
    #     num_content = num_content_raw["displayNum"]
    #     print("!!!"*100)
    #     print(num_content)
    #     num_raw = int(num_content)/30
    #     num = math.ceil(num_raw)
    #     print("*"*50)
    #     for i in range(num):
    #         url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&word={}&pn={}&rn=30".format(
    #             item["title"], num*30
    #         )
    #         yield Request(url, callback=self.parse_disease, dont_filter=True,
    #                       meta={"item": deepcopy(item)}
    #                       )

    def parse(self,response):
        # 遍历之后的每一个菜谱的所有的图片的列表页的数据
        item = response.meta["item"]
        try:
            content = json.loads(response.body)
            data_list = content["data"]
            for data_one in data_list:
                img_title = (data_one["fromPageTitle"]).replace(" ", "")
                if item["title"] in img_title:
                    img_url = data_one["thumbURL"]  # 图片的url地址
                    img_name = img_url.replace(":","").replace(".","").replace("/",
                    "").replace("&", "").replace("=", "").replace(",", "").replace("?", "")  # 图片存储时的名字
                    item["img_name"] = img_name
                    print(img_url,"*"*10)

                    yield Request(img_url, callback=self.parse_img, dont_filter=True,
                                  meta={"item": deepcopy(item)}
                                  )
        except:
            pass


    def parse_img(self,response):
        item = response.meta["item"]

        try:
            os.mkdir("H:/caipu_img/{}".format(item["title"]))
        except:
            pass

        with open("H:/caipu_img/{}/{}.jpg".format(item["title"], item["img_name"]),"wb") as f:
            f.write(response.body)









