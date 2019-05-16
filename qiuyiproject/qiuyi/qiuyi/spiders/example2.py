# -*- coding: utf-8 -*-
# 从全部问题中获取的问答
import scrapy
from scrapy.http import Request

class Example2Spider(scrapy.Spider):
    name = 'example2'
    allowed_domains = ['www.qiuyi.cn']
    start_urls = []

    def start_requests(self):
        # http: // ask.qiuyi.cn / questionlist / 2.html
        for i in range(1, 52832):
            url = 'http://ask.qiuyi.cn/questionlist/'+ str(i) + '.html'
            # print()

            yield Request(url, callback=self.parse_one,dont_filter=True)

    def parse_one(self,response):
        item = {}
        urls = response.xpath("//ul[@class='active']/li/span[1]/a[@target='_blank']/@href").extract()
        n = len(urls)
        # print(n)
        for i in range(0, n):
            all_urls = urls[i]
            # print(all_urls)

            yield Request(all_urls, callback=self.parse_two,dont_filter=True)

    def parse_two(self, response):
        items = {}
        text = response.xpath("//div[@class='left_text']//div[@class='wd_cont_s']//text()").extract()
        # print(text)
        big_class_raw = response.xpath("//p[@class='position']/a[3]/text()").extract_first()
        big_class = str(big_class_raw)
        items["big_class"] = big_class

        # 小分类
        small_class_raw = response.xpath("//p[@class='position']/a[4]/text()").extract_first()
        small_class = str(small_class_raw)
        items["small_class"] = small_class

        #病症的名称
        title_raw = response.xpath("//p[@class='position']/a[5]/text()").extract_first()
        title = str(title_raw)
        items["title"] = title

        # 问题的 头部
        ask_title_raw = response.xpath("//div[@class='ask_title']/h1/text()").extract_first()
        ask_title = str(ask_title_raw).replace("\n", "")
        items["ask_title"] = ask_title

        # 病症描述
        disease_Description_raw = response.xpath("//div[@class='wd_cont_s']/p[1]/text()").extract_first()
        disease_Description = str(disease_Description_raw).replace("\n", "")
        items["disease_Description"] = disease_Description

        # 医师回答（包括多条，每条使用[] 分隔）
        list = []
        answer_raw = response.xpath("//div[@class='wd_box_2 bor answer']//div[@class='wd_cont_s']/p[1]")
        for answer_ra in answer_raw:
            list.append("[" + str(answer_ra.xpath("./text()").extract_first().replace("\\n", "") + "]"))
        items["answer"] = str(list)
        print(items)
        # yield items

