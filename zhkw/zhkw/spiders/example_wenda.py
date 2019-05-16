# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy




class ExampleWendaSpider(scrapy.Spider):
    name = 'example_wenda'
    allowed_domains = ['cnkang.com/']
    start_urls = ['http://www.cnkang.com/ask/question/list_1_0_1.html']

    def parse(self, response):
        item  ={}
        a_list = response.xpath("//dl[@class='iask11_con']/dd/ul/a")
        for a in a_list:
            url_raw = a.xpath("./@href").extract_first()
            url = "http://www.cnkang.com" + url_raw

            item["big_class"] = a.xpath("./text()").extract_first()



            yield Request(url,callback=self.parse_class,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_class(self,response):
        item = response.meta["item"]
        a_list = response.xpath("//dl[@class='iask11_con']/dd/ol/a[1]/following-sibling::*")
        for a in a_list:
            url_raw = a.xpath("./@href").extract_first()
            url = "http://www.cnkang.com" + url_raw

            item["small_class"] = a.xpath("./text()").extract_first()


            yield Request(url,callback=self.parse_list,dont_filter=True,meta={"item":deepcopy(item)})


    def parse_list(self,response):
        item = response.meta["item"]
        a_list  = response.xpath("//div[@class='iask12_con']/dl/dt/a")
        for a in a_list:
            url_raw = a.xpath("./@href").extract_first()
            url = "http://www.cnkang.com" + url_raw

            item["title"] = a.xpath("./text()").extract_first()

            yield Request(url,callback=self.parse_disease,dont_filter=True,meta={"item":deepcopy(item)})

        next_url_raw = response.xpath("//div[@class='pageStyle']/a[text()='下一页']/@href").extract_first()
        if next_url_raw is not None:
            next_url = "http://www.cnkang.com"  + next_url_raw
            yield Request(next_url,callback=self.parse_list,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_disease(self,response):
        item = response.meta["item"]
        question_raw = response.xpath("//div[@class='iask13 iask13_q']//ul[@class='iask13_con']/text()").extract()
        question = str(question_raw).replace("['","").replace("']","").replace(" ","").replace("\\r","").replace("\\n",
        "").replace("\\t","").replace("','','","。").replace("','","")
        item["question"] = question


        answer_raw = response.xpath("//div[@class='iask13 iask13_a']//ul[@class='iask13_con']/text()").extract()
        answer = str(answer_raw).replace("['","").replace("']","").replace(" ","").replace("\\r","").replace("\\n",
        "").replace("\\t","").replace("','','","。").replace("','","")
        item["answer"] = answer

        if len(answer) > 5:
            yield item
            # print(item)
















