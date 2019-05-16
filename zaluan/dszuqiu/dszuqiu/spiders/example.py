# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,FormRequest


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['dszuqiu.com/']
    start_urls = []

    def start_requests(self):
        url = 'https://www.dszuqiu.com/login'
        '''
        zhanghu:18513606786
        password:jing1995
        captcha_input:24qax
        rememberMe:on
        bsubmit:1
        '''
        formdata = {
            "zhanghu": "18513606786",
            "password" :"jing1995",
            "rememberMe": "on",
            "bsubmit": "1"
        }

        header = {"user-angent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

        yield FormRequest(url,callback=self.parse,headers=header,formdata=formdata)

    def parse(self, response):
        print(response.body.decode())
