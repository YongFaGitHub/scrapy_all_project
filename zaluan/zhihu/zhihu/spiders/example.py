# -*- coding: utf-8 -*-
import scrapy
import json
import math
from copy import deepcopy
from scrapy import Request
import csv

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['zhihu.com']
    start_urls = []

    def start_requests(self):

        file = open("F:/pycharmproject/project/zaluan/zhihu/zhihu/spiders/text.txt", "rt", encoding="utf-8")
        read = csv.reader(file)
        for line in read:
            for i in range(1, 20):
                url = "https://www.zhihu.com/api/v4/search_v3?t=general&q={}&correction=1&offset={}&limit=10&show_all_topics=0&search_hash_id=87481d6ff595d5ba726b69915aac647a".format(line[0], 2*i-1)
                print(url)

                yield Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = {}
        content = json.loads(response.body)
        list_one = content["data"]
        for one in list_one:
            q_content = one["highlight"]["title"]
            print(q_content)
            item["content"] = q_content
            yield Request("https://www.zhihu.com/",callback=self.parse_dis,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_dis(self,response):
        item = response.meta["item"]
        with open("H:one_one.csv", "a+", encoding="utf-8") as f:
            f.write(item["content"] + "\n")