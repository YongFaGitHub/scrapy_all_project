# -*- coding: utf-8 -*-
import scrapy
import scrapy
from scrapy.http import Request
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['jbk.39.net/']
    start_urls = ['http://jbk.39.net/']

    def parse(self, response):
        item = {}
        dl_list = response.xpath("//div[@class='mapList']/dl")
        # 拿到部位

        for dl in dl_list:
            position_list = dl.xpath("./dd/div[1]/ul/li")
            for position in position_list:
                jibing_list = position.xpath("./span[@class='right']/a")  # 病症列表
                for jibing in jibing_list:
                    title_raw = jibing.xpath("./text()").extract_first()  # 拿到标题
                    title = str(title_raw)
                    item["title"] = title

                    url = jibing.xpath("./@href").extract()[0]  # 拿到标题的url
                    len_url = url.split("/")
                    if len(len_url) == 5:
                        yield Request(url, callback=self.parse_one, meta={"item": deepcopy(item)}, dont_filter=True)

    def parse_one(self, response):
        item = response.meta["item"]
        url = response.xpath("//div[@class='leftNav']/ul/li/a[text()='临床检查']/@href").extract_first()
        yield Request(url, callback=self.parse_two, meta={"item": deepcopy(item)}, dont_filter=True)

    def parse_two(self, response):
        item = response.meta["item"]

        tr1_raw= response.xpath("//div[@class='checkbox']//tbody/tr[1]//text()").extract()
        tr1 = str(tr1_raw).replace("['","").replace("']","").replace(" ","").replace("\\r","").replace("\\n",
        "").replace("','','",",").replace("','","")
        tr_all = tr1 +"\n"
        item["all"] = tr_all

        ty_list = response.xpath("//div[@class='checkbox']//tbody/tr[1]//following-sibling::*")

        for tr in ty_list:
            td_list = tr.xpath("./td")
            tr_s = ""
            for i in range(1,len(td_list)):
                tr_raw = tr.xpath("./td[{}]//text()".format(str(i))).extract()
                tr_1_s = str(tr_raw).replace("['","").replace("']","").replace(" ","、")
                tr_s = tr_s + tr_1_s +","

            item["disease"] = tr_s
            url = tr.xpath(".//a/@href").extract_first()
            if url is not None:
                yield Request(url, callback=self.parse_three, meta={"item": deepcopy(item)}, dont_filter=True)


    def parse_three(self,response):
        item = response.meta["item"]
        text_raw = response.xpath("//div[@id='refdisease']/div[@class='text']/p/text()").extract()
        text = str(text_raw).replace("['","").replace("']","").replace("\\u3000","").replace(",","，")
        info = item["disease"] + text

        with open("H:/pycharmproject/project/39jk/bingzhengkujiancha/bingzhengkujiancha/spiders/{}.csv".format(item["title"]),"a+",encoding="utf-8") as f:
            f.write(info)
            f.write("\n")




