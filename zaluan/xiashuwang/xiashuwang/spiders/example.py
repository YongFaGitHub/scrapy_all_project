# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import os
import re

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['3.com']
    start_urls = ['http://www.xiabook.com/']

    def parse(self, response):
        item  = {}
        div_list = response.xpath("//div[@class='vk_nv_sub png cl']/div")
        for div in div_list:
            big_class = div.xpath("./div/p/text()").extract_first()
            item["big_class"] = big_class
            li_list = div.xpath("./ul/li")
            for li in li_list:
                small_class = li.xpath("./a/text()").extract_first()
                item["small_class"] = small_class
                url = li.xpath("./a/@href").extract_first()  #每个大类别的地址
                yield Request(url,callback=self.parse_liebiao,dont_filter=True,meta={"item":deepcopy(item)})


    def parse_liebiao(self,response):
        item = response.meta["item"]
        div_list = response.xpath("//div[@class='bbox']")
        for div in div_list:
            title_raw = div.xpath("./div[@class='bintro']/h3/a/text()").extract_first()
            title = str(title_raw).replace(":","：")
            item["title"] = title
            url_raw = div.xpath("./div[@class='bintro']/h3/a/@href").extract_first()
            url = "http://www.xiabook.com" + url_raw  #每一本书的地址

            yield Request(url,callback=self.parse_disease,dont_filter=True,meta={"item":deepcopy(item)})

        next_url_raw = response.xpath("//div[@class='pages']/a[text()='下一页']/@href").extract_first()
        if next_url_raw is not None:
            next_url = "http://www.xiabook.com" + next_url_raw
            yield Request(next_url,callback=self.parse_liebiao,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_disease(self,response):
        item = response.meta["item"]
        # print("@@@@@@@@@@@@@@@@@@@@@@@")
        td_list = response.xpath("//div[@id='yuedu']//tr/td")
        for td in td_list :
            li_list = td.xpath("./ul/li")
            for li in li_list:
                title_name_raw = li.xpath("./a/@title").extract_first()
                title_name = str(title_name_raw).replace(":","：")
                item["title_name"] = title_name
                url_raw = li.xpath("./a/@href").extract_first()

                if url_raw is not   None:
                    url = "http://www.xiabook.com" + url_raw   #每一章节地址
                    # print("@@@@@@@@@@@@@@@@@@@@@")
                    yield Request(url,callback=self.parse_disease_one,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_disease_one(self,response):
        item = response.meta["item"]

        info_raw = response.xpath("//div[@class='zw']//text()").extract()
        info = str(info_raw).replace("['","").replace("']","").replace("\\n","").replace(" ","").replace("\\t",
        "").replace("\\r","").replace("\\u3000","").replace("\\xa0","").replace("','','","\n").replace("','",
        "\n").replace("wWw．Ｌｚｕｏｗｅｎ．ｃｏｍ^下 ?书? 网","").replace("wwＷ．7wenｗｅｎ.com","").replace("�","")

        b_list  = re.findall("([wWＷ].*?[ＭMm])", info, re.S)
        for b in b_list:
            info = info.replace(b,"")
        # print(info)

        try:os.mkdir("J:/xiaoshuo.txt")
        except:pass

        try:os.mkdir("J:/xiaoshuo.txt/{}".format(item["big_class"]))
        except:pass

        try:os.mkdir("J:/xiaoshuo.txt/{}/{}".format(item["big_class"],item["small_class"]))
        except:pass

        try:os.mkdir("J:/xiaoshuo.txt/{}/{}/{}".format(item["big_class"], item["small_class"],item["title"]))
        except:pass

        with open("J:/xiaoshuo.txt/{}/{}/{}/{}.txt".format(item["big_class"], item["small_class"],item["title"],item["title_name"]),"w",encoding="utf-8") as f :
            f.write(info)

        print(item["big_class"], item["small_class"],item["title"],item["title_name"],"完成写入")