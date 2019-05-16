# -*- coding: utf-8 -*-
import scrapy
import time

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['wukong.com/']
    start_urls = ['https://www.wukong.com/']

    def parse(self, response):
        s = time.time()
        print("!!!!!!!!!!!!!!!!!!")

        yield scrapy.Request("https://www.wukong.com/",callback=self.parse_f,dont_filter=True)
        print(time.time(),"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        time.sleep(5)
        print(time.time(),"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        e = time.time()
        print(e-s,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    def parse_f(self, response):

        print(time.time(), "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")





