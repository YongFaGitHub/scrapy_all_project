# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import json
import time
import random


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['wukong.com/']
    start_urls = ['https://www.wukong.com/']

    def parse(self, response):
        item = {}
        header = {
            "cookie": "tt_webid=6626204913008412164; wendacsrftoken=3369c7ab7c433a99e0f5c29f46b27774; tt_webid=6626204913008412164; answer_finalFrom=; cookie_tt_page=97332cc2ca86d7f3c5e77624c96aca0f; _ga=GA1.2.1229206126.1542783557; _gid=GA1.2.1477376751.1542783557; answer_enterFrom=; wenda_last_concern_id=6215497899774577154"}

        id_list = ["6215497895248923137","6215497899774577154"]  #
        # for i in range(4):
        id = random.choice(id_list)
        # url = "https://www.wukong.com/wenda/web/nativefeed/brow/?concern_id={}&t=1542853849252&max_behot_time={}".format(
        #     id, int(1542793935) - 30*i)
        url = "https://www.wukong.com/wenda/web/nativefeed/brow/?concern_id={}".format(id)
        if id == "6215497895248923137":
            item["class_name"] = "健康"
        else:
            item["class_name"] = "美食"
        time.sleep(1)
        # url = "https://www.wukong.com/wenda/web/nativefeed/brow/?concern_id=6215497899774577154&t=1542787497627&max_behot_time=1542787925"
        yield Request(url, callback=self.parse_json, dont_filter=True, headers=header, meta={"item": deepcopy(item)})

#
    def parse_json(self, response):
        content = json.loads(response.body)
        item = response.meta["item"]
        data_list = content["data"]
        if len(data_list) < 2:
            print('静等五秒')
            time.sleep(5)

        else:
            for data in data_list:
                question = data["question"]["title"]
                item["question"] = question

                yield item




                url = "https://www.wukong.com/"
                time.sleep(5)
                yield Request(url, callback=self.parse_fin, dont_filter=True)

    def parse_fin(self, response):
        item = response.meta["item"]
        yield item


        time.sleep(2)
        yield Request("https://www.wukong.com/", callback=self.parse, dont_filter=True)