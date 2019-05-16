# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.ewsos.com']
    start_urls = ['http://jibing.ewsos.com/jibing/keshi']

    def parse(self, response):
        li_list = response.xpath("//ul[@id='menu']/li")
        for li in li_list:
            big_class_url = li.xpath("./a/@href").extract_first()
            yield Request(big_class_url,callback=self.parse_one,dont_filter=True)

    def parse_one(self,response):
        li_list = response.xpath("//div[@class='leftPinBox1']/ul/li")
        for li in li_list:
            url = li.xpath("./a/@href").extract_first()
            yield Request(url,callback=self.parse_disease,dont_filter=True)


    def parse_disease(self,response):
        item = {}

        #介绍
        disease_raw = response.xpath("//div[@class='content2']/div[1]/text()").extract()
        disease = str(disease_raw).replace("[","").replace("]","").replace("\\r","").replace("\\n",
        "").replace(" ","").replace("'","").replace("\\u3000","")
        # print(disease)
        item["disease"] = disease

        #科室
        a_keshi_raw= response.xpath("//strong[text()='科室：']/following-sibling::*//text()").extract()
        keshi = str(a_keshi_raw).replace("]","").replace("[","").replace(" ","").replace("','","、").replace("'","")
        item["keshi"] = keshi

        #症状
        zhengzhuang_raw = response.xpath("//span[@class='DivAll']/a/text()").extract()
        zhengzhuang = str(zhengzhuang_raw).replace("]","").replace("[","").replace(" ","").replace("','",
        "、").replace("'","")
        item["zhengzhuang"] = zhengzhuang

        jiancha_raw = response.xpath("//span[@class='DivAll2']/a/text()").extract()
        jiancha = str(jiancha_raw).replace("]","").replace("[","").replace(" ","").replace("','",
        "、").replace("'","")
        # print(jiancha)
        item["jiancha1"] = jiancha

        url = response.xpath("//div[@class='leftsidebar a_06']/ul/li/a[text()='病因']/@href").extract_first()
        yield Request(url,callback=self.bingyin, meta={"item": deepcopy(item)},dont_filter=True)

    def bingyin(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='contArticle']/p")
        p_info_s = ""
        for p in p_list:
            p_info_raw = p.xpath("./text()").extract()
            p_info = str(p_info_raw).replace("[","").replace("]","").replace("\\r","").replace("\\n",
        "").replace(" ","").replace("'","").replace("\\u3000","").replace('\\xa0',"")

            p_info_s = p_info_s + p_info +"\n"
        # print(p_info_s)
        item["bingyin"] = p_info_s

