# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.boohee.com']
    start_urls = []

    def start_requests(self):
        for i in range(1, 11):
            url = "http://www.boohee.com/food/group/{}".format(i)
            yield Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        li_list = response.xpath("//ul[@class='food-list']/li")
        for li in li_list:
            # 每一项的请求地址
            url_raw = li.xpath("./div[@class='img-box pull-left']/a/@href").extract_first()
            url = "http://www.boohee.com" + url_raw
            yield Request(url, callback=self.parse_one, dont_filter=True)

        # 翻页请求
        next_url_raw = response.xpath("//div[@class='widget-pagination']//a[text()='下一页 »']/@href").extract_first()
        if next_url_raw is not None:
            next_url = "http://www.boohee.com" + next_url_raw

            yield Request(next_url, callback=self.parse, dont_filter=True)

    def parse_one(self, response):
        title = response.xpath("//div[@class='widget-food-detail pull-left']/h3/text()").extract_first()



