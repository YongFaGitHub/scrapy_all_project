# -*- coding: utf-8 -*-
import scrapy


class JkSpider(scrapy.Spider):
    name = 'jk'
    allowed_domains = ['jbk.39.net/']
    start_urls = ['http://jbk.39.net/']

    def parse(self, response):
        items = {}
        title_list = response.xpath("//div[@class='mapList']/dl")
        print("$$$$$$$")

        for title in title_list:
            li_list = title .xpath("./dd/div[1]/ul/li")
            for li in li_list:
                a_list = li.xpath("./span[@class='right']/a")
                print(a_list)
                for a in a_list:
                    title_raw= a.xpath("./text()").extract_first()
                    title_ra = str(title_raw)
                    items['title'] = title_ra
                    print(items)
