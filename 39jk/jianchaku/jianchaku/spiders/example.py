# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['jbk.39.net/']
    start_urls = ['http://jbk.39.net/jiancha/search/toubu/']

    def start_requests(self):
        for i in range(48):
            url = "http://jbk.39.net/jiancha/search/toubu_p{}".format(i)
            yield Request(url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        item = {}
        div_list = response.xpath("//div[@class='item']/div[@class='res_list']")
        for  div in div_list:
            title = div.xpath("./dl/dt/h3/a/@title").extract_first()
            item["title"] = title
            url = div.xpath("./dl/dt/h3/a/@href").extract_first()
            yield Request(url,callback=self.parse_disease,meta={"item":deepcopy(item)},dont_filter=True)

    def parse_disease(self,response):
        item = response.meta["item"]

        #检查部位
        body_jiancha_raw = response.xpath("//ul[@class='infolist']/li[1]/span/a/text()").extract()
        if body_jiancha_raw is not None:
            body_jiancha = str(body_jiancha_raw).replace("['","").replace("']","").replace("[","").replace("]",
            "").replace(" ","").replace("','","、")
            if len(body_jiancha) >0:
                item["body_jiancha"] = body_jiancha
            print(item["title"],body_jiancha)


