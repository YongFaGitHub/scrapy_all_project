# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['mvyxws.com/']
    start_urls = ['http://www.mvyxws.com/']

    def parse(self, response):
        # print(response.body.decode())
        item = {}
        div_list = response.xpath("//div[@class='category']")
        for div in div_list:
            big_class_raw = div.xpath("./h2/text()").extract_first()
            big_class = str(big_class_raw)
            item["big_class"] = big_class
            # print(big_class)
            a_list = div.xpath("./p/a")
            for a in a_list:
                title_raw = a.xpath("./@title").extract_first()

                title_cut = str(title_raw).split("//")
                title = title_cut[0]
                item["title"] = title

                url_raw = a.xpath("./@href").extract_first()

                url  = "http://www.mvyxws.com" + url_raw
                item["url"] = url
                yield Request(url,callback=self.parse_disease,meta={"item":deepcopy(item)},dont_filter=True)



    def parse_disease(self,response):
        item = response.meta["item"]

        li_list = response.xpath("//ul[@class='jb-list']/li")
        for  li in li_list:
            query_raw = li.xpath("./a/@title").extract_first()
            query = str(query_raw)
            item["query"] = query

            yield Request(item["url"],callback=self.parse_f,meta={"item":deepcopy(item)},dont_filter=True)


    def parse_f(self,response):
        item = response.meta["item"]
        yield item









