# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re
import json
from copy import deepcopy
import math


class AllexampleSpider(scrapy.Spider):
    name = 'allexample'
    allowed_domains = ['h5.izhangchu.com']
    start_urls = ['http://h5.izhangchu.com/category/subtype.html#4']

    def parse(self, response):
        list = []
        item = {}
        dl_list = response.xpath("//div[@id='DishesCategory-wrap']/dl")
        for dl in dl_list[:-1]:
            li_list = dl.xpath("./dd/ul/li")
            for li in li_list:

                id_num_raw  = li.xpath("./a/@href").extract_first()
                id_num = re.findall("id=(.*)", id_num_raw)

                list.append(int(id_num[0]))

        list.sort()
        for num in list:
            item["id_num"] = num

            url = "http://api.izhangchu.com/index.php?methodName=CategorySearch&cat_id={}&type=1&size=5&page=1".format(num)
            yield Request(url,callback=self.parse_list,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_list(self,response):
        item = response.meta["item"]
        json_r = json.loads(response.body)
        num_raw = json_r["data"]["total"]
        num = int(num_raw)
        page_num_raw = math.ceil(num/5)
        page_num  = int(page_num_raw) + 1

        for num in range(1,page_num):

            url = "http://api.izhangchu.com/index.php?methodName=CategorySearch&cat_id={}&type=1&size=5&page={}".format(
                item["id_num"],num)

            yield Request(url,callback=self.parse_json,dont_filter=True,meta={"item":deepcopy(item)})

    #json页面
    def parse_json(self,response):
        item=response.meta["item"]
        json_r = json.loads(response.body)
        page_one_list = json_r["data"]["data"]

        item["class"] = json_r["data"]["page_title"]
        for one in page_one_list:
            disease_num = one['dishes_id']
            item["title"] = one["title"]
            item["big_class"] = one["tags_info"][0]["text"]
            item["description"] = one["description"]

            url = "http://h5.izhangchu.com/dishes_view/index.html?&dishes_id={}".format(disease_num)

            # print(url)
            yield Request(url,callback=self.parse_disease,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_disease(self,response):
        item = response.meta["item"]

        item["zuofa"] = ""
        item["shicai"] = ""
        item["changshi"] = ""
        item["zhizuozhidao"] = ""
        item["xiangyi"] = ""
        item["xiangke"] =""


        li_list = response.xpath("//div[@class='goods-detail product-box']/div[@class='nav-height']//li")
        for li in li_list:
            title = li.xpath("./a/text()").extract_first()
            id_class = li.xpath("./a/@id").extract_first()
            if title =="做法":
                # zuofa_id = id_class
                div_xpath = response.xpath("//div[@class='goods-detail product-box']/div[@class='section-content xsj {}']".format(id_class))
                li_list = div_xpath.xpath(".//li")

                zuofa_s = ""
                for li in li_list:
                    li_text_raw = li.xpath("./div//text()").extract()
                    li_text = str(li_text_raw).replace("['","").replace("']","").replace(" ","").replace("','","、")

                    zuofa_s = zuofa_s + li_text +"\n"

                item["zuofa"] = zuofa_s


            if title == "食材":
                div_xpath = response.xpath("//div[@class='goods-detail product-box']/div[@class='section-content xsj {}']".format(id_class))
                li_list = div_xpath.xpath("./div[@class='material']//div[@class='material-list']/ul/li")
                shicai_s = ""
                for li in li_list:
                    info_one_raw = li.xpath("./text()").extract()
                    info_one = str(info_one_raw).replace("['","").replace("']","").replace(" ",
                        "").replace("\\r","").replace("\\n","").replace("、","，")


                    info_two_raw = li.xpath("./span/text()").extract()

                    if len(info_two_raw) >0:
                        info_two = str(info_two_raw).replace("['","").replace("']","").replace(" ",
                        "").replace("\\r","").replace("\\n","").replace("、","，")
                        shicai_s  = shicai_s + info_one + "-" +info_two + "\n"

                    else:
                        shicai_s = shicai_s +info_one +"\n"
                item["shicai"] = shicai_s
                # print( item["shicai"])


            if title =="相关常识":
                div_xpath = response.xpath("//div[@class='goods-detail product-box']/div[@class='section-content xsj {}']".format(id_class))
                li_list = div_xpath.xpath("./div[@class='sense-md']//div[@class='sense-list']//li")

                for li in li_list:
                    changshi_fenlei_text  = li.xpath("./h5/text()").extract_first()
                    if changshi_fenlei_text =='相关常识':
                        info_one_text_raw = li.xpath("./div/text()").extract()
                        info_one_text = str(info_one_text_raw).replace("['","").replace("']","").replace(" ",
                        "").replace("\\r","").replace("\\n","")

                        item["changshi"] = info_one_text


                    if changshi_fenlei_text =="制作指导":
                        info_two_text_raw = li.xpath("./div/text()").extract()
                        info_two_text = str(info_two_text_raw).replace("['","").replace("']","").replace(" ",
                        "").replace("\\r","").replace("\\n","")

                        item["zhizuozhidao"] = info_two_text


            if title == "相宜相克":
                div_xpath = response.xpath(
                    "//div[@class='goods-detail product-box']/div[@class='section-content xsj {}']".format(id_class))
                li_list = div_xpath.xpath(".//div[@class='suit-list']/ul/li")
                xiangyi_s = ""
                xiangke_s = ""
                for li in li_list:
                    text_raw= li.xpath("./div[@class='hd']//text()").extract()

                    text = str(text_raw).replace("['","").replace("']","").replace(" ","").replace("','",
                    "").replace(" ",
                        "").replace("\\r","").replace("\\n","") + "："

                    if "相宜" in text:
                        div_list = li.xpath("./div[@class='list']/div")
                        for div in div_list:
                            what_raw = div.xpath("./h5/text()").extract()
                            what = str(what_raw).replace("['","").replace("']","").replace(" ",
                        "").replace("\\r","").replace("\\n","")

                            why_raw = div.xpath("./div[@class='txt']/text()").extract()
                            why = str(why_raw).replace("['","").replace("']","").replace(" ",
                        "").replace("\\r","").replace("\\n","")

                            xiangyi_s = xiangyi_s + what + "-" + why + "\n"


                    item["xiangyi"] = xiangyi_s


                    if "相克" in text:
                        div_list = li.xpath("./div[@class='list']/div")
                        for div in div_list:
                            what_raw = div.xpath("./h5/text()").extract()
                            what = str(what_raw).replace("['","").replace("']","").replace(" ",
                        "").replace("\\r","").replace("\\n","")

                            why_raw = div.xpath("./div[@class='txt']/text()").extract()
                            why = str(why_raw).replace("['","").replace("']","").replace(" ",
                        "").replace("\\r","").replace("\\n","")

                            xiangke_s = xiangke_s + what + "-" + why + "\n"

                    item["xiangke"] = xiangke_s


        yield item
        # print(item)


