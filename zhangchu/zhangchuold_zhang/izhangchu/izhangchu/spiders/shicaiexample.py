# -*- coding: utf-8 -*-
import scrapy


class ShicaiexampleSpider(scrapy.Spider):
    name = 'shicaiexample'
    allowed_domains = ['h5.izhangchu.com']
    start_urls = ['http://h5.izhangchu.com/category/subtype.html?type=2']

    def parse(self, response):
        dl_list = response.xpath("//div[@id='MaterialCategory-wrap']/dl")
        for dl in dl_list:
            li_list = dl.xpath(".//ul/li")
            for li in li_list:
                text = li.xpath("./a/text()").extract_first()
                print(text)