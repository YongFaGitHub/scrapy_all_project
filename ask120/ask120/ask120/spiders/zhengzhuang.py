# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy


class ZhengzhuangSpider(scrapy.Spider):
    name = 'zhengzhuang'
    allowed_domains = ['tag.120ask.com']
    start_urls = ['http://tag.120ask.com/jibing/']

    def parse(self, response):
        item = {}
        span_list = response.xpath("//ul[@class='p_leftdivnav']/li/div[2]/span")
        for span in span_list:
            p_list = span.xpath("./p/span")
            for p in p_list:
                a_list = p.xpath("./a")
                for a in a_list:
                    url_raw = a.xpath("./@href").extract_first()
                    url = "http://tag.120ask.com" + url_raw

                    title_raw = a.xpath("./@title").extract_first()
                    item["title"] = title_raw
                    yield scrapy.Request(url,callback=self.parse_one, meta={"item": deepcopy(item)})

    def parse_one(self,response):
        item = response.meta["item"]
        url = response.xpath("//div[@class='m980 pageNav']/a[text() = '症状']/@href").extract_first()
        yield scrapy.Request(url,callback=self.parse_two, meta={"item": deepcopy(item)})

    def parse_two(self,response):
        item = response.meta["item"]
        zheng_raw = response.xpath("//div[@class='p_cleftartbox']/div[2]/text()").extract()
        zheng = str(zheng_raw).replace("[","").replace("]","").replace("'","").replace(" ","").replace("\\r\\n,","").replace("\\u3000","").replace("\\xa0","").replace("。,","。").replace("、,","").replace(",、","")
        item["zheng"] = zheng
        # print(item)
        yield item