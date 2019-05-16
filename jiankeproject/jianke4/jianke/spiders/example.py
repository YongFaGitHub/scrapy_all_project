# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re
from copy import deepcopy
#//a/following-sibling::*
class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.jianke.com']
    start_urls = ['http://www.jianke.com/ask/']

    def parse(self, response):
        url_list = []
        div_list = response.xpath("//div[@class='mc']/div[6]") #/following-sibling::*    2 3 4 5 6 7  11 12 13
        for div1 in div_list:
            a_list = div1.xpath("./span/i/s/a")
            for a in a_list:
                url_raw1 = a.xpath("./@href").extract_first()
                url1 = "http://www.jianke.com" + url_raw1
                url_list.append(url1)

        for div2 in div_list:
            dd_list = div2.xpath("./div/dl/dd")
            for dd in dd_list:
                url2_raw = dd.xpath("./a/@href").extract_first()
                url2 =  "http://www.jianke.com" + url2_raw
                url_list.append(url2)
        # print(len(url_list))# 所有的中等标签
        for url  in url_list:
            all_url_raw = re.findall('(.*-)\w+',url)
            for i in range(20000):
                all_url = all_url_raw[0]+str(1)
                yield Request(url, callback=self.parse_one, dont_filter=True)


    def parse_one(self,response):
        li_list = response.xpath("//ul[@class='alltw_box']/li")
        for li in li_list:
            url_raw = li.xpath("./dl/dd[@class='dd1']/span/a/@href").extract_first()
            url = "http://www.jianke.com" + url_raw
            yield Request(url, callback=self.parse_two, dont_filter=True)



    def parse_two(self,response):
        item = {}
        list = [] #title列表
        list2 = []#回答列表
        a_list = response.xpath("//h5/a[text()='所有问题']/following-sibling::*")
        for a in a_list:
            title_list = a.xpath("./text()").extract_first()
            list.append(title_list)

        item["title"] = str(list)

        question_title_raw = response.xpath("//div[@class='why']/h1/text()").extract_first()
        question_title = str(question_title_raw)
        item["question_title"] = question_title

        gender_age_list  = response.xpath("//p[@class='name_age f12']/text()").extract()
        gender_raw = gender_age_list[0]
        gender = str(gender_raw).replace("\r\n","").replace(" ","")
        item["gender"] = gender


        age_raw = gender_age_list[1]
        age = str(age_raw).replace("\r\n", "").replace(" ", "")
        item["age"] = age

        question_raw = response.xpath("//p[@class='pd_txt']/text()").extract_first()
        question = str(question_raw)
        item["question"] = question

        answer_list = response.xpath("//div[@class='anwsernew fl']")
        for answer in answer_list:
            answer_raw = answer.xpath("./div[@class='an_cont']/dl/dt//text()").extract()
            list2.append(answer_raw)
        item["answer"] = str(list2).replace("'","")

        yield item








#      （*-*-）






