# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from scrapy import Request


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['meishichina.com/']
    start_urls = ['https://www.meishichina.com/YuanLiao/gongxiao/']

    def parse(self, response):
        item = {}
        div_list = response.xpath("//div[@class='category_box mt20']/div")
        for div in div_list:
            class_name = div.xpath("./h3/text()").extract_first()
            item["class_name"] = class_name
            li_list = div.xpath("./ul/li")
            for li in li_list:
                title_raw = li.xpath("./a/@title").extract_first()
                if "/" in title_raw:
                    title = (title_raw.split("/"))[1]
                else:
                    title = title_raw

                item["title"] = title

                url_dis = li.xpath("./a/@href").extract_first()
                yield Request(url_dis, callback=self.parse_disease, dont_filter=True, meta={"item": deepcopy(item)})

    def parse_disease(self, response):
        item = response.meta["item"]

        text_raw = response.xpath("//div[@class='space_left']/p[@class='collect_txt']/text()").extract()
        text = str(text_raw).replace("['", "").replace("']", "").replace(" ", "").replace("\\u3000",
        "").replace(",", "，").replace("'", "").replace('"', "")
        # print(text)
        item["disease"] = text
        li_list = response.xpath("//div[@class='space_left']/div[@class='tui_c']/ul/li")
        tui_c = ""
        for li in li_list:
            a_text_raw = li.xpath("./a/text()").extract()
            a_text = str(a_text_raw).replace("['", "").replace("']", "").replace(" ", "").replace("\\n",
            "").replace("','", "")
            tui_c += a_text + ","
        # print(tui_c[:-1])
        item["tui_c"] = tui_c

        yield Request("https://www.meishichina.com/", callback=self.parse_fin, dont_filter=True, meta={"item": deepcopy(item)})


    def parse_fin(self,response):
        item = response.meta["item"]
        yield item









