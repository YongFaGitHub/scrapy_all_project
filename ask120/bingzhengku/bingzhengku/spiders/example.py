# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from scrapy import Request

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.120ask.com']
    start_urls = ['http://tag.120ask.com/jibing/']


    def parse(self, response):
        li_list = response.xpath("//ul[@class='p_leftdivnav']/li")
        item = {}
        for li in li_list:
            p_list = li.xpath("./div[2]/span/p")
            for p in p_list:
                span_list = p.xpath("./span")
                for span in span_list:
                    title_raw = span.xpath("./a/@title").extract_first()
                    item["title"] = title_raw

                    url_raw = span.xpath("./a/@href").extract_first()

                    url = "http://tag.120ask.com" + url_raw
                    if "jibing" in url:
                        yield Request(url,callback=self.parse_one,meta={"item":deepcopy(item)},dont_filter=True)


    def parse_one(self,response):
        item = response.meta["item"]
        url_disease = response.xpath("//div[@class='p_lbox1_ab']/p/a/@href").extract_first()

        img_url_raw = response.xpath("//div[@class='p_lbox1_ab']/a/img/@src").extract_first()
        img_url = "http:" + img_url_raw
        item["img_url"] = img_url

        yield Request(img_url,callback=self.parse_img,meta={"item":deepcopy(item)},dont_filter=True)
        # yield Request(url_disease,callback=self.parse_disease,meta={"item":deepcopy(item)},dont_filter=True)

    def parse_img(self,response):
        item = response.meta["item"]
        with open("I:/疾病图片/ask120/{}.png".format(item["title"]),"wb") as f:
            f.write(response.body)

        with open("H:/pycharmproject/project/ask120/bingzhengku/bingzhengku/spiders/img_url.txt","a+",encoding="utf-8") as f:
            f.write(item["title"])
            f.write("、")
            f.write(item["img_url"])
            f.write("\n")










    #概述
    def parse_disease(self,response):
        item = response.meta["item"]
        info_disease_raw = response.xpath("//div[@class='p_cleftartbox']/div[2]//text()").extract()
        info_disease = str(info_disease_raw).replace("['","").replace("']","").replace("\\r","").replace("\\n",
        "").replace("\\xa0","").replace("\\u3000","").replace(' ',"").replace("','","")
        item["disease"] = info_disease

        bingyin_url = response.xpath("//div[@class='m980 pageNav']/a[text()='病因']/@href").extract_first()
        yield Request(bingyin_url,callback=self.parse_bingyin,meta={"item":deepcopy(item)},dont_filter=True)

    #病因
    def parse_bingyin(self,response):
        item = response.meta["item"]
        info_disease_raw = response.xpath("//div[@class='p_cleftartbox']/div[2]//text()").extract()
        info_disease = str(info_disease_raw).replace("['","").replace("']","").replace("\\r","").replace("\\n",
        "").replace(" ","").replace("','\\u3000\\u3000","\n").replace("','","").replace('\\xa0',
        "").replace("\\u3000","")

        item["bingyin"] = info_disease


        bingyin_url = response.xpath("//div[@class='m980 pageNav']/a[text()='症状']/@href").extract_first()
        yield Request(bingyin_url, callback=self.parse_zhengzhuang, meta={"item": deepcopy(item)}, dont_filter=True)

    #症状
    def parse_zhengzhuang(self,response):
        item=response.meta["item"]
        info_disease_raw = response.xpath("//div[@class='p_cleftartbox']/div[2]//text()").extract()
        info_disease = str(info_disease_raw).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
        "").replace(" ", "").replace("','\\u3000\\u3000", "\n").replace("','", "").replace('\\xa0',
        "").replace("\\u3000", "")

        item["zhengzhuang"] = info_disease

        bingyin_url = response.xpath("//div[@class='m980 pageNav']/a[text()='检查']/@href").extract_first()
        yield Request(bingyin_url, callback=self.parse_jiancha, meta={"item": deepcopy(item)}, dont_filter=True)

    #检查
    def parse_jiancha(self,response):
        item = response.meta["item"]
        info_disease_raw = response.xpath("//div[@class='p_cleftartbox']/div[2]//text()").extract()
        info_disease = str(info_disease_raw).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
        "").replace(" ", "").replace("','\\u3000\\u3000", "\n").replace("','", "").replace('\\xa0',
        "").replace("\\u3000", "")

        item["jiancha"] = info_disease

        bingyin_url = response.xpath("//div[@class='m980 pageNav']/a[text()='鉴别']/@href").extract_first()
        yield Request(bingyin_url, callback=self.parse_jianbie, meta={"item": deepcopy(item)}, dont_filter=True)

    #鉴别
    def parse_jianbie(self,response):
        item = response.meta["item"]
        info_disease_raw = response.xpath("//div[@class='p_cleftartbox']/div[2]//text()").extract()
        info_disease = str(info_disease_raw).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
        "").replace(" ", "").replace("','\\u3000\\u3000", "\n").replace("','", "").replace('\\xa0',
        "").replace("\\u3000", "")

        item["jianbie"] = info_disease

        bingyin_url = response.xpath("//div[@class='m980 pageNav']/a[text()='预防']/@href").extract_first()
        yield Request(bingyin_url, callback=self.parse_yufang, meta={"item": deepcopy(item)}, dont_filter=True)



    def parse_yufang(self,response):
        item = response.meta["item"]
        info_disease_raw = response.xpath("//div[@class='p_cleftartbox']/div[2]//text()").extract()
        info_disease = str(info_disease_raw).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
        "").replace(" ", "").replace("','\\u3000\\u3000", "\n").replace("','", "").replace('\\xa0',
        "").replace("\\u3000", "")

        item["yufang"] = info_disease

        bingyin_url = response.xpath("//div[@class='m980 pageNav']/a[text()='治疗']/@href").extract_first()
        yield Request(bingyin_url, callback=self.parse_zhiliao, meta={"item": deepcopy(item)}, dont_filter=True)


    def parse_zhiliao(self,response):
        item = response.meta["item"]
        info_disease_raw = response.xpath("//div[@class='p_cleftartbox']/div[2]//text()").extract()
        info_disease = str(info_disease_raw).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
        "").replace(" ", "").replace("','\\u3000\\u3000", "\n").replace("','", "").replace('\\xa0',
        "").replace("\\u3000", "")

        item["zhiliao"] = info_disease

        yield item

