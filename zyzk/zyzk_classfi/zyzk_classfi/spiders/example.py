# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['zk120.com/']

    start_urls = ['https://www.zk120.com/baike/w/%E7%89%B9%E6%AE%8A:%E6%89%80%E6%9C%89%E9%A1%B5%E9%9D%A2']

    def parse(self, response):
        item = {}
        li_list = response.xpath("//ul[@class='mw-allpages-chunk']/li")
        for li in li_list:
            url_raw = li.xpath("./a/@href").extract_first()
            url = "https://www.zk120.com" + url_raw
            url_name = li.xpath("./a/@title").extract_first()
            item["name"] = url_name

            yield Request(url, callback=self.parse_details, dont_filter=True, meta={"item": deepcopy(item)})
        next_url_raw = response.xpath("//div[@class='mw-allpages-nav']/a[contains(text(),'下一页')]/@href").extract_first()
        if next_url_raw is not None:
            next_url = "https://www.zk120.com" + next_url_raw

            yield Request(next_url, callback=self.parse, dont_filter=True)

    def parse_details(self, response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@class='mw-normal-catlinks']/a[text()='分类']/../ul/li")

        text_all = []
        for li in li_list:
            text = li.xpath("./a/text()").extract_first()
            text_all.append(text)

        if len(text_all) > 0:
            item["classfy"] = str(text_all).replace("'", "").replace("[", "").replace("]", "")
            yield item