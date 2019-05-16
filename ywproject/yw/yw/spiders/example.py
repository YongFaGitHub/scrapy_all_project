# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.ewsos.com']
    start_urls = ['http://ask.ewsos.com/']

    def parse(self, response):
        item = {}
        li_list = response.xpath("//div[@class='menu']/ul[@id='mnav']/li[1]")
        for li in li_list:
            big_title_raw = li.xpath("./p/a/text()").extract_first()   #大分类
            big_title = str(big_title_raw)
            item["big_title"] = big_title
            li_list2 = li.xpath("./div/ul/li")
            for li2 in li_list2:
                url_raw = li2.xpath("./a/@href").extract_first() #http://ask.ewsos.com
                url = "http://ask.ewsos.com" + str(url_raw)
                small_title_raw = li2.xpath("./a/text()").extract_first() #中分类
                small_title = str(small_title_raw)
                item["small_title"] = small_title
                yield Request(url, callback=self.parse_one, meta={"item": deepcopy(item)},dont_filter=True)

    def parse_one(self,response):
        item = response.meta["item"]
        div_list = response.xpath("//div[@class='qatxt']/div[1]")
        for div in div_list:
            url_jin = div.xpath("./span[1]/a/@href").extract_first()  #进入详情的地址
            url = "http://ask.ewsos.com" + str(url_jin)
            question_title_raw = div.xpath("./span[1]/a/text()").extract_first()
            question_title = str(question_title_raw)
            item["question_title"] = question_title

            title_raw = div.xpath("./span[2]/a/text()").extract_first()
            title = str(title_raw)
            item["title"] = title

            yield Request(url, callback=self.parse_two, meta={"item": deepcopy(item)},dont_filter=True)


    def parse_two(self,response):
        list = []
        item = response.meta["item"]
        info_raw = response.xpath("//div[@class='wny']/p[1]/text()").extract()
        info = str(info_raw).replace("\\r\\n","").replace(" ","").replace("\\xa0","")
        item["info"] = info   #个人信息

        question_raw = response.xpath("//div[@class='wny']/p[2]/text()").extract()
        question = str(question_raw).replace("\\r\\n","").replace(" ","")
        item["question"] = question

        before_raw = response.xpath("//div[@class='wny']/p[3]/text()").extract_first()
        before = str(before_raw).replace("\xa0","")
        item["before"] = before

        help_raw = response.xpath("//div[@class='wny']/p[4]/text()").extract_first()
        help = str(help_raw)
        item["help"] =help

        answer_list = response.xpath("//div[@class='myhf']")
        for answers in answer_list:
            answer_raw = answers.xpath(".//div[@class='mone']/p/text()").extract_first()
            answerssss = str(answer_raw).replace("\r\n","").replace(" ","")
            list.append(answerssss)
        item["answer"] = str(list)
        yield item

