# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['car.autohome.com.cn/']
    start_urls = ['https://car.autohome.com.cn/pic/']

    def parse(self, response):
        item={}
        ul_list = response.xpath("//div[@class='cartree']/ul")
        for ul in ul_list:
            li_list = ul.xpath("./li")
            for li in li_list:
                url_raw  = li.xpath(".//a/@href").extract_first()
                url = "http://car.autohome.com.cn/" + url_raw
                big_title_raw = li.xpath(".//text()").extract()
                big_title = str(big_title_raw)
                item["big_title"] = big_title

                yield scrapy.Request(url,callback=self.parse_one,meta={"item":deepcopy(item)},dont_filter=True)

    def parse_one(self,response):
        item = response.meta["item"]
        dd_list = response.xpath("//div[@class='cartree']/ul/li//dl/dd/a")
        for dd in dd_list:
            url_raw = dd.xpath("./@href").extract_first()
            url = "http://car.autohome.com.cn/" + url_raw

            title_raw = dd.xpath("./text()").extract()
            title = str(title_raw)
            item["title"] = title

            yield scrapy.Request(url,callback=self.parse_two,dont_filter=True,meta={"item":deepcopy(item)})


    def parse_two(self,response):
        item = response.meta["item"]
        info_raqw = response.xpath("//div[@class='search-pic']//div/dl/dt/text()").extract()
        info = str(info_raqw)
        item["info"] = info
        print(item)



