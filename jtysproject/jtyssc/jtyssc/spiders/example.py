# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from scrapy.http import Request
import os
import csv

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['ask.familydoctor.com']
    start_urls = ["https://sck.familydoctor.com.cn/category_0_0_0_0.html"]



    #首地址进入
    def parse(self,response):
        item = {}
        li_list = response.xpath("//div[@class='select-food']/ul[@id='side-cate']/li")
        for li in li_list:
            big_class_raw = li.xpath("./b/a/text()").extract_first()
            big_class = str(big_class_raw).replace("/","_")
            item["big_class"] = big_class

            a_list = li.xpath("./p/a")
            for a in a_list:
                small_class_raw = a.xpath("./text()").extract_first()
                small_class = str(small_class_raw).replace("/","_")
                item["small_class"] = small_class

                url_raw = a.xpath("./@href").extract_first()
                url_start = url_raw.replace("_1.html","")
                for i in range(1,50):
                    url = url_start +"_{}.html".format(str(i))

                    yield Request(url,callback=self.parse_f,dont_filter=True,meta={"item":deepcopy(item)})


    def parse_f(self, response):
        item = response.meta["item"]
        dl_list = response.xpath("//div[@class='foods-hot']/dl")
        for dl in dl_list:
            title_raw = dl.xpath("./dd/span/a/text()").extract_first()
            title = str(title_raw).replace("/","_")
            item["title"] = title

            img = dl.xpath("./dt/a/img/@src").extract_first()
            if img == "http://img.familydoctor.com.cn/images/ku/disease_default.jpg":
                item["title_img_url"] = ""
            else:
                item["title_img_url"] = img

                yield Request(img,callback=self.parse_img,dont_filter=True,meta={"item":deepcopy(item)})

            disease_url = dl.xpath("./dd/span/a/@href").extract_first()
            yield Request(disease_url,callback=self.parse_one,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_img(self,response):
        item = response.meta["item"]
        try:
            os.mkdir("I:/img/{}".format(item["big_class"]))
        except:
            pass
        try:
            os.mkdir("I:/img/{}/{}".format(item["big_class"],item["small_class"]))
        except:
            pass
        with open("I:/img/{}/{}/{}.jpeg".format(item["big_class"],item["small_class"],item["title"]),"wb") as f:
            f.write(response.body)



    #功效简介
    def parse_one(self,response):
        #主要功效
        item = response.meta["item"]
        gongxiao_disease_raw = response.xpath("//div[@class='summary-fun-head']/p//text()").extract()
        gongxiao_disease = str(gongxiao_disease_raw).replace(" ","").replace("\\r","").replace("\\n",
        "").replace("','","").replace("|","、").replace("['","").replace("']","").replace("[",
        "").replace("]","").replace("\\u3000","").replace(" ","").replace("\\xa0","")
        if len(gongxiao_disease)>1:
            item["gongxiao_disease"] = gongxiao_disease
        else:
            item["gongxiao_disease"] = ""

        #营养功效的地址
        url_info = response.xpath("//div[@class='summary-nav']/a[text()='营养功效']/@href").extract_first()
        yield Request(url_info,callback=self.parse_two,dont_filter=True,meta={"item":deepcopy(item)})

        # print(gongxiao_disease)

    #营养功效，与营养价值
    def parse_two(self,response):
        #营养功效
        item = response.meta["item"]
        #功效与作用
        gongxiaozuoyong_raw_lis= response.xpath("//div[@class='cont-com cont-fl fl']/div[1]/div[1]/p/text()").extract()
        gongxiaozuoyong_raw_li = str(gongxiaozuoyong_raw_lis).replace("[","").replace("]","")

        if len(gongxiaozuoyong_raw_li)>1 :
            gongxiaozuoyong_raw_list = response.xpath("//div[@class='cont-com cont-fl fl']/div[1]/div[1]/*")
            gongxiaozuoyong_s = ""
            for gongxiaozuoyong_raws in gongxiaozuoyong_raw_list:
                gongxiaozuoyong_raw = gongxiaozuoyong_raws.xpath(".//text()").extract()
                gongxiaozuoyong = str(gongxiaozuoyong_raw).replace("['","").replace("']","").replace("[",
                "").replace("[","").replace("\\r","").replace("\\n","").replace("查看更多","").replace("\\u3000",
                "")
                # print(gongxiaozuoyong)
                if len(gongxiaozuoyong)>1:
                    gongxiaozuoyong_s = gongxiaozuoyong_s + gongxiaozuoyong +"\n"

            item["gongxiaozuoyong"] = gongxiaozuoyong_s

        else:
            item["gongxiaozuoyong"] =""

            #营养价值
        yingyangjiazhi_raw_list = response.xpath("//div[@class='cont-com cont-fl fl']/div[1]/div[2]/*")
        yingyangjiazhi_s = ""
        for yingyangjiazhi_raws in yingyangjiazhi_raw_list:
            yingyangjiazhi_raw = yingyangjiazhi_raws.xpath(".//text()").extract()
            yingyangjiazhi = str(yingyangjiazhi_raw).replace("['", "").replace("']", "").replace("[",
            "").replace("[","").replace("\\r", "").replace("\\n", "").replace("查看更多", "").replace("\\u3000",
            "")
            if len(yingyangjiazhi) > 1:
                yingyangjiazhi_s = yingyangjiazhi_s + yingyangjiazhi + "\n"

        item["yingyangjiazhi"] = yingyangjiazhi_s

        url_info = response.xpath("//div[@class='summary-nav']/a[text()='基本介绍']/@href").extract_first()
        yield Request(url_info, callback=self.parse_three, dont_filter=True, meta={"item": deepcopy(item)})

    #简介，内容
    def parse_three(self,response):
        item = response.meta["item"]
        #食材简介
        info_list = response.xpath("//div[@class='introduce-info']/*")
        info_s = ""
        for info in info_list:
            info_raw = info.xpath(".//text()").extract()
            info_f = str(info_raw).replace("['","").replace("']","").replace("[","").replace("]",
            "").replace("\\u3000","").replace("\\r","").replace("\\n","").replace("\\t","").replace("\\u3000","").replace(" ",
        "").replace("','","").replace("\\xa0","")
            if len(info_f)>1:
                info_s = info_s + info_f +"\n"

        item["disease_info"]  = info_s

        #别名
        title2_raw = response.xpath("//div[@class='summary-head']/dl/dd/h4/i/text()").extract_first()
        title2 = str(title2_raw).replace(")","").replace("(","").replace("None","")
        if title2 is not None:
            item["title2"] = title2
        else:
            item["title2"] =""

        url_info = response.xpath("//div[@class='summary-nav']/a[text()='适宜人群']/@href").extract_first()
        yield Request(url_info, callback=self.parse_four, dont_filter=True, meta={"item": deepcopy(item)})

    #适宜人群
    def parse_four(self,response):
        item = response.meta["item"]

        gongxiaozuoyong_raw_lis = response.xpath("//div[@class='suitable-show']/p/text()").extract()
        gongxiaozuoyong_raw_li = str(gongxiaozuoyong_raw_lis).replace("[", "").replace("]", "")

        if len(gongxiaozuoyong_raw_li) > 1:

            info_list = response.xpath("//div[@class='suitable-show']/*")
            info_s = ""
            for info in info_list:
                info_raw = info.xpath(".//text()").extract()
                info_f = str(info_raw).replace("['","").replace("']","").replace("[","").replace("]",
                "").replace("\\r","").replace("\\n","").replace("\\t","").replace("\\u3000","").replace(" ",
            "").replace("','","").replace("\\xa0","")
                if len(info_f)>1:
                    info_s = info_s +info_f +"\n"

            # print(info_s)
            if len(info_s)>1:
                item["shiyirenqun"] = info_s

        else:
            item["shiyirenqun"] =""

        url_info = response.xpath("//div[@class='summary-nav']/a[text()='不适宜人群']/@href").extract_first()
        yield Request(url_info, callback=self.parse_five, dont_filter=True, meta={"item": deepcopy(item)})

    #不适宜人群
    def parse_five(self,response):
        item = response.meta["item"]
        info1_raw  = response.xpath("//div[@class='improper-info']/h4/text()").extract()
        info1 = str(info1_raw).replace("['","").replace("']","").replace("[","").replace("]",
        "").replace("\\r","").replace("\\n","").replace("\\t","").replace("\\u3000","").replace(" ",
        "").replace("','","").replace("\\xa0","")

        info2_raw = response.xpath("//div[@class='improper-info']/div[1]//text()").extract()
        info2 = str(info2_raw).replace("['","").replace("']","").replace("[","").replace("]",
        "").replace("\\n","").replace("\\r","").replace("\\t","").replace("\\u3000","").replace(" ",
        "").replace("','","").replace("\\xa0","")
        if len(info2)>1:
            info = info1 + "\n" +info2
            item["bushiyirenqun"] = info

        else:
            item["bushiyirenqun"] =""
            # print(info)
        url_info = response.xpath("//div[@class='summary-nav']/a[text()='食物相克']/@href").extract_first()
        yield Request(url_info, callback=self.parse_six, dont_filter=True, meta={"item": deepcopy(item)})

    #食物相克
    def parse_six(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@class='summary-foods summary-taboo summary-top']/ul/li")

        info_s = ""
        for li in li_list:
            dt_list_raw = li.xpath("./span//text()").extract()
            dt_list=  str(dt_list_raw).replace("['","").replace("']","").replace("[","").replace("]",
            "").replace(" ","").replace("','","").replace("\\r","").replace("\\n","").replace("\\t","")

            em_raw = li.xpath("./em/text()").extract()
            em = str(em_raw).replace("['","").replace("']","").replace("[","").replace("]",
            "").replace(" ","").replace("','","").replace("\\r","").replace("\\n","").replace("\\t","")
            info_one = dt_list + "：" + em
            info_s = info_s + info_one +"\n"
        if len(info_s)>1:
            item["shiwuxiangke"] = info_s
        else:
            item["shiwuxiangke"] = ""

        url_info = response.xpath("//div[@class='summary-nav']/a[text()='食物搭配']/@href").extract_first()
        yield Request(url_info, callback=self.parse_seven, dont_filter=True, meta={"item": deepcopy(item)})

    def parse_seven(self,response):
        item = response.meta["item"]
        #与什么搭配好吃
        fun_info_show_raw = response.xpath("//p[@class='fun-info-show']//text()").extract()
        fun_info_show = str(fun_info_show_raw).replace("['","").replace("']","").replace("[","").replace("]",
        "").replace("\\r","").replace("\\n","").replace("\\t","")
        fun_info = fun_info_show.split("：")

        if len(fun_info[1]) != 0:
            item["fun_info_show"] = fun_info_show
        else:
            item["fun_info_show"] = ""

        #与其他食物搭配具体有什么好处
        li_list = response.xpath("//div[@class='summary-foods summary-top']/ul/li")
        info_s = ""
        for li in li_list:
            dt_list_raw = li.xpath("./span//text()").extract()
            dt_list = str(dt_list_raw).replace("['", "").replace("']", "").replace("[", "").replace("]",
            "").replace(" ","").replace("','", "").replace("\\r","").replace("\\n","").replace("\\t","")

            em_raw = li.xpath("./em/text()").extract()
            em = str(em_raw).replace("['", "").replace("']", "").replace("[", "").replace("]",
            "").replace(" ", "").replace("','", "").replace("\\r","").replace("\\n","").replace("\\t","")
            info_one = dt_list + "：" + em
            info_s = info_s + info_one + "\n"

        if len(info_s) >1:

            item["fun_info_show2"] = info_s
        else:
            item["fun_info_show2"] =""
        url_info = response.xpath("//div[@class='summary-nav']/a[text()='如何挑选']/@href").extract_first()
        yield Request(url_info, callback=self.parse_night, dont_filter=True, meta={"item": deepcopy(item)})

    def parse_night(self,response):
        item = response.meta["item"]

        #挑选辨别方法
        bianbie_raw  = response.xpath("//div[@class='select-info']/p[1]/text()").extract()
        bianbie = str(bianbie_raw).replace("['","").replace("']","").replace("[","").replace("]",
        "").replace("\\u3000","").replace("\\r","").replace("\\n","").replace("\\t","")
        if len(bianbie)>1:
            item["bianbie"] = bianbie

        else:
            item["bianbie"] = ""

        #存储方法
        cunchu_raw = response.xpath("//div[@class='select-info']/p[2]/text()").extract()
        cunchu = str(cunchu_raw).replace("['","").replace("']","").replace("[","").replace("]",
        "").replace("\\u3000","").replace("\\r","").replace("\\n","").replace("\\t","")
        if len(cunchu) >1:
            item["cunchu"] = cunchu
        else:
            item["cunchu"] = ""


        # print(item)
        yield item

























    # def parse(self, response):
    #     dl_list = response.xpath("//div[@class='foods-hot']/dl/dd/div[@class='btn-list']")
    #     for dl in dl_list:
    #         url = dl.xpath("./a[text()='营养功效']/@href").extract_first()
    #         # print(url_list)
    #         yield Request(url,callback=self.parse_one,dont_filter=True)
    #
    #     next_url = response.xpath("//div[@class='pager']/a[text()='下页']/@href").extract_first()
    #     yield Request(next_url,callback=self.parse,dont_filter=True)
    #
    #
    # def parse_one(self,response):
    #     item = {}
    #     #营养功效
    #     nutrition_com_list = response.xpath("//div[@class='nutrition-com']/*")
    #     nutrition_s = ""
    #     for nutrition in nutrition_com_list:
    #         nutrition_com_raw = nutrition.xpath(".//text()").extract()
    #         nutrition_com = str(nutrition_com_raw).replace("\\r\\n","").replace(" ","").replace("'',","").replace("'",
    #         "").replace(",,","").replace("。,","。").replace("\\xa0","").replace("\\u3000","").replace("[","").replace("]","")
    #         if len(nutrition_com) >1:
    #             nutrition_s = nutrition_s + nutrition_com +"\n"
    #
    #     item["nutrition_com"] = nutrition_s
    #     # print(item)
    #     title_raw =  response.xpath("//div[@class='summary-head']/dl/dd/h4/text()").extract_first()
    #     title = str(title_raw)
    #     item["title"] = title
    #
    #     title2_raw = response.xpath("//div[@class='summary-head']/dl/dd/h4/i/text()").extract_first()
    #     title2 = str(title2_raw).replace(")","").replace("(","")
    #     item["title2"] = title2
    #
    #
    #     url  = response.xpath("//div[@class='summary-head']/dl/dd/a/@href").extract_first()
    #     yield Request(url,callback=self.parse_two,meta={"item": deepcopy(item)},dont_filter=True)
    #
    #
    # def parse_two(self,response):
    #     item = response.meta["item"]
    #     #基本介绍
    #     # print(item)
    #     introduce_info_raw = response.xpath("//div[@class='introduce-info']//text()").extract()
    #     introduce_info = str(introduce_info_raw).replace("\\r\\n","").replace(" ","").replace("'',","").replace("'",
    #     "").replace(",,","").replace("。,","。").replace("\\xa0","").replace("\\u3000","").replace("[","").replace("]",
    #     "")
    #
    #     item["introduce_info"] = introduce_info
    #     # yield item
    #     print(item["nutrition_com"] )