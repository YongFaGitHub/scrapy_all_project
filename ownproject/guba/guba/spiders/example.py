# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['guba.eastmoney.com/']
    start_urls = ['http://guba.eastmoney.com/']

    def start_requests(self):
        for i in range(1,100000):
            url = "http://guba.eastmoney.com/default_{}.html".format(i)

            yield Request(url,callback=self.parse,dont_filter=True)



    def parse(self, response):
        # print(response.body.decode())
        li_list = response.xpath("//ul[@class='newlist']/li")
        item = {}
        for li in li_list:
            #阅读数
            read_num = li.xpath("./cite[1]/text()").extract_first()
            item["read_num"] = read_num
            #评论数
            write_num = li.xpath("./cite[2]/text()").extract_first()
            item["write_num"] = write_num
            #作者
            aut = li.xpath("./cite[@class='aut']/a/text()").extract_first()
            item["aut"] = aut
            #发表日期
            data_time = li.xpath("./cite[@class='data']/text()").extract()
            item["data_time"] = data_time
            #最后更新时间
            last_time = li.xpath("./cite[@class='last']/text()").extract()
            item["last_titme"] = last_time
            #所属贴吧
            tieba_name = li.xpath("./span/a[1]/text()").extract_first()
            item["tieba_name"] = tieba_name
            #title名称
            title = li.xpath("./span/a[@class='note']/@title").extract_first()
            item["title"] = title
            url_raw = li.xpath("./span/a[@class='note']/@href").extract_first()
            url = "http://guba.eastmoney.com" + url_raw
            # print(url)

            yield Request(url,callback=self.parse_disease,meta={"item":deepcopy(item)},dont_filter=True)

        # next_page_raw = response.xpath("//a[text()='下一页']/@href").extract_first()
        # print(next_page_raw,"#####################")
        # if next_page_raw is not None:
        #     next_page = "http://guba.eastmoney.com" + next_page_raw
        #     yield Request(next_page,callback=self.parse,meta={"item":deepcopy(item)})


    def parse_disease(self,response):
        item = response.meta["item"]
        print(item)






