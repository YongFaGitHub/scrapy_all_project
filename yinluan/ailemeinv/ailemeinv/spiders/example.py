# -*- coding: utf-8 -*-
import scrapy
from scrapy import  Request
from copy import deepcopy
import os

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['ilemiss.com/']
    start_urls = ['http://www.ilemiss.com/']

    def parse(self, response):
        item = {}
        # print(response.body.decode())
        li_list = response.xpath("//div[@class='nav']/ul/li[@class='nli']")
        for li in li_list:
            # 大类
            big_class = li.xpath("./a/text()").extract_first()
            item["big_name"] = big_class

            # 大类地址
            big_url = li.xpath("./a/@href").extract_first()
            # print(big_url)
            item["big_url"] = big_url
            yield Request(big_url,callback=self.parse_big_class,dont_filter=True,
                          meta={"item": deepcopy(item)})

    def parse_big_class(self,response):
        item = response.meta["item"]
        # print(response.body.decode())
        li_list = response.xpath("//div[@class='imainbox']/ul/li")
        for li in li_list:
            title_url = li.xpath("./div[@class='imbtxt']/p/a/@href").extract_first()
            title = li.xpath("./div[@class='imbtxt']/p/a/text()").extract_first()
            item["title"] = title

            yield Request(title_url,callback=self.parse_disease,dont_filter=True,
                          meta={"item": deepcopy(item)})

        # 图片集的下一页
        next_url = response.xpath("//div[@class='wlistpages']//span[text()='下一页']/../@href").extract_first()
        if next_url is  not None:
            # print(next_url)
            yield Request(next_url,callback=self.parse_big_class,dont_filter=True,
                          meta={"item": deepcopy(item)})

    # 进入图片集的内部
    def parse_disease(self, response):
        item = response.meta["item"]
        img_name = response.xpath("//div[@class='contentpic']/img/@alt").extract_first()
        item["img_name"] = img_name

        img_url = response.xpath("//div[@class='contentpic']/img/@src").extract_first()
        yield Request(img_url,callback=self.parse_img,dont_filter=True,
                      meta={"item": deepcopy(item)})

        next_img_url_Raw = response.xpath("//div[@class='wlinkpages']//a[text()='下一页']/@href").extract_first()
        if next_img_url_Raw is not None:
            next_img_url = item["big_url"] + next_img_url_Raw
            yield Request(next_img_url, callback=self.parse_disease,dont_filter=True,
                          meta={"item": deepcopy(item)})

    def parse_img(self, response):
        item = response.meta["item"]

        try: os.mkdir("I:图片/aile/{}".format(item["big_name"]))
        except: pass

        try: os.mkdir("I:/图片/aile/{}/{}".format(item["big_name"], item["title"]))
        except:pass

        with open("I:/图片/aile/{}/{}/{}.jpg".format(item["big_name"], item["title"], item["img_name"]), "wb") as f:
            f.write(response.body)
        print(item["img_name"])
