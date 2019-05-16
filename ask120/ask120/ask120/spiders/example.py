# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.120ask.com']
    start_urls = ['http://www.120ask.com/']

    def parse(self, response):
        item = {}

        div_list = response.xpath("//div[@class='left_sickbox']/div")
        for div in div_list:
            li_list = div.xpath("./div[2]/ul/li")
            for li in li_list:
                #large_assortment：大分类。
                large_assortment_raw = li.xpath("./b/a/text()").extract_first()
                large_assortment = str(large_assortment_raw)
                item["large_assortment"] = large_assortment
                a_list = li.xpath("./div/a")
                for a in a_list:
                    #小分类：subclassification
                    subclassification_raw = a.xpath("./text()").extract_first()
                    subclassification = str(subclassification_raw)
                    item["subclassification"] = subclassification

                    subclassification_url_raw = a.xpath("./@href").extract_first()
                    for i in range(201):
                        subclassification_url = subclassification_url_raw+"all/"+str(i)+"/"


                        yield scrapy.Request(subclassification_url,callback=self.parse_next,meta={"item":deepcopy(item)})

    def parse_next(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//ul[@class='clears h-ul3']/li")
        for li in li_list:
            url = li.xpath("./div[1]/p/a[@class='q-quename']/@href").extract_first()
            yield scrapy.Request(url, callback=self.parse_data, meta={"item": deepcopy(item)})

    def parse_data(self,response):
        item = response.meta["item"]
        list = []
        information_raw = response.xpath("//div[@class='b_askbox']/div[1]/div/span[1]/text()").extract_first()
        information = information_raw.split("|")
        gender_raw = information[0]
        gender = str(gender_raw)
        item["gender"] = gender

        age_raw = information[1]
        age = str(age_raw)
        item["age"] = age
        question_raw = response.xpath("//div[@class='b_askbox']/div[2]//text()").extract()
        question = str(question_raw).replace('\\t','').replace('\\r','').replace('\\n','').replace(" ","").replace("''","").replace(",,","")

        item["question"] = question
        # item["question"] = response.xpath("//p[@class='crazy_new']/text()").extract_first()
        answer_raw_list = response.xpath("//div[@class='b_anscont_cont']//p")   #/div[@class='b_answerbox t10']/div[@class='b_answerli']/div[2]/div[@class='b_anscontc'] 完整路径
        for answer_ra in answer_raw_list:
            answer2 = answer_ra.xpath("./text()").extract()
            answer_raw = list.append(answer2)
        answer = str(list)
        item["answer"] = answer.replace('\\t','').replace('\\r','').replace('\\n','').replace("\\xa0","").replace(" ","")

        # answer = str(answer_raw).replace('\\t','').replace('\\r','').replace('\\n','')
        # item["answer"] = answer
        yield item







