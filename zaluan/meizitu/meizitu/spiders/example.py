# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import os

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['3.com']
    start_urls = ['http://www.mzitu.com/page/0/']

    def parse(self, response):

        # 主页面的每个图片集的li以及进入的url
        li_list = response.xpath("//ul[@id='pins']/li")
        for li in li_list:
            url = li.xpath('./a/@href').extract_first()
            yield Request(url, callback=self.parse_disease, dont_filter=True)


        # 获取图片集的下一页
        next_page_url = response.xpath("//div[@class='nav-links']/a[text()='下一页»']/@href").extract_first()
        if next_page_url is not None:
            yield Request(next_page_url,callback=self.parse, dont_filter=True)
    def parse_disease(self, response):
        item = {}
        # 图片的地址
        '''Beautyleg 美腿写真 No.984 Cindy'''
        class_name_raw = response.xpath("//div[@class='main-image']/p/a/img/@alt").extract()
        class_name = (class_name_raw[0]).replace(" ", "").replace(".", "")
        item["class_name"] = class_name


        img_url = response.xpath("//div[@class='main-image']/p/a/img/@src").extract_first()
        one_name = (img_url.split("/"))[-1]
        item["one_name"] = one_name
        yield Request(img_url, callback=self.parse_cun, dont_filter=True, meta={"item": deepcopy(item)})

        # 图片集中下一个图片所在的页面
        next_url = response.xpath("//div[@class='pagenavi']/a/span[text()='下一页»']/../@href").extract_first()
        if next_url is not None:
            yield Request(next_url, callback=self.parse_disease, dont_filter=True)

    def parse_cun(self, response):
        item = response.meta["item"]

        try: os.mkdir("L:/美女图片/meizitu/{}".format(item["class_name"]))
        except:pass

        with open("L:/美女图片/meizitu/{}/{}".format(item["class_name"], item["one_name"]),"wb") as f:
            f.write(response.body)
