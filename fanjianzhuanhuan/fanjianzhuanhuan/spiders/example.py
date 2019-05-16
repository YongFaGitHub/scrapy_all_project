# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.fantizi5.com/']
    start_urls = []

    def start_requests(self):
        list = ["http://www.fantizi5.com/map.html"]
        for i in range(2,19):
            url_num = "http://www.fantizi5.com/map_{}.html".format(i)
            list.append(url_num)
        for num in list:
            yield Request(num,callback=self.parse,dont_filter=True)

    def parse(self,response):
        print("@@@@@@@@@@@@@@@@")
        li_list = response.xpath("//div[@class='daquanlist']/ul/li")
        for li in li_list:
            info = li.xpath("./a/text()").extract_first()

            # print(info)
            with open("H:/pycharmproject/project/fanjianzhuanhuan/fanjianzhuanhuan/spiders/data.txt","a+",encoding="utf-8") as f:
                f.write(info)
                f.write("\n")
