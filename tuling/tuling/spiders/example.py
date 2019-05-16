# # -*- coding: utf-8 -*-
# import scrapy
# from scrapy import FormRequest
#
#
# class ExampleSpider(scrapy.Spider):
#     name = 'jieba_try'
#     allowed_domains = ['open.turingapi.com']
#     start_urls = []
#
#     def start_requests(self):
#         header = {
#             "Accept": "application / json, text / plain, * / *",
#             "User-Agent":"Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11 Pluskt Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044306 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x26070336) NetType/WIFI Language/zh_CN Process/tools",
#             "Accept - Encoding": "gzip, deflate",
#             "Accept-Language": "zh-CN,en-US;q=0.8",
#             "X-Requested-With": "com.tencent.mm",
#             "Content-Length": "106",
#             "Content-Type": "application/json;charset=UTF-8",
#             "Origin": "http://uzoo.cn",
#             "Connection": "keep-alive",
#             "Host": "open.turingapi.com"
#         }
#         formdata ={
#             "info":"在吗",
#             "Key":"43da57df-c7a1-4cdd-8904-93556d7d566f"
# }
#         url = 'http://open.turingapi.com/v1/openapi'
#         yield FormRequest(url,formdata=formdata,callback=self.parse)
#
#
#     def parse(self, response):
#         print("$"*100)
#         print(response.body.decode())
#         print("$"*100)


# -*- coding: utf-8 -*-

import json
import sys, locale
import requests

if __name__ == '__main__':
    Key = '2cb29e5c4ad2430080bbb316f05e6cdb'
    url = 'http://www.tuling123.com/openapi/api'
    while True:
        info = input('input:')

        info.encode('utf-8')

        query = {'key': Key, 'info': info}
        headers = {'Content-type': 'text/html', 'charset': 'utf-8'}

        r = requests.get(url, params=query, headers=headers)
        res = r.text
        print(json.loads(res).get('text').replace('<br>', '\n') + '\n')