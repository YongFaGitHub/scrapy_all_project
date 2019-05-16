# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import re

'''
拿到所有的ts视频的响应 但是内容有加密
'''


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['52se34.com']
    start_urls = ['http://52se34.com']

    def parse(self, response):
        item = {}
        li_list = response.xpath("//ul[@class='top-nav']/li[1]/following-sibling::*")
        for li in li_list:
            # 分类名称
            text = li.xpath("./a/text()").extract_first()
            item["class_name"] = text
            url = "http://52se34.com" + li.xpath("./a/@href").extract_first()

            yield Request(url, callback=self.parse_list, dont_filter=True,
                          meta={"item": deepcopy(item)})

    def parse_list(self, response):
        item = response.meta["item"]
        # print(response.body.decode())
        #
        # li_list = response.xpath("//div[@class='index-area clearfix']/ul/li")
        # for li in li_list:
        #     text = li.xpath("./a/@title").extract_first()
        #     item["title"] = text
        #     url = "http://52se34.com" + li.xpath("./a/@href").extract_first()
        #     # print(url)
        #
        #     yield Request(url, callback=self.parse_disease, dont_filter=True,
        #                   meta={"item": deepcopy(item)})
        #
        # next_url_raw = response.xpath("//div[@class='page']/a[text()='下一页']/@href").extract_first()
        # if next_url_raw is not None:
        #     next_url = "http://52se34.com" + next_url_raw
        #     yield Request(next_url, callback=self.parse_list, dont_filter=True,
        #                   meta={"item": deepcopy(item)})

        yield Request("http://52se34.com/?m=vod-detail-id-94359.html", callback=self.parse_disease, dont_filter=True,
                      meta={"item": deepcopy(item)})

    def parse_disease(self, response):
        item = response.meta["item"]
        url = "http://52se34.com" + response.xpath(
            "//div[@class='show_player_gogo']/ul/li/a[contains(text(),'立即播放')]/@href").extract_first()

        yield Request(url, callback=self.parse_m3u8_last, dont_filter=True,
                      meta={"item": deepcopy(item)})

    def parse_m3u8_last(self, response):
        item = response.meta["item"]
        url_raw = (re.findall("mac_url=unescape\('(.*?)'\)", response.body.decode(), re.S))[0]
        url = str(url_raw).replace("%3A", ":").replace("%2F", "/")
        item["ts_url"] = url
        # print(item["ts_url"])

        yield Request(url, callback=self.parse_m3u8_list, dont_filter=True,
                      meta={"item": deepcopy(item)})

    def parse_m3u8_list(self, response):
        item = response.meta["item"]

        url_last = (re.findall("(.*?m3u8)", response.body.decode()))[0]

        item["ts_url"] = (item["ts_url"]).replace("index.m3u8", url_last)

        yield Request(item["ts_url"], callback=self.parse_ts_list, dont_filter=True,
                      meta={"item": deepcopy(item)})

    def parse_ts_list(self, response):
        item = response.meta["item"]

        ts_list = re.findall("(.*?ts)", response.body.decode())
        for ts in ts_list:
            item["ts_url"] = (item["ts_url"]).replace("index.m3u8", ts)
            item["ts_name"] = ts.replace(".","")

            yield Request(item["ts_url"], callback=self.parse_fin, dont_filter=True,
                          meta={"item": deepcopy(item)})

    def parse_fin(self, response):
        item = response.meta["item"]

        with open("H://daxiangjiao/{}.ts".format(item["ts_name"]), "wb") as f:
            f.write(response.body)


