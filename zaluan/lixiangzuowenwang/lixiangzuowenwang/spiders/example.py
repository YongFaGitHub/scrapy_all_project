# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import re
import os

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['lzuowen.com/']
    start_urls = ['http://www.lzuowen.com/book/']

    def parse(self, response):
        item = {}
        list = [1,2,4]
        for i in list:
            div_list = response.xpath("//div[@id='content']/div[{}]/div".format(i))
            for div in div_list:
                url_raw = div.xpath("./h2/span/a[text()='更多']/@href").extract_first()
                url = "http://www.lzuowen.com" + url_raw

                big_class_raw = div.xpath("./h2/a/text()").extract_first()
                item["big_class"] = big_class_raw

                # print(item)
                yield Request(url,callback=self.parse_liebiao,meta={"item":deepcopy(item)},dont_filter=True)


    def parse_liebiao(self,response):
        item = response.meta["item"]
        div_list  = response.xpath("//div[@class='box']/div[@class='bk1']")
        for div in div_list:
            title = div.xpath("./h3/a/text()").extract_first()
            item["title"] = title

            url_raw = div.xpath("./h3/a/@href").extract_first()
            url = "http://www.lzuowen.com" + url_raw + "read.html"   #全部章节的地址
            yield  Request(url,callback=self.parse_disease,dont_filter=True,meta={"item":deepcopy(item)})

        #下一页
        next_url_raw = response.xpath("//div[@class='box']/div[@class='yema']/a[text()='下一页']/@href").extract_first()
        if next_url_raw is not None:
            next_url = "http://www.lzuowen.com" + next_url_raw
            yield Request(next_url,callback=self.parse_liebiao,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_disease(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@class='mulu']/ul/li")
        for li in li_list:
            title_name = li.xpath("./a/text()").extract_first()
            item["title_name"] = title_name
            url_raw = li.xpath("./a/@href").extract_first()
            url = "http://www.lzuowen.com" + url_raw
            yield Request(url,callback=self.parse_one_page,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_one_page(self,response):
        item = response.meta["item"]
        # p标签之内的类型：文学名著，外国文学，儿童文学，散文随笔，历史传记
        p_list = response.xpath("//div[@id='content']/p")

        info_s = ""
        for p in p_list:
            info_raw = p.xpath(".//text()").extract()
            info = str(info_raw).replace("\\u3000","").replace("['","").replace("']","").replace("[","").replace("]",
            "").replace("\\xa0","").replace("\\n","").replace("\\t","").replace("\\r","").replace(" ","").replace("','",
            "")
            if len(info)>1:
                info_s = info_s + info +"\n"
        if len(info_s)<100:
            info_s_raw = response.xpath("//div[@id='content']/text()").extract()
            info_s = str(info_s_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace(
                "\\n","").replace("\\t", "").replace("\\r", "").replace(" ", "").replace("','','", "\n").replace("\\xa0",
                 "").replace("\\u3000", "").replace("','", "")

            try:
                os.mkdir("J:/理想作文网小说")
            except:
                pass

            try:
                os.mkdir("J:/理想作文网小说/{}".format(item["big_class"]))
            except:
                pass
            try:
                os.mkdir("J:/理想作文网小说/{}/{}".format(item["big_class"], item["title"]))
            except:
                pass

            with open("J:/理想作文网小说/{}/{}/{}.txt".format(item["big_class"], item["title"], item["title_name"]), "w",
                      encoding="utf-8") as f:

                f.write(info_s)
                print(item["big_class"], item["title"], item["title_name"], "成功写入!!!!!!")



        else:
            try:os.mkdir("J:/理想作文网小说")
            except:pass

            try:os.mkdir("J:/理想作文网小说/{}".format(item["big_class"]))
            except:pass
            try:os.mkdir("J:/理想作文网小说/{}/{}".format(item["big_class"],item["title"]))
            except:pass


            with open("J:/理想作文网小说/{}/{}/{}.txt".format(item["big_class"],item["title"],item["title_name"]),"w",encoding="utf-8") as f:

                f.write(info_s)
                print(item["big_class"],item["title"],item["title_name"],"成功写入!!!!!!")













