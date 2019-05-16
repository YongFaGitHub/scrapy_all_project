# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.tianyancha.com']
    start_urls = ['http://www.tianyancha.com/']
    def __init__(self):
        self.list1=[]

    def parse(self, response):
        url_list = response.xpath("//div[@class='company_container mainv2_tab3']/div[2]//a[@event-name='分类搜索']") #按照区域查询的标签锁定

        # print(url_list)
        for url in url_list:
            name = url.xpath("./@href").extract_first()
            self.list1.append(name)
        list2 = set(self.list1)

        for li in list2:
            # print(li)
            yield Request(li,callback=self.parse_one, dont_filter = True)


    def parse_one(self,response):
        #//a/following-sibling::*
        # print("#######################3")
        div_list = response.xpath("//text[@class='tyc-num']/text()")
        # div_list = response.xpath("//div[@class='cateSubItem position-abs b-c-white new-border border-right-none border-shadow']/div[1]/following-sibling::*")
        for div in div_list:
            # url_list = div.xpath('./div[2]/*[not(contains(a(text()="全部"))]')
            # for url in url_list:
            #     next_url = url.xpath("./@href").extract_first()
            #     print(next_url,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print(div,"####################################################")


            # print(name)