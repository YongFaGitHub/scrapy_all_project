# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy



class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['http://www.9939.com/']
    start_urls = []

    def start_requests(self):
        for i in range(1,649):
            url = "http://jb.9939.com/jbzz_t2/?page={}".format(str(i))
            yield Request(url,callback=self.parse,dont_filter=True)


    def parse(self, response):
        div_list = response.xpath("//div[@class='doc_anwer disline']")
        for div in div_list:
            disease_url =  div.xpath("./div[1]/div/h3/a/@href").extract_first()

            yield Request(disease_url,callback=self.parse_one,dont_filter=True)

    def parse_one(self,response):
        xiangxi_url_raw = response.xpath("//div[@class='widsp']//a[text()='[详细]']/@href").extract_first()
        xiangxi_url = "http://jb.9939.com" + xiangxi_url_raw
        yield Request(xiangxi_url,callback=self.parse_two,dont_filter=True)



    def parse_two(self,response):
        item={}

        title_raw = response.xpath("//h1[@class='sypmt']/b/text()").extract_first()
        title = str(title_raw)
        item["title"] = title

        disease_raw = response.xpath("//div[@class='tost nickn bshare prevp curere spread graco']/p[2]/text()").extract_first()
        disease = str(disease_raw).replace("\u3000","").replace("\\u3000","").replace("\xa0","").replace("\\xa0",
        "").replace("\n","").replace("\\n","").replace("\r","").replace("\\r","")
        item["disease"] = disease
        # print(disease)


        yield item
        # print(item)
