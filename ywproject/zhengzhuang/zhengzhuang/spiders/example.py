# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from scrapy import Request

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['jibing.ewsos.com/']
    start_urls = ['http://jibing.ewsos.com/zhengzhuang/buwei']

    def parse(self, response):
        li_ist  = response.xpath("//ul[@id='menu']/li")
        item ={}
        for li in li_ist:
            url_liebiao = li.xpath("./a/@href").extract_first()

            body = li.xpath("./a/text()").extract_first()
            item["body"] = body
            yield Request(url_liebiao,callback=self.parse_liebiao,meta={"item":deepcopy(item)},dont_filter=True)

    def parse_liebiao(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@class='leftPinBox1']/ul/li")
        for li in li_list:
            url_disease_raw = li.xpath("./a/@href").extract_first()  #症状的地址
            title = li.xpath("./a/text()").extract_first()
            item["title"] = title

            url_disease = url_disease_raw.replace("jieshao","{}")  #每种症状的基本地址
            item["url"] = url_disease

            yield Request(url_disease_raw,callback=self.parse_disease,meta={"item":deepcopy(item)},dont_filter=True)

        #下一页
        next_url_raw = response.xpath("//div[@class='art_page']/span/a[text()='下一页']/@href").extract_first()
        if next_url_raw is not None:
            next_url = "http://jibing.ewsos.com" + next_url_raw
            yield Request(next_url ,callback=self.parse_liebiao,dont_filter=True,meta={"item":deepcopy(item)})


    def parse_disease(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='showsmalorall']/div[@id='showAll']/p")
        p_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            p_info = str(p_info_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
            "").replace("\\u3000","").replace("\\xa0","").replace("\\n","").replace("\\t","").replace("\\r",
            "").replace('"target=_blank>',"").replace("','","")

            if len(p_info) >1:
                p_s = p_s + p_info +"\n"

        item["disease"] = p_s[:-1]
        # print(p_s)
        url = (item["url"]).format("bingyin") #病因地址

        yield Request(url,callback=self.parse_bingyin,meta={"item":deepcopy(item)},dont_filter=True)


    def parse_bingyin(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='leftArticle2']/p")
        p_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            p_info = str(p_info_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
            "").replace("\\u3000","").replace("\\xa0","").replace("\\n","").replace("\\t","").replace("\\r",
            "").replace("','","").replace('"target=_blank>',"")

            if len(p_info) >1:
                p_s = p_s +p_info +"\n"

        item["bingyin"] = p_s[:-1]
        # print(p_s)
        url = (item["url"]).format("jiancha") #检查地址

        yield Request(url,callback=self.parse_jiancha,meta={"item":deepcopy(item)},dont_filter=True)
    #检查
    def parse_jiancha(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@class='leftArticle2']/div/ul/li")
        li_s = ""
        for li in li_list:
            li_info = li.xpath("./a/text()").extract_first()
            li_s = li_s + li_info +"、"

        item["jianchaxiangmu"] = li_s[:-1]

        p_list = response.xpath("//div[@class='leftArticle2']/p")
        p_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            p_info = str(p_info_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
            "").replace("\\u3000","").replace("\\xa0","").replace("\\n","").replace("\\t","").replace("\\r",
            "").replace("','","").replace('"target=_blank>',"")

            if len(p_info)>1:
                p_s = p_s + p_info +"\n"


        item["jianchaxiangqing"] = p_s[:-1]
        # print(p_s)
        url = (item["url"]).format("zhenduan")
        yield Request(url,callback=self.parse_zhenduan,meta={"item":deepcopy(item)},dont_filter=True)

    def parse_zhenduan(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='leftArticle2']/p")
        p_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            p_info = str(p_info_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
            "").replace("\\u3000","").replace("\\xa0","").replace("\\n","").replace("\\t","").replace("\\r",
            "").replace("','","").replace('"target=_blank>',"")

            if len(p_info)>1:
                p_s = p_s + p_info +"\n"

        item["zhenduan"] = p_s[:-1]

        # print(item)

        yield item