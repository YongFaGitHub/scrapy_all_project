# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from scrapy import Request
import time


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.xiachufang.com/']
    start_urls = ['http://www.xiachufang.com/category/']

    def parse(self, response):
        list = ["3", "4", "7", "8", "9"]
        item = {}
        item["small_class"] = ""

        for i in list:

            div_lsit = response.xpath("//div[@class='block-bg p40 font16']/div[{}]".format(str(i)))
            for div in div_lsit:
                big_class_raw = div.xpath(".//h3/text()").extract_first()
                item["big_class"] = big_class_raw

                h4_lsit = div.xpath("./div[3]/h4")
                for h4 in h4_lsit:

                    li_list = h4.xpath("./following-sibling::*[1]/li")
                    if li_list is not None:
                        small_class_raw = h4.xpath(".//text()").extract()
                        small_class = str(small_class_raw).replace("['","").replace("']","").replace("[",
                        "").replace("]","").replace(" ","").replace("','","").replace("\\n","")
                        item["small_class"] = small_class


                        for li in li_list:
                            title = li.xpath("./a/text()").extract_first()
                            item["title"] = title

                            url_raw = li.xpath("./a/@href").extract_first()
                            url = "http://www.xiachufang.com" + url_raw
                            yield Request(url,callback=self.parse_disease,dont_filter=True,meta={"item":deepcopy(item)})


                    else:

                        title = h4.xpath("./a/text()").extract_first()
                        item["title"] = title

                        url2_raw =  h4.xpath("./a/@href").extract_first()
                        url2 ="http://www.xiachufang.com" + url2_raw
                        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        print(url2)
                        time.sleep(10000)
                        yield Request(url2, callback=self.parse_disease, dont_filter=True,meta={"item": deepcopy(item)})

    #进入每一种食材的详情页面
    def parse_disease(self,response):
        item = response.meta["item"]

        item["gongxiao"] = ""
        item["tiaoxuan"] = ""
        item["cunchu"] = ""
        item["yingyangzhishi"] = ""
        item["shiyongrenqun"] = ""
        item["yinshijinji"] = ""
        item["zhizuozhishi"] = ""
        item["bieming"] = ""
        item["shiling"] = ""
        item["cunchushijian"] = ""
        item["disease_info"] = ""


        h3_list = response.xpath("//div[@class='ing-detail hidden']/h3")
        #营养功效里面的内容
        if h3_list is not None:#如果为空，则是没有以下的内容
            for h3 in h3_list:
                text = h3.xpath("./text()").extract_first()
                if text is not None:
                    #判断功效是否存在
                    if "功效" in text:
                        gongxiao_raw = h3.xpath("./following-sibling::*[1]/text()").extract()
                        gongxiao = str(gongxiao_raw).replace("['","").replace("']","").replace("[","").replace("]",
                        "").replace(" ","").replace("\\r","").replace("\\n","").replace("','","、")
                        if len(gongxiao) >1:
                            item["gongxiao"] = gongxiao

                    #判断挑选是否存在
                    if "挑选" in text:
                        tiaoxuan_raw = h3.xpath("./following-sibling::*[1]/text()").extract()
                        tiaoxuan = str(tiaoxuan_raw).replace("['","").replace("']","").replace("[","").replace("]",
                        "").replace(" ","").replace("\\r","").replace("\\n","").replace("','","、")

                        if len(tiaoxuan) >1:
                            item["tiaoxuan"] = tiaoxuan

                    # 判断存储是否存在
                    if "储存" in text:
                        cunchu_raw = h3.xpath("./following-sibling::*[1]/text()").extract()
                        cunchu = str(cunchu_raw).replace("['", "").replace("']", "").replace("[", "").replace("]",
                        "").replace(" ", "").replace("\\r", "").replace("\\n", "").replace("','", "、")
                        if len(cunchu) > 1:
                            item["cunchu"] = cunchu

                    # 判断营养知识是否存在
                    if "营养小知识" in text or "营养分析" in text:
                        yingyangzhishi_raw = h3.xpath("./following-sibling::*[1]/text()").extract()
                        yingyangzhishi = str(yingyangzhishi_raw).replace("['", "").replace("']", "").replace("[", "").replace("]",
                        "").replace(" ", "").replace("\\r", "").replace("\\n", "").replace("','", "、")
                        if len(yingyangzhishi) > 1:
                            item["yingyangzhishi"] = yingyangzhishi

                    # 判断适用人群是否存在
                    if "适用人群" in text or "相关人群" in text:
                        shiyongrenqun_raw = h3.xpath("./following-sibling::*[1]/text()").extract()
                        shiyongrenqun = str(shiyongrenqun_raw).replace("['", "").replace("']", "").replace("[",
                        "").replace("]","").replace(" ", "").replace("\\r", "").replace("\\n", "").replace("','", "、")
                        if len(shiyongrenqun) > 1:
                            item["shiyongrenqun"] = shiyongrenqun

                    # 判断饮食宜忌是否存在
                    if "饮食宜忌"  in text or "食用禁忌" in text:
                        yinshiyiji_raw = h3.xpath("./following-sibling::*[1]/text()").extract()
                        yinshiyiji = str(yinshiyiji_raw).replace("['", "").replace("']", "").replace("[",
                        "").replace("]", "").replace(" ", "").replace("\\r", "").replace("\\n", "").replace("','", "、")
                        if len(yinshiyiji) > 1:
                            item["yinshiyiji"] = yinshiyiji

                    # 判断制作小知识是否存在
                    if "制作小知识" in text:
                        zhizuozhishi_raw = h3.xpath("./following-sibling::*[1]/text()").extract()
                        zhizuozhishi = str(zhizuozhishi_raw).replace("['", "").replace("']", "").replace("[",
                        "").replace("]","").replace(" ", "").replace("\\r", "").replace("\\n", "").replace("','", "、")
                        if len(zhizuozhishi) > 1:
                            item["zhizuozhishi"] = zhizuozhishi

        li_list = response.xpath("//div[@class='ing-detail hidden']/ul[@class='plain']/li")
        for  li in li_list:
            text_raw_raw = li.xpath(".//text()").extract()
            text_raw = str(text_raw_raw)
            if "别名：" in text_raw:
                bieming = str(text_raw).replace("['","").replace("']","")
                item["bieming"] = bieming

            if "时令：" in text_raw:
                shiling = str(text_raw).replace("['","").replace("']","")
                item["shiling"] = shiling
                print(shiling)

            if "存储时间" in text_raw:
                cunchushijian = str(text_raw).replace("['", "").replace("']","")
                item["cunchushijian"] = cunchushijian


        disease_info_raw = response.xpath("//div[@class='ing-detail hidden']/ul[@class='plain']/br/following-sibling::*//text()").extract()
        disease_info = str(disease_info_raw).replace("['", "").replace("']", "").replace("[", "").replace("]",
                           "")
        item["disease_info"] = disease_info
        yield item
















        # #功效
        # gongxiao_raw = response.xpath("//div[@class='ing-detail hidden']/h3[text()='{}的功效']/following-sibling::*[1]/text()".format(item["title"])).extract()
        # gongxiao = str(gongxiao_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace("\\r",
        # "").replace("\\n","").replace(" ","").replace("','","、")
        # if len(gongxiao)>1:
        #     item["gongxiao"] = gongxiao
        #
        # else:
        #     item["gongxiao"] = ""
        #
        # #挑选
        # tiaoxuan_raw = response.xpath("//div[@class='ing-detail hidden']/h3[text()='如何挑选{}']/following-sibling::*[1]/text()".format(
        #         item["title"])).extract()
        # tiaoxuan = str(tiaoxuan_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace("\\r",
        # "").replace("\\n", "").replace(" ", "").replace("','", "\n")
        # if len(tiaoxuan) > 1:
        #     item["tiaoxuan"] = tiaoxuan
        #
        # else:
        #     item["tiaoxuan"] = ""
        #
        # #存储
        # cunchu_raw = response.xpath("//div[@class='ing-detail hidden']/h3[text()='{}的储存方法']/following-sibling::*[1]/text()".format(
        #         item["title"])).extract()
        # cunchu = str(cunchu_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace("\\r",
        #     "").replace("\\n", "").replace(" ", "").replace("','", "\n")
        # if len(cunchu) > 1:
        #     item["cunchu"] = cunchu
        #
        # else:
        #     item["cunchu"] = ""
        # print(cunchu)








