# -*- coding: utf-8 -*-
import scrapy
'''
遇到问题：访问页面请求响应为400，怀疑为cookies的问题
'''

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.xueqiu.com']
    start_urls = []

    def start_requests(self):
        headers = {
            "Cookie":"aliyungf_tc=AQAAAIV4bnP7mg0AcjvMb1fYchsk4k33; xq_a_token=9c75d6bfbd0112c72b385fd95305e36563da53fb; xq_a_token.sig=-6-bcHntQlhRjsyrvsY2IGwh-B4; xq_r_token=9ad364aac7522791166c59720025e1f8f11bf9eb; xq_r_token.sig=usx1_hrblByw-9h0cXk1yLIUlL4; u=321537407638023; Hm_lvt_1db88642e346389874251b5a1eded6e3=1537407638; _ga=GA1.2.35797704.1537407638; _gid=GA1.2.1461538692.1537407638; device_id=9ed49fd4956a642af298db943f7980a1; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1537409770; _gat_gtag_UA_16079156_4=1"
        }
        url = "https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=-1"

        yield scrapy.Request(url,headers=headers,callback=self.parse,dont_filter=True)



    def parse(self, response):
        print(response.body.decode())

