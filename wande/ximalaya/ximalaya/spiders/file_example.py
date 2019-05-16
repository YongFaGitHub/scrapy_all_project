# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,FormRequest
import requests

class ExampleSpider(scrapy.Spider):
    name = 'file_example'
    allowed_domains = ['ximalaya.com/']
    start_urls = ['http://www.ximalaya.com/']

    def start_requests(self):
        url = "http://www.ximalaya.com/passport/login"

        formdata = {
            "account":"18513606786",
            "password":"Lt5uVves2sGOePR7UV+BjyDX4zOyTufZMlT87F1eNsahWeHqxu8TY8jyPGPn7J3s1tNAMfwVFB4A71qzE9cSOj5TCEXpiWpwxM9J2hzTN2VHlnpE9/GGTEFczdVQw4QqlQYVFdbRIoXwYYao11QOPtaSZsVW8hoZ2e+KNl1wOVE="
        }

        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"}

        yield FormRequest(url,callback=self.parse,headers=header,formdata=formdata)
    def parse(self,response):
        print(response.body)












# import requests
# import json
# import sys
#
# class BaiduFanyi:
#     def __init__(self):
#         self.post_url = "https://www.ximalaya.com/passport/login"
#         self.post_data = {
#             "account":"18624064125",
#             "password":"hzs3Ld5MlgKzHdqzt9PX6MtD4SO04ndfTHnXJ0uWrQxl2z9GWDBPsekZKKxayEa9O6hf+d0OQh9FztghUg50Y9OBG3jg3eq4sA+cwQfG60xAYGCJyU5MwKWhxTmn1we1lk+zMm2d6Vh4xA2DnzXh6WAnz746e7tOLIdOrRAXMw=="
#         }
#         self.headers= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
#
#     def parse_url(self):
#         r = requests.post(self.post_url,data=self.post_data,headers=self.headers)
#         print(r.content.decode())
#
#     def get_result(self,html_str):#提取数据
#       pass
#
#     def run(self):
#         # 1.url,post_Data
#         # 2.发送请求，获取响应
#         html_str = self.parse_url()
#         # 3.提取数据
#         self.get_result(html_str)
#
# if __name__ == '__main__':
#
#     baidu_fanyi = BaiduFanyi()
#     baidu_fanyi.run()