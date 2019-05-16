# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['7tin.cn/']
    start_urls = ['http://www.7tin.cn/']

    def parse(self, response):
        # print(response.body.decode())
        li_list = response.xpath("//div[@class='index_content_tab']/ul/li")
        for li in li_list:
            text_raw = li.xpath(".//text()").extract()
            class_name = str(text_raw).replace("['", "").replace("']", "")
            # print(class_name)
            url_rew = li.xpath("./a/@href").extract_first()
            if url_rew is not None:
                url = "http://www.7tin.cn/" + url_rew.replace(".", "")

                yield Request(url,callback=self.parse_list,dont_filter=True)

    def parse_list(self,response):
        li_list = response.xpath("//div[@class='newslist xfa-newslist clearfix']/li")
        pass





