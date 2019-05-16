# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['gamehelper.gm825.com']
    start_urls = []

    def start_requests(self):
        headers = {'Accept-Charset': 'UTF-8',
                   'Accept-Encoding': 'gzip,deflate',
                   'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 5 MIUI/V8.1.6.0.MAACNDI)',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Content-type': 'application/x-www-form-urlencoded',
                   'Connection': 'Keep-Alive',
                   'Host': 'gamehelper.gm825.com'}
        url = 'http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8'

        yield Request(url,callback=self.parse,headers=headers)

    def parse(self, response):
        item={}
        # print(response.body.decode("unicode_escape"))
        r = json.loads(response.body)
        list = r["list"]
        for  i in list:
            item["name"] = i["name"]
            url = i["cover"]
            yield Request(url,callback=self.parse_img,meta={"item":deepcopy(item)},dont_filter=True)

    def parse_img(self,response):
        item = response.meta["item"]

        with open("H:/wangzhe_img/{}.png".format(item["name"]),"wb") as f:
            f.write(response.body)
            print(item["name"])



