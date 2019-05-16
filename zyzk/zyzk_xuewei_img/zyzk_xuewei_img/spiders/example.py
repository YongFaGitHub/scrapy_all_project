# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.zk120.com/']
    start_urls = ['http://www.zk120.com/baike/w/%E7%A9%B4%E4%BD%8D%E9%A6%96%E9%A1%B5?nav=ys']

    def parse(self, response):
        item = {}
        a_list = response.xpath("//div[@id='mw-content-text']//table[2]//tr/td/a")

        for a in a_list:
            name = a.xpath("./text()").extract_first()
            item["name"] = name
            url_raw = a.xpath("./@href").extract_first()
            url = "https://www.zk120.com" + url_raw
            yield scrapy.Request(url, callback=self.parse_da, dont_filter=True,
                                 meta={"item": deepcopy(item)})

    def parse_da(self, response):
        item = response.meta["item"]
        img_a = response.xpath("//div[@class='thumb tright']//a[@class='image']/img")
        num = 1
        if len(img_a) < 1:
            with open("H:/空.txt", "a+", encoding="utf-8") as f:
                f.write(item["name"])
                f.write("\n")


        # if len(img_a) == 1:
        #     num = 0
        # for img in img_a:
        #     url = "https://www.zk120.com" + img.xpath("./@src").extract_first()
        #     item["num"] = num
        #     yield scrapy.Request(url, callback=self.parse_cun, dont_filter=True,meta={"item":deepcopy(item)})
        #     num += 1

    def parse_cun(self, response):
        item = response.meta["item"]
        if item["num"] == 0:
            item["num"] = ""
        with open("H:/xuewei/{}.jpg".format(item["name"] + str(item["num"])), "wb") as f:
            f.write(response.body)


