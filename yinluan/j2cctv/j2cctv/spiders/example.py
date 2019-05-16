# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from scrapy import Request
import re
import os

'''
主页已经修改，需要重新调整xpath
'''


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['j2cctv.com/']
    start_urls = ['http://www.j2cctv.com/']

    def parse(self, response):
        item = {}
        # print(response.body.decode())
        li_list = response.xpath('//div[@class="wrap mt20 nav"]/ul[1]/li | //div[@class="wrap mt20 nav"]/ul[2]/li')

        for li in li_list:
            print("%%%%%%%%%%%%%%%%%%%%%%%%%")
            class_name = li.xpath("./a/text()").extract_first()
            item["class_name"] = class_name
            url = "http://www.j2cctv.com" + li.xpath("./a/@href").extract_first()
            # url = "https://v-pptv.com/share/b628386c9b92481fab68fbf284bd6a64"

            yield Request(url, callback=self.parse_class_name, dont_filter=True,
                          meta={"item": deepcopy(item)})

    def parse_class_name(self, response):
        item = response.meta["item"]
        # print(response.body.decode())
        li_list = response.xpath("//div[@class='box movie_list']//ul/li")
        for li in li_list:
            title_raw = li.xpath("./a/@title").extract()
            title = str(title_raw).replace("['", "").replace("']", "").replace(" ", "_")
            item["title"] = title

            title_url = "http://www.j2cctv.com" + li.xpath("./a/@href").extract_first()
            yield Request(title_url, callback=self.parse_disease, dont_filter=True,
                          meta={"item": deepcopy(item)})

    def parse_disease(self, response):
        item = response.meta["item"]
        # print("*"*200)
        url_raw = str(response.xpath("//script/text()").extract())
        if "mac_server='0$$$0'" in url_raw:
            url_raw_raw = re.findall("mac_url=unescape\('(.*?)'\)", url_raw)[0]
            url_raw_raw_raw = (url_raw_raw.split("http"))[-1]
            url = "http" + url_raw_raw_raw.replace("%3A", ":").replace("%2F", "/")

            yield Request(url, callback=self.parse_list, dont_filter=True,
                          meta={"item": deepcopy(item)})
    '''
    m3u8格式的视频如何下载:要如何分段下载
    '''

    def parse_list(self, response):
        item = response.meta["item"]

        title = response.xpath("//title/text()").extract_first()
        item["title"] = title

        url_f = (re.findall('var main = "(.*?)/index.m3u8', response.body.decode()))[0]
        item["url_f"] = url_f

        url_raw = (re.findall('var main = "(.*?)";', response.body.decode()))[0]
        url = "https://v-pptv.com" + url_raw
        # print(url)

        yield Request(url, callback=self.parse_li, dont_filter=True,
                      meta={"item": deepcopy(item)})

    def parse_li(self,response):
        item = response.meta["item"]

        url_last = (re.findall("(.*?)m3u8", response.body.decode()))[0]
        # print(url_last)

        url = "https://v-pptv.com" + item["url_f"] + "/" + url_last + "m3u8"
        ts_url =url.replace("index.m3u8", "")
        item["ts"] = ts_url
        yield Request(url, callback=self.parse_lili, dont_filter=True,
                      meta={"item": deepcopy(item)})

    def parse_lili(self, response):
        item = response.meta["item"]
        # print(response.body.decode())
        # print("*("*100)
        moive_list_url = re.findall("(.*?)\.ts", response.body.decode())
        for moive_list in moive_list_url:
            item["name"] = moive_list

            url = item["ts"] + moive_list + ".ts"
            yield Request(url,callback=self.parse_fin,  dont_filter=True,
                          meta={"item": deepcopy(item)})

    def parse_fin(self,response):
        item = response.meta["item"]

        try:
            os.mkdir("I:/j2/{}".format(item["title"]))
        except:
            pass

        with open("I:/j2/{}.ts".format(item["title"]), "wb+") as f:
            f.write(response.body)
        print("%s:%s已保存" % (item["title"]))
