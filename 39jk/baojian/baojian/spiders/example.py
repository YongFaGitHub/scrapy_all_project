# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
from copy import deepcopy



class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['jbk.39.net/']
    start_urls = ['http://care.39.net/']

    def parse(self, response):
        item = {}
        a_list = response.xpath("//div[@class='new_channelnav']/ul//span/a")
        for  a in a_list:
            url = a.xpath("./@href").extract_first()
            item["url_raw"] = url
            # print(item["url"])
            yield Request(url,callback=self.parse_one,meta={"item": deepcopy(item)},dont_filter=True)

    def parse_one(self,response):
        item = response.meta["item"]
        a_list = response.xpath("//div[@class='listbox']/ul/li/span/a")
        for a in a_list:
            url = a.xpath("./@href").extract_first()
            if url is not None:
                yield Request(url,callback=self.parse_two, meta={"item": deepcopy(item)},dont_filter=True)

        page = response.xpath("//div[@class='list_page']//a[text()='下一页']/@href").extract_first()
        if page is not  None:
            next_url = item["url_raw"] + page
            # print(next_url)
            yield Request(next_url,callback=self.parse_one,meta={"item": deepcopy(item)},dont_filter=True)

    def parse_two(self,response):
        item = response.meta["item"]
        title_raw = response.xpath("//h1/text()").extract_first()
        item["title"] = title_raw

        p_list = response.xpath("//div[@class='art_con']/p")
        p_all = ""
        for p in p_list:
            p_raw = p.xpath(".//text()").extract()
            p_disease_raw = str(p_raw).replace("\\u3000","").replace("['","").replace("']",
            "").replace(" ","").replace("','","").replace("[","").replace("]",
            "").replace("\\n","").replace("\\t","").replace("\\xa0","").replace(".hzh{display:none;}",
            "").replace("\\r","").replace("\\ue5e5","").replace("▲","").replace("●","")
            a =  re.findall("(（.*?：.*?）)",p_disease_raw)
            if len(a) != 0:
                p_disease1 = p_disease_raw.replace(a[0],"")
            else:
                p_disease1 = p_disease_raw
            b = re.findall("if.*,'",p_disease_raw)
            if len(b) !=0:
                p_disease = p_disease1.replace(b[0], "")
            else:
                p_disease = p_disease1

            if len(p_disease) > 1:
                p_all = p_all + p_disease +"\n"

        item["disease"] = p_all
        if item["title"] is not None and len(item["disease"])>5:
            yield item




