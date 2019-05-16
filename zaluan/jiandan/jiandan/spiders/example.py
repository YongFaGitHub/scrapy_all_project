# -*- coding: utf-8 -*-
import scrapy
import base64
from copy import deepcopy


def decode_base64(data):
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    return base64.b64decode(data)

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/ooxx']



    def parse(self, response):
        item = {}
        li_list = response.xpath("//ol[@class='commentlist']/li")
        for li in li_list:
            span_list = li.xpath(".//div[@class='text']/p/span[@class='img-hash']")
            for span in span_list:
                url_hash = span.xpath("./text()").extract_first()
                item["name"] = url_hash
                if url_hash is not None   :
                    # print(url_hash,"@"*100)
                    url_raw = decode_base64(url_hash).decode('utf8')
                    url = "http:" + url_raw
                    yield scrapy.Request(url, callback=self.parse_disease,dont_filter=True,meta={"item": deepcopy(item)})


        next_url_raw = response.xpath("//a[text()='下一页']/@href").extract_first()
        # print(next_url_raw)
        if next_url_raw is not None:
            next_url = "http:" +next_url_raw
            yield scrapy.Request(next_url, callback=self.parse,dont_filter=True)


    def parse_disease(self,response):
        item = response.meta["item"]
        item["name"] = "aaa"
        fdir = "K:/img_jiandan/"
        # # ssssssss
        # item["anthor"] = s
        # yield item

        with open(fdir+item["name"]+ ".jpg" ,"wb") as f:
            f.write(response.body)



