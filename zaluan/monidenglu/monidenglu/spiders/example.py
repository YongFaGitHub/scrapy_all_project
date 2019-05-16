# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,FormRequest

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['renren.com/']
    start_urls = ['http://www.renren.com/']


    def start_requests(self):
        url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018741512396"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"}
        formdata = {
            "email": "18513606786",
            "origURL": "http://www.renren.com/home",
            "password": "5871ce5da1bacaae5e586ba686bc50d4a41be6a3c2a19f573b088f3cecd52cca",
            "rkey": "56c61d35789ce0326162a224b59725f3"
        }
        yield FormRequest(url,headers=header,formdata=formdata,callback=self.parse)


    def parse(self, response):
        yield Request("http://www.renren.com/home",callback=self.disease,dont_filter=True)

    def disease(self,response):
        text = response.xpath("//a[@class='hd-name']/@title").extract_first()
        print(text,"#@"*20)



# import scrapy
#
# class LoginSpider(scrapy.Spider):
#     name = 'jieba_try.com'
#     start_urls = []
#
#
#     def start_requests(self):
#         url = "http://www.example.com/users/login.php"
#
#     def parse(self, response):
#         return scrapy.FormRequest.from_response(
#             response,
#             formdata={'username': 'john', 'password': 'secret'},
#             callback=self.after_login
#         )
#
#     def after_login(self, response):
#         # check login succeed before going on
#         if "authentication failed" in response.body:
#             self.log("Login failed", level=log.ERROR)
#             return