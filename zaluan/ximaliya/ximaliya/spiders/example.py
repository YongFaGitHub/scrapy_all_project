# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['ximalaya.com']
    start_urls = ['https://www.ximalaya.com/category/']

    def parse(self, response):
        item = {}

        div_list = response.xpath("//div[@class='plates Kx']/div")
        for div in div_list:
            big_class = div.xpath("./h2/text()").extract_first()
            item["big_calss"] = big_class

            small_div_list = div.xpath("./div[@class='body Kx']")
            for small_div in small_div_list:
                section_list = small_div.xpath("./section[@class='subject_wrapper Kx']")
                for section in section_list:
                    small_class = section.xpath("./div[@class='subject Kx']//h2/text()").extract_first()
                    item["small_class"] = small_class
                    a_list = section.xpath("./div[@class='list Kx']/a")
                    for a in a_list:
                        url = "https://www.ximalaya.com" + a.xpath("./@href").extract_first()
                        ssmall_class = a.xpath("./text()").extract_first()
                        item["ssmall_class"] = ssmall_class
                        yield Request(url, callback=self.parse_disease, dont_filter=True,
                                      meta={"item": deepcopy(item)})

    def parse_disease(self, response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@class='content']/ul/li")
        for li in li_list:
            big_title = li.xpath("./div/a[@class='album-title line-2 lg  Iki']/@title").extract_first()
            item["big_title"] = big_title
            url = "https://www.ximalaya.com" + li.xpath(
                "./div/a[@class='album-title line-2 lg  Iki']/@href").extract_first()

            yield Request(url, callback=self.parse_list, dont_filter=True,
                          meta={"item": deepcopy(item)})

    def parse_list(self, response):
        item = response.meta["item"]
        div = response.xpath("//div[@class='sound-list rC5T']")
        li_list = div.xpath("./ul/li")
        for li in li_list:
            title = li.xpath("./div[@class='text rC5T']/a/@title").extract_first()
            item["title"] = title
            url = "https://www.ximalaya.com" + li.xpath("./div[@class='text rC5T']/a/@href").extract_first()
            yield Request(url, callback=self.parse_disease_one, dont_filter=True,
                          meta={"item": deepcopy(item)})

    def parse_disease_one(self, response):
        item = response.meta["item"]

