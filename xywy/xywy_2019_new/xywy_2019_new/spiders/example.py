# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['club.xywy.com']
    start_urls = []

    def start_requests(self):

        url_raw = "http://club.xywy.com/keshi/{}.html"
        for i in range(1, 68):
            url = url_raw.format(i)
            yield Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = {}
        li_list = response.xpath("//ul[@class='club_Date clearfix']/li")

        for li in li_list:
            url = li.xpath("./a/@href").extract_first()
            item["time"] = li.xpath("./a/text()").extract_first()

            yield Request(url, callback=self.parse_list, dont_filter=True, meta={"item": deepcopy(item)})

    def parse_list(self, response):
        item = response.meta["item"]
        div_lsit = response.xpath("//div[@class='bc mt15 DiCeng']/div[@class='club_dic']")

        for div in div_lsit:
            item["big_class"] = div.xpath("./h4/var/a/text()").extract_first()
            url = div.xpath("./h4/em/a/@href").extract_first()

            yield Request(url, callback=self.parse_detail, dont_filter=True, meta={"item": deepcopy(item)})

    def parse_detail(self, response):
        item = response.meta["item"]


