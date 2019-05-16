# -*- coding: utf-8 -*-
import scrapy
'''
翻页请求的响应得不到网页的url
'''


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['blog.csdn.net/']
    start_urls = ['https://blog.csdn.net/Uwr44UOuQcNsUQb60zk2/article/list']

    def parse(self, response):
        div_list = response.xpath("//div[@class='article-list']/div[@class='article-item-box csdn-tracking-statistics']")
        for div in div_list:
            url = div.xpath("./h4/a/@href").extract_first()
            print(url,"####")
            yield scrapy.Request(url,callback=self.parse_disease,dont_filter=True)

        # next_url = response.xpath("//div[@class='article-list']/div[@class='pagination-box']")


    def parse_disease(self,response):
        text = response.xpath("//div[@class='article__content']//text()").extract()
        print(text)