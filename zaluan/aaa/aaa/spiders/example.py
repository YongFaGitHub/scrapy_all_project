# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['10.19.248.200:31419/']
    start_urls = []

    def start_requests(self):
        url = "http://10.19.248.200:31419/enn190101/data"
        files = {"files[]": open("F:\知识图谱\加载两个owl\enn20190131.owl", "rb")}
        yield FormRequest(url, callback=self.parse, dont_filter=True, formdata=files)

    def parse(self, response):
        print(response.body)
