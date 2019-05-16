# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['ci.qiuyi.cn']
    start_urls = ['http://ci.qiuyi.cn/html/disease/index.html']

    def parse(self, response):
        item = {}
        div_list = response.xpath("//div[@class='map_list_block']/div")
        for div in div_list:
            big_title_raw  = div.xpath("./h3/a/text()").extract_first()
            big_title  = str(big_title_raw)
            item["big_title"] = big_title

            a_lsit = div.xpath("./div/a")
            for a in a_lsit:
                title_raw = a.xpath("./text()").extract_first()
                title = str(title_raw)
                item["title"] = title

                item[""]

                url = a.xpath("./@href").extract_first()
                yield Request(url,callback=self.parse_disease,dont_filter=True,meta={"item":deepcopy(item)})


    def parse_disease(self,response):
        item = response.meta["item"]
        print("###############################")
        a_lsit = response.xpath("//dl[@class='blue change_s']/dd")

        for a in a_lsit:
            print("@@@@@@@@@@@@@@@@@")
            a_s = a.xpath("./a/@href").extract_first()
            # print(a_s)
            if a_s is not None:
                noble = int(a_s.replace("#bs","")) -1
                print(noble)
                info_list = response.xpath("//div[@class='bk_c bor clearfix']")
                info = (info_list[noble]).xpath("./p//text()").extract()
                print(info)











