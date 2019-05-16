# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['a-hospital.com/']
    start_urls = ['http://www.a-hospital.com/w/%E7%96%BE%E7%97%85%E6%9D%A1%E7%9B%AE%E7%B4%A2%E5%BC%95-A']

    def parse(self,response):
        a_lsit = response.xpath("//strong[@class='selflink']/following-sibling::*")

        #每个拼音开头的地址
        for a in a_lsit:
            list_url_raw = a.xpath("./@href").extract_first()
            list_url =  "http://www.a-hospital.com" + list_url_raw

            yield Request(list_url,callback=self.parse_l,dont_filter=True)


    def parse_l(self, response):
        item = {}
        a_list = response.xpath("//div[@id='bodyContent']/ul/li/a")
        for a in a_list:
            title_raw = a.xpath("./@title").extract_first()
            title = str(title_raw)
            item["title"] = title


            url_raw = a.xpath("./@href").extract_first()
            url = "http://www.a-hospital.com" + url_raw

            yield Request(url,callback=self.parse_one,meta={"item":deepcopy(item)},dont_filter=True)


    def parse_one(self,response):
        item = response.meta["item"]
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        p_list = response.xpath("//div[@id='bodyContent']/p") + response.xpath("//div[@id='bodyContent']/h2")
        for p in p_list:
            info_raw = p.xpath(".//text()").extract()
            info = str(info_raw).replace(" ","").replace("','","")

            print(p)






