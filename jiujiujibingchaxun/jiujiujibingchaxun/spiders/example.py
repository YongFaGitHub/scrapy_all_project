# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import random
import time


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['99.com']
    start_urls = ['http://jbk.99.com.cn/']


    def process_request(self, request, spider):
        # if not request.meta['proxies']:
        for url in self.start_urls:
            yield scrapy.Request(url,callback=self.parse,meta={'proxy':"http://120.26.110.59:8080"})

    def parse(self, response):
        div_list = response.xpath("//div[@class='s-menu-cont']/div[1]/following-sibling::*")
        item = {}
        for div in div_list:
            li_list = div.xpath("./div/ul/li")

            if len(li_list) >1 :
                li_list2 = div.xpath("./div/ul/li[1]/following-sibling::*")
                for li in li_list2:
                    big_title_raw = li.xpath("./a/text()").extract()
                    big_title = str(big_title_raw).replace("[","").replace("]","").replace("\\r",
                    "").replace("\\n","").replace(" ","")
                    item["big_title"] = big_title
                    url1 = li.xpath("./a/@href").extract_first()
                    # print(url1,"!!!!!!!!!!!!!!!!!!1")
                    time.sleep(0.3)
                    yield Request(url1,callback=self.parse_one, meta={"item": deepcopy(item)},dont_filter=True)

            else:
                url2 = li_list.xpath("./a/@href").extract_first()
                big_title_raw = li_list.xpath("./a/text()").extract()
                big_title = str(big_title_raw)
                # print(url2,"@@@@@@@@@@@@@@@@@@@@@@")
                time.sleep(0.1)
                yield Request(url2,callback=self.parse_one, meta={"item": deepcopy(item)},dont_filter=True)


    def parse_one(self,response):
        item = response.meta["item"]
        dl_list = response.xpath("//div[@class='part-cont3']/dl")
        for dl in dl_list:
            url = dl.xpath("./dd//h3/a/@href").extract_first()
            title_raw = dl.xpath("./dd//h3/a/@title").extract_first()
            title = str(title_raw)
            item["title"] = title
            time.sleep(0.1)
            yield Request(url,callback=self.parse_two, meta={"item": deepcopy(item)},dont_filter=True)

        #下一页的地址
        next_url = response.xpath("//div[@class='digg']/a[text()='> ']/@href").extract_first()
        yield Request(next_url,callback=self.parse_one, meta={"item": deepcopy(item)},dont_filter=True)

    def parse_two(self,response):
        item = response.meta["item"]
        disease_raw = response.xpath("//div[@class='d-js-cont']/dl/dd/p/text()").extract()
        disease = str(disease_raw).replace("['","").replace("']","").replace("\\r","").replace("\\n",
        "").replace(" ","").replace("','","").replace("\\u3000","").replace("\\t","").replace("\\xa0","")
        item["disease"] = disease

        keshi_raw = response.xpath("//font[text()='就诊科室：']/following-sibling::*/text()").extract()
        keshi = str(keshi_raw).replace("[","").replace("]","").replace(" ","").replace("','","、").replace("'","")
        if len(keshi) >1:
            item["keshi"] = keshi
        else:
            item["keshi"] = "暂无"

        yaopin_raw = response.xpath("//font[text()='疾病用药：']/following-sibling::*//text()").extract()
        yaopin = str(yaopin_raw).replace("[", "").replace("]", "").replace(" ", "").replace("','','", "、").replace("'", "")
        if len(yaopin) > 1:
            item["yaopin"] = yaopin

        else:
            item["yaopin"] = "暂无"
        time.sleep(0.1)
        url = response.xpath("//div[@id='disease']/ul/li/a[text()='病 因']/@href").extract_first()
        # if url is None:
        # print(item,"@@@/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        yield Request(url,callback=self.parse_bingyin, meta={"item": deepcopy(item)},dont_filter=True)

    #疾病病因
    def parse_bingyin(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='d-js-cont2']/p")
        p_info_s= ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            # print(p_info)
            p_info = str(p_info_raw).replace("['","").replace("']","").replace("\\u3000","").replace("\\xa0",
            "").replace(" ","").replace("','","").replace("\\r","").replace("\\n","").replace("\\t","")
            if len(p_info) > 1:
                p_info_s = p_info_s + p_info +"\n"

        item["bingyin"] = p_info_s
        # print(item)
        time.sleep(0.1)
        url = response.xpath("//div[@id='disease']/ul/li/a[text()='症 状']/@href").extract_first()
        yield Request(url, callback=self.parse_zhengzhuang, meta={"item": deepcopy(item)}, dont_filter=True)

    #疾病症状
    def parse_zhengzhuang(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='d-js-cont2']/p")
        p_info_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            # print(p_info)
            p_info = str(p_info_raw).replace("['", "").replace("']", "").replace("\\u3000", "").replace("\\xa0",
            "").replace(" ","").replace("','", "").replace("\\r", "").replace("\\n", "").replace("\\t", "")
            if len(p_info) > 1:
                p_info_s = p_info_s + p_info + "\n"

        item["zhengzhuang"] = p_info_s
        time.sleep(0.1)
        url = response.xpath("//div[@id='disease']/ul/li/a[text()='检 查']/@href").extract_first()
        yield Request(url, callback=self.parse_jiancha, meta={"item": deepcopy(item)}, dont_filter=True)

    #疾病检查
    def parse_jiancha(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='d-js-cont2']/p")
        p_info_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            # print(p_info)
            p_info = str(p_info_raw).replace("['", "").replace("']", "").replace("\\u3000", "").replace("\\xa0",
                                                                                                        "").replace(" ",
                                                                                                                    "").replace(
                "','", "").replace("\\r", "").replace("\\n", "").replace("\\t", "")
            if len(p_info) > 1:
                p_info_s = p_info_s + p_info + "\n"

        item["jiancha"] = p_info_s
        time.sleep(0.1)
        url = response.xpath("//div[@id='disease']/ul/li/a[text()='预 防']/@href").extract_first()
        yield Request(url, callback=self.parse_yufang, meta={"item": deepcopy(item)}, dont_filter=True)


    #疾病预防
    def parse_yufang(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='d-js-cont2']/p")
        p_info_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            # print(p_info)
            p_info = str(p_info_raw).replace("['", "").replace("']", "").replace("\\u3000", "").replace("\\xa0",
                                                                                                        "").replace(" ",
                                                                                                                    "").replace(
                "','", "").replace("\\r", "").replace("\\n", "").replace("\\t", "")
            if len(p_info) > 1:
                p_info_s = p_info_s + p_info + "\n"
        time.sleep(0.1)
        item["yufang"] = p_info_s
        url = response.xpath("//div[@id='disease']/ul/li/a[text()='治 疗']/@href").extract_first()
        yield Request(url, callback=self.parse_zhiliao, meta={"item": deepcopy(item)}, dont_filter=True)

    #治疗
    def parse_zhiliao(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='d-js-cont2']/p")
        p_info_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            # print(p_info)
            p_info = str(p_info_raw).replace("['", "").replace("']", "").replace("\\u3000", "").replace("\\xa0",
                                                                                                        "").replace(" ",
                                                                                                                    "").replace(
                "','", "").replace("\\r", "").replace("\\n", "").replace("\\t", "")
            if len(p_info) > 1:
                p_info_s = p_info_s + p_info + "\n"
        time.sleep(0.1)
        item["zhiliao"] = p_info_s
        url = response.xpath("//div[@id='disease']/ul/li/a[text()='鉴 别']/@href").extract_first()
        yield Request(url, callback=self.parse_jianbie, meta={"item": deepcopy(item)}, dont_filter=True)

    #鉴别
    def parse_jianbie(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='d-js-cont2']/p")
        p_info_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            # print(p_info)
            p_info = str(p_info_raw).replace("['", "").replace("']", "").replace("\\u3000", "").replace("\\xa0",
                                                                                                        "").replace(" ",
                                                                                                                    "").replace(
                "','", "").replace("\\r", "").replace("\\n", "").replace("\\t", "")
            if len(p_info) > 1:
                p_info_s = p_info_s + p_info + "\n"
        time.sleep(0.1)
        item["jianbie"] = p_info_s


        yield item
