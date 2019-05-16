# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import json


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['ximalaya.com']
    start_urls = ['http://www.ximalaya.com/category/']

    def parse(self, response):
        # print(response.body.decode())
        list = []
        a_list = response.xpath("//div[@class='hW1c category_hotword']//div[@class='hW1c list']/a")
        for a in a_list:
            href_raw = a.xpath("./@href").extract_first()
            href = "https://www.ximalaya.com" + href_raw
            list.append(href)

        a2_list = response.xpath("//div[@class='hW1c plates']/div/div[@class='hW1c body']//div[@class='hW1c list']/a")
        for a2 in a2_list:
            href2_raw = a2.xpath("./@href").extract_first()
            href2 = "https://www.ximalaya.com" + href2_raw
            list.append(href2)

        for li in list:
            yield Request(li,callback=self.parse_url_all,dont_filter=True)

    def parse_url_all(self,response):
        list = []
        a_list = response.xpath("//div[@class='category-filter-body-switch']/div[1]//div[@class='category-filter-value-list']/a")
        if a_list is not    None:
            for a in a_list:
                href_raw = a.xpath("./@href").extract_first()
                href = "https://www.ximalaya.com" + href_raw
                list.append(href)

        list2 = set(list)

        for li in list2:
            yield Request(li ,callback=self.parse_mianfei,dont_filter=True)

    #获取到免费音频的地址
    def parse_mianfei(self,response):
        url_mianfei_raw = response.xpath("//div[@class='category-filter-value-list']/a[text()='免费']/@href").extract_first()
        for i in range(1,35):
            if url_mianfei_raw is not   None:
                url_mianfei = "https://www.ximalaya.com"  + url_mianfei_raw +"p{}".format(i)

                yield Request(url_mianfei,callback=self.parse_disease,dont_filter=True)


    #对音频各种进行获取
    def parse_disease(self,response):
        li_list = response.xpath("//div[@class='content']/ul/li/div")
        for i in range(1,35):
            for li in li_list:
                disease_url_raw = li.xpath("./a[1]/@href").extract_first()
                disease_url = "https://www.ximalaya.com" + disease_url_raw +"p{}".format(i)


                # title = li.xpath("./a[1]/@title").extract_first()

                yield Request(disease_url,callback=self.disease_liebiao,dont_filter=True)




    def disease_liebiao(self,response):
        li_list = response.xpath("//ul[@class='dOi2']/li")
        for li in li_list:
            title_raw = li.xpath("./div[2]/a/@href").extract_first()
            title_list = title_raw.split("/")

            num = title_list[-1]

            url = "https://www.ximalaya.com/revision/play/tracks?trackIds={}".format(num)
            yield Request(url,callback=self.disease,dont_filter=True)

    def disease(self,response):
        json_r = json.loads(response.body)
        print(json_r)







            # '''https://www.ximalaya.com/revision/play/tracks?trackIds=11198220
            #   https://www.ximalaya.com/revision/play/tracks?trackIds=71745418'''











