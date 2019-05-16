# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['weixin.sogou.com/']
    start_urls = []

    def start_requests(self):
        list = ["糖尿病"]  #词条列表
        for i in list:
            url  = "http://weixin.sogou.com/weixin?type=2&query={}".format(i)
            print(url)
            yield Request(url,callback=self.parse)

    def parse(self, response):
        li_list = response.xpath("//ul[@class='news-list']/li")
        for li in li_list:
            gongzonghao_url = li.xpath("./div[@class='txt-box']/div/a/@href").extract_first()
            print(gongzonghao_url)

        next_url_raw = response.xpath("//div[@id='pagebar_container']/a[text()='下一页']/@href").extract_first()
        next_url = "http://weixin.sogou.com/weixin" + next_url_raw
        # print(next_url)
        yield Request(next_url,callback=self.parse,dont_filter=True)
