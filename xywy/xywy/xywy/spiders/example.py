# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.http import Request
import selectors
from xywy.items import AskdoctorItem

class ExampleSpider(scrapy.Spider):
    name = 'gaoxueya'
    allowed_domains = ['club.xywy.com']
    start_urls = []

    def start_requests(self):
        for i in range(1,5272):
            url = 'http://club.xywy.com/keshi/2017-11-08/'+str(i)+'.html'
            yield  Request(url,callback=self.parse_one)

    def parse_one(self,response):
        url_list = []#创建一个大的list存储所有的url
        urls = response.xpath("//em//a[@target=\'_blank\']/@href").extract()
        n = len(urls)
        print(n)
        for i in range(0,n):
            all_urls = urls[i]
            print(all_urls)
            yield Request(all_urls, callback=self.parse_second)


    def parse_second(self, response):
        items = AskdoctorItem()
        titleClass = response.xpath('//div//p//a[@target=\'_blank\']/text()').extract()
        title = titleClass[3]
        question_raw = response.xpath('//div[@id=\'qdetailc\']/text()').extract()
        question = str(question_raw).replace('\\t','').replace('\\r','').replace('\\n','')
        #print(question)
        items['question'] = question

        items['titleClass'] = title

        answer_raw = response.xpath('//div[@class=\'pt15 f14 graydeep  pl20 pr20\']/text()').extract()
        answer = str(answer_raw).replace('\\t','').replace('\\r','').replace('\\n','')
        items['answer'] = answer
        #print(answer)

        gender_raw = response.xpath('//div[@class =\'User_askcon clearfix pr\'] / div[3] / span[5]').extract()
        gender = str(gender_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '')

        items['gender'] = gender

        age_raw = response.xpath('//div[@class=\'User_askcon clearfix pr\']/div[3]/span[3]').extract()
        age = str(age_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '')

        items['age'] = age
        yield items
        # .// div[ @
        #
        # class ='User_askcon clearfix pr'] / div[3] / span[5]  年龄

        # .//div[@class='User_askcon clearfix pr']/div[3]/span[3] 性别































