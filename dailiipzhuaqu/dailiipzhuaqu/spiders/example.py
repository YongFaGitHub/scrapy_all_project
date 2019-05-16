# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['xicidaili.com/']
    start_urls = ['http://www.xicidaili.com/']

    def parse(self, response):
        tr_list = response.xpath("//table[@id='ip_list']//tr/th/a[text()='更多']")
        for tr in tr_list:
            url_raw = tr.xpath("./@href").extract_first()
            url = "http://www.xicidaili.com/" + url_raw

            print(url)
            yield Request(url,callback=self.parse_liebiao,dont_filter=True)

    def parse_liebiao(self,response):
        item = {}
        tr_list = response.xpath("//table[@id='ip_list']//tr[1]/following-sibling::*")
        for tr in tr_list[:-1]:
            ip_info = tr.xpath("./td[2]/text()").extract_first()
            port_info = tr.xpath("./td[3]/text()").extract_first()
            tcp_info = tr.xpath("./td[6]/text()").extract_first()
            # print(ip_info,"@@@@@@@@@@@@@@@@@@")

            info = tcp_info +"://" + ip_info +":" + port_info

            item["info"] = info
            # yield item


#  "http://120.26.110.59:8080"