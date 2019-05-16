# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['club.xywy.com']
    start_urls = ['http://jib.xywy.com/']

    def parse(self, response):

        item = {}
        li_list = response.xpath("//ul[@class='illness-list clearfix']/li")

        for li in li_list:

            div_list = li.xpath("./div/div/div")
            for div in div_list:

                samll_list = div.xpath("./ul/li")
                for small in samll_list:
                    url_raw = small.xpath("./a/@href").extract_first()

                    small_title_raw = small.xpath("./a/text()").extract_first()
                    small_title = str(small_title_raw)
                    item["small_title"] = small_title
                    if len(url_raw) < 26:
                        url = "http://jib.xywy.com" + url_raw

                        yield Request(url,callback=self.parse_one,meta={"item": deepcopy(item)},dont_filter=True)


    def parse_one(self,response):
        item = response.meta["item"]
        url_raw = response.xpath("//div[@class='jib-navbar fl bor pr']//a[text()='检查']/@href").extract_first()
        url = "http://jib.xywy.com" + url_raw
        # with open("H:/pycharmproject/deal_data/xywydata/jiancha2/url.csv","a+",encoding="utf-8") as f:
        #     f.write(url)
        #     f.write("\n")

        yield Request(url,callback=self.parse_two,meta={"item": deepcopy(item)},dont_filter=True)

    def parse_two(self,response):

        item = response.meta["item"]
        ul_list = response.xpath("//div[@class='more-zk pr']//ul[1]/following-sibling::*")

        for ul in ul_list:
            #价格
            info_two_raw = ul.xpath("./li[2]//text()").extract()
            info_two = str(info_two_raw).replace("[","").replace("]","").replace(' ',"").replace("'","")
            item["info_two"] = info_two
            info_one_url = ul.xpath("./li[@class='check-item']/a/@href").extract_first()
            if info_one_url is not None:
            # print(info_one_url)
                yield Request(info_one_url,callback=self.parse_three,meta={"item": deepcopy(item)},dont_filter=True)

    def parse_three(self,response):
        item = response.meta["item"]
        info_raw  = response.xpath("//div[@class='clearfix']/strong/text()").extract_first()
        with open("H:/pycharmproject/deal_data/xywydata/jiancha2/{}.csv".format(item["small_title"]),"a+",encoding="utf-8") as f:
            f.write(info_raw)
            f.write(",")
            f.write(item["info_two"])
            f.write("\n")











