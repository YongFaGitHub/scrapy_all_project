# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest,Request


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['chunyuyisheng.com/']
    start_urls = []

    def start_requests(self):
        url = 'http://www.chunyuyisheng.com/ssl/api/weblogin/?next=/index'
        formdata = {
            "csrfmiddlewaretoken":"7709ee5b85db6200a31da523f300c1d3",
            "next":"/ssl/api/weblogin/?next=/index",
            "username":"18513606786",
            "password":"jing1995"
        }
        yield FormRequest(url,callback=self.parse,formdata=formdata)

    def parse(self, response):
        print(response.body.decode())


