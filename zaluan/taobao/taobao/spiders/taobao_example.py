# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,FormRequest

class TaobaoExampleSpider(scrapy.Spider):
    name = 'taobao_example'
    allowed_domains = ['taobao.com/']
    start_urls = []

    def start_requests(self):
        url = 'https://login.taobao.com/member/login.jhtml'

        formdata = {
            "TPL_username" : "18513606786",
            "TPL_password" : "jing19950110"
        }
        headers = {'Host':'login.taobao.com',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Referer' : 'https://login.taobao.com/member/login.jhtml',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection' : 'Keep-Alive'
            }

        yield FormRequest(url,callback=self.parse,headers=headers,formdata= formdata)

    def parse(self,response):
        print(response.body)



