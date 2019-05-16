# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['ditu.amap.com/']
    start_urls = ['http://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&city=100000&geoobj=19.198221%7C11.793397%7C-172.051779%7C53.547635&keywords=%E5%B9%B2%E6%9E%9C']

    def parse(self, response):
        text = json.loads(response.body)
        print(text)