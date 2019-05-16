# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['jbk.39.net/']
    start_urls = ['http://ask.39.net/browse/all_322.html']

    def parse(self, response):
        #获取进入的大分类页面中的小分类的地址
        ddlist = response.xpath("//dl[@class='cj']/dd")
        for dd in ddlist:
            url_raw = dd.xpath("./a/@href").extract_first()
            url = "http://ask.39.net" + url_raw

            yield Request(url,callback=self.parse_two,dont_filter=True)
        #获取每个打分类的地址
        a_list = response.xpath("//ul[@class='tag-all-menu']/li/a")
        for a in a_list:
            big_class_url_raw = a.xpath("./@href").extract_first()
            big_class_url = "http://ask.39.net" + big_class_url_raw
            yield Request(big_class_url,callback=self.parse,dont_filter=True)


    def parse_two(self,response):
        #进入每个小分类的地址
        url_list = response.xpath("//a[text()='查看全部问题']/@href").extract_first()
        url = "http://ask.39.net" + url_list
        yield Request(url ,callback=self.parse_three,dont_filter=True)

    def parse_three(self,response):
        #进入列表页
        item = {}
        #小分类的名称
        title_raw = response.xpath("//div[@class='post-screen']/div/text()").extract_first()
        title = str(title_raw).replace("'","")
        item["title"] = title

        li_list = response.xpath("//div[@class='question-box']/ul/li")
        for li in li_list:
            url_raw = li.xpath("./div[@class='question-ask']/p/a/@href").extract_first()
            url = "http://ask.39.net" + url_raw
            yield  Request(url,callback=self.parse_four,meta={"item": deepcopy(item)},dont_filter=True)

        next_url_raw = response.xpath("//a[text()='下一页']/@href").extract_first()
        next_url =  "http://ask.39.net" + next_url_raw
        yield Request(next_url,callback=self.parse_three,dont_filter=True)


    def parse_four(self,response):
        item = response.meta["item"]
        question_body = response.xpath("//div[@class='ask_cont']")
        title2_raw = question_body.xpath("./p[@class='ask_tit']/text()").extract()
        title2 = str(title2_raw).replace("\\n","").replace(" ","").replace("[","").replace("]","").replace("'","")
        item["title2"] = title2

        info_q = question_body.xpath("./p[@class='mation']")
        gender_raw = info_q.xpath("./span[1]/text()").extract_first()
        gender = str(gender_raw).replace("'","")
        item["gender"] = gender

        age_raw = info_q.xpath("./span[2]/text()").extract_first()
        age = str(age_raw).replace("\n","").replace(" ","").replace("'","")
        item["age"] = age

        time_raw = info_q.xpath("./span[3]/text()").extract_first()
        time = str(time_raw)
        item["time"] = time

        question_raw = response.xpath("//p[@class='txt_ms']/text()").extract()
        question = str(question_raw).replace("\\t","").replace("\\n","").replace(" ","").replace("['","").replace("']","").replace("','","").replace("'","")
        item["question"] = question


        div_list = response.xpath("//div[@class='selected']/div")
        list2 = []
        for div in div_list:
            answer_raw = div.xpath("./p[@class='sele_txt']/text()").extract()
            answer = str(answer_raw).replace("\u3000","").replace("',","").replace("'","")
            # print(answer)
            list2.append(answer)

        ans = str(list2)
        item["answer"] = ans

        print(item)







