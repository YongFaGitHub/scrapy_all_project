# -*- coding: utf-8 -*-
import scrapy
import json
from copy import deepcopy
from scrapy import Request



class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['ctrip.com/']
    start_urls = ['http://hotels.ctrip.com/Domestic/Tool/AjaxGetCitySuggestion.aspx']

    def parse(self, response):
        list = ["ABCD","EFGH","JKLM","NOPQRS","TUVWX","YZ"]
        content_raw = str(response.body.decode())
        content = content_raw.replace("if (!cQuery.jsonpResponse) { cQuery.jsonpResponse = {}; } cQuery.jsonpResponse.suggestion=",
                "").replace("热门","'热门'").replace("display", "'display'").replace("data","'data'").replace("group",
                "'group'").replace("ABCD", "'ABCD'").replace("EFGH","'EFGH'").replace("JKLM","'JKLM'").replace("NOPQRS",
                "'NOPQRS'").replace("TUVWX", "'TUVWX'").replace("YZ","'YZ'")
        # print(content)
        # content = "{" + content_raw + "}"
        city_list = eval(content)
        # print(city_list)
        for i in list:
            for city_dict in city_list["{}".format(i)]:
                # print(type(city_dict))
                data_raw = city_dict["data"]
                data_list = data_raw.split("|")
                print(data_list)

                # 得到了城市名称和城市的酒店的url
                url = "http://hotels.ctrip.com/hotel/" + data_list[0] + data_list[2]
                name = data_list[1]
