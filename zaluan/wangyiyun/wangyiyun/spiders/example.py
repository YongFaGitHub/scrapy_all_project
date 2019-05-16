# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['music.163.com/']
    start_urls = ['https://music.163.com/discover/artist/cat?id=1001']

    def parse(self, response):
        item = {}
        div_list = response.xpath("//div[@class='blk']")
        for div in div_list:
            # big_class
            big_class_name = div.xpath("./h2/text()").extract_first()
            item["big_class_name"] = big_class_name

            #每个大分类下的小分类
            li_list = div.xpath("./ul/li")
            for li in li_list:
                # 小分类地址
                small_url = "https://music.163.com" + li.xpath("./a/@href").extract_first()
                # 小分类名称
                small_class_name = li.xpath("./a/text()").extract_first()
                item["small_class_name"] = small_class_name

                yield Request(small_url,callback=self.parse_small_class,dont_filter=True,
                              meta={"item": deepcopy(item)})

    def parse_small_class(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//ul[@class= 'n-ltlst f-cb']/li/a[@class='']")
        # 拿到小分类里面的字母开头的url
        for li in li_list:
            num_url = "https://music.163.com" + li.xpath("./@href").extract_first()
            num_name = li.xpath("./text()").extract_first()
            item["num_name"] = num_name
            yield Request(num_url,callback=self.parse_num_list,dont_filter=True,
                          meta={"item": deepcopy(item)}
                          )

    '''
    到此处被封
    '''

    def parse_num_list(self,response):
        item = response.meta["item"]



