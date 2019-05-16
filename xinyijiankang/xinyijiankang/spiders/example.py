# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from scrapy import Request
import json
"""

ERROR


"""

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['qingzhi.xinyijiankang.com']
    start_urls = ['http://qingzhi.xinyijiankang.com:9987/adminLogin?username=jingyq&password=43ae0add70fd1bda16d0700282cd8d2d']

    def parse(self, response):
        text = json.loads(response.body)
        print(text)

        url = "http://qingzhi.xinyijiankang.com:9987/psychometricsPage"

        yield Request(url, callback=self.parse_one, dont_filter=True)

    def parse_one(self, response):
        print(response.text)
        print("$######################")
        text = json.loads(response.body)
        print(text)