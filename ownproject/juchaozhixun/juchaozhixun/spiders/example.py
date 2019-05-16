# -*- coding: utf-8 -*-
'''
如何获得js发送的数据

'''
import scrapy
from scrapy import Request,FormRequest
import json


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['cninfo.com.cn/']
    start_urls = []

    def start_requests(self):

        header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9",
            'Connection':"keep-alive",
            "Content-Length":"230",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Host":"www.cninfo.com.cn",
            "Origin":"http://www.cninfo.com.cn",
            "Referer":"http://www.cninfo.com.cn/cninfo-new/disclosure/szse",
            "X-Requested-With":"XMLHttpRequest",
            "Cookie":"JSESSIONID=2E82711CA6402963F88EF495F3657F3D"
        }

        url = "http://www.cninfo.com.cn/cninfo-new/disclosure/szse_latest"
        # for i in range(1,100):
        formdata = {
            "stock":"",
            "searchkey":"",
            "plate":"",
            "category":"",
            "trade":"",
            "column":"szse",
            "columnTitle":"深市公告",
            "pageNum":"1",
            "pageSize":"30",
            "tabName":"latest",
            "sortName":"",
            "limit":"",
            "showTitle":"",
        }

        yield FormRequest(url,callback=self.parse,headers=header,formdata=formdata,dont_filter=True)

    def parse(self,response):
        print(response.body)
        #http://www.cninfo.com.cn/cninfo-new/disclosure/szse/bulletin_detail/true/1205453731?announceTime=2018-09-19%2011:40

