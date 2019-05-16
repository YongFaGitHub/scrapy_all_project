# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import os


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.meishichina.com']
    start_urls = ['http://www.meishichina.com/YuanLiao/#hmsr=www&hmpl=index&hmcu=magicside&hmkw=D2&hmci=D2_main']




    def parse(self, response):
        item= {}

        #大分类列标进入小分类的列表页
        div_list = response.xpath("//div[@class='category_box mt20']/div[1]/following-sibling::*")
        for div in div_list:
            big_class = div.xpath("./h3/text()").extract_first()
            item["big_class"] = big_class #大类别
            url_raw = div.xpath("./ul/li/a[text()='更多']/@href").extract_first()
            url = "http:" + url_raw
            yield Request(url,callback=self.parse_one,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_one(self,response):
        item = response.meta["item"]

        div_list = response.xpath("//div[@class='category_box mt20']/div")
        for div in div_list:
            small_class = div.xpath("./h3/text()").extract_first()

            item["small_class"] = small_class  #种类

            li_list = div.xpath("./ul/li")
            for li in li_list:
                title = li.xpath("./a/text()").extract_first()
                item["title"] = title  #具体食材
                item["img"] = 0

                url_raw = li.xpath("./a/@href").extract_first()
                if url_raw is not None:

                    url = url_raw + "useful/"
                    yield Request(url,callback=self.parse_jiazhi,meta={"item":deepcopy(item)})



    def parse_jiazhi(self,response):
        item = response.meta["item"]
        list  = []

        yingyangjiazhi_raw = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='营养价值']/../following-sibling::*[1]//text()").extract()
        yingyangjiazhi = str(yingyangjiazhi_raw).replace("['","").replace("']","").replace("[","").replace("]",
        "").replace("\\xa0","").replace(" ","").replace("','","").replace("\\n","\n").replace("\\u3000","").replace('"',"“")
        if len(yingyangjiazhi) >2:
            item["yingyangjiazhi"]  = yingyangjiazhi
        else:
            # yingyang2_raw = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='{}的营养价值']/../following-sibling::*//text()".format(item["title"])).extract()
            # yingyang2_r = str(yingyang2_raw).replace("['","").replace("']","").replace(" ","").replace("','","\n").replace("\\u3000",
            # "").replace("\\xa0","").replace("[","").replace("]","")
            # yingyang2 = '{}的营养价值'.format(item["title"]) +"\n" +yingyang2_r
            # # print(yingyang2)
            # list.append(yingyang2)
            item["yingyangjiazhi"] =""

        # print(yingyangjiazhi)

        shiyonggongxiao_raw = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='食用功效']/../following-sibling::*[1]//text()").extract()
        shiyonggongxiao = str(shiyonggongxiao_raw).replace("['","").replace("']","").replace("[","").replace("]",
        "").replace("\\xa0","").replace(" ","").replace("','","").replace("\\n","\n").replace("\\u3000","")
        if len(shiyonggongxiao) >2:
            item["shiyonggongxiao"]  = shiyonggongxiao
        else:
            item["shiyonggongxiao"] = ""
        # else:
        #     shiyongxiaoguo2_raw  = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='{}的功效与作用']/../following-sibling::*//text()".format(item["title"])).extract()
        #     shiyongxiaoguo2_r = str(shiyongxiaoguo2_raw).replace("['", "").replace("']", "").replace(" ", "").replace("','",
        #     "\n").replace("\\u3000","").replace("\\xa0", "").replace("[", "").replace("]", "")
        #     shiyongxiaoguo2 = '{}的营养价值'.format(item["title"]) + "\n" + shiyongxiaoguo2_r
        #     list.append(shiyongxiaoguo2)


        # print(shiyonggongxiao)

        shiyongrenqun_raw = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='适用人群']/../following-sibling::*[1]//text()").extract()
        shiyongrenqun = str(shiyongrenqun_raw).replace("['","").replace("']","").replace("[","").replace("]",
        "").replace("\\xa0","").replace(" ","").replace("','","").replace("\\n","\n").replace("\\u3000","")

        if len(shiyongrenqun)>2:
            item["shiyirenqun"] = shiyongrenqun
        else:
            item["shiyirenqun"] =""


            # print(shiyongrenqun)

        jinjirenqun_raw = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='禁忌人群']/../following-sibling::*[1]//text()").extract()
        jinjirenqun = str(jinjirenqun_raw).replace("['","").replace("']","").replace("[","").replace("]",
        "").replace("\\xa0","").replace(" ","").replace("','","").replace("\\n","\n").replace("\\u3000","")
        if  len(jinjirenqun) >2:
            item["jinjirenqun"] = jinjirenqun

        else:
            item["jinjirenqun"] =""


        xuangoujiqiao_raw = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='选购技巧']/../following-sibling::*[1]//text()").extract()
        xuangoujiqiao = str(xuangoujiqiao_raw).replace("['","").replace("']","").replace("[","").replace("]",
        "").replace("\\xa0","").replace(" ","").replace("','","").replace("\\n","\n").replace("\\u3000","")

        if len(xuangoujiqiao) >2:
            item["xuangoujiqiao"] = xuangoujiqiao
        else:
            item["xuangoujiqiao"] =""
        cunchu_raw = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='储存简述']/../following-sibling::*[1]//text()").extract()
        cunchu = str(cunchu_raw).replace("['","").replace("']","").replace("[","").replace("]",
        "").replace("\\xa0","").replace(" ","").replace("','","").replace("\\n","\n").replace("\\u3000","")
        if len(cunchu)>2:
            item["cunchu"] = cunchu
        else:
            item["cunchu"] = ""


        yield item








    def parse_two(self, response):
        item = response.meta["item"]
        disease_info_raw = response.xpath("//div[@class='space_left']/p//text()").extract()
        disease_info = str(disease_info_raw).replace("['", "").replace("']", "").replace(" ", "").replace("','",
                                                                                                          "").replace(
            "\\n", "\n").replace("\\xa0", "").replace("\\u3000", "").replace('"', "“")

        item["disease_info"] = disease_info
        # print(disease_info)

        p_list = response.xpath("//div[@class='blog_message']/*")
        info_s = ""
        for p in p_list:
            info_raw = p.xpath(".//text()").extract()
            info = str(info_raw).replace("['", "").replace("']", "").replace("[", "").replace("]",
                                                                                              "").replace("\\xa0",
                                                                                                          "").replace(
                " ", "").replace("','", "").replace("\\u3000", "").replace("\\n",
                                                                           "").replace('\"', '“')
            if len(info) > 1:
                info_s = info_s + info + "\n"

        if len(info_s) > 2:
            item["tiaoxuan"] = info_s

        else:
            info2_raw = response.xpath("//div[@class='blog_message']//text()").extract()
            info2 = str(info2_raw).replace("['", "").replace("']", "").replace("\\n",
                                                                               "").replace("\\xa0", "").replace(" ",
                                                                                                                "").replace(
                "','", "\n").replace("[", "").replace("]",
                                                      "").replace("\\n", "").replace("'", "").replace('\"', "“")
            # print(item["big_class"],item["small_class"],item["title"])
            # print(info2)
            if len(info2) > 2:
                item["tiaoxuan"] = info2

            else:
                item["tiaoxuan"] = ""

        yield item

        # xuangou_url_raw = response.xpath("//h2/a[text()='认识与选购']/@href").extract_first()
        # if item["a"] == 0:
        #     if xuangou_url_raw is not None:
        #         yield Request(xuangou_url_raw,callback=self.parse_three,dont_filter=True,meta={"item":deepcopy(item)})
        #
        #     else:
        #         item["disease_info"] = ""
        #         item["tiaoxuan"] = ""
        #
        # yingyang_url_raw = response.xpath("//h2/a[text()='营养功效']/@href").extract_first()
        # if item["b"] == 0:
        #     if yingyang_url_raw is not None:
        #         yield Request(yingyang_url_raw,callback=self.parse_yingyang,dont_filter=True,meta={"item":deepcopy(item)})
        #     else:
        #         item["yingyangjiazhi"] = ""
        #         item["shiyonggongxiao"] = ""
        #         item["shiyirenqun"] = ""
        #         item["jinjirenqun"] = ""
        #         item["xuangoujiqiao"] =""
        #         item["cunchu"] = ""
        #
        #
        # yield Request("https://www.meishichina.com/YuanLiao/",callback=self.parse_f,dont_filter=True,meta={"item":deepcopy(item)})




    # def parse_img(self,response):
    #     item = response.meta["item"]
    #     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    #     try:
    #         os.mkdir("I:/meishitianxia_img")
    #     except:
    #         pass
    #
    #     try:
    #         os.mkdir("I:/meishitianxia_img/{}".format(item["big_class"]))
    #     except:
    #         pass
    #
    #     try:
    #         os.mkdir("I:/meishitianxia_img/{}/{}".format(item["big_class"],item["small_class"]))
    #     except:
    #         pass
    #
    #
    #     with open("I:/meishitianxia_img/{}/{}/{}.jpg".format(item["big_class"],item["small_class"],item["title"]),"wb") as f:
    #         f.write(response.body)
    #


    # #简介，选购
    # def parse_three(self,response):
    #     item = response.meta["item"]
    #     disease_info_raw = response.xpath("//div[@class='space_left']/p/text()").extract()
    #     disease_info = str(disease_info_raw).replace("['","").replace("']","").replace(" ","").replace("','",
    #     "").replace("\\n","\n").replace("\\xa0","").replace("\\u3000","")
    #     item["disease_info"] = disease_info
    #
    #     p_list = response.xpath("//div[@class='blog_message']/*")
    #     info_s = ""
    #     for p in p_list:
    #         info_raw = p.xpath(".//text()").extract()
    #         info = str(info_raw).replace("['","").replace("']","").replace("[","").replace("]",
    #         "").replace("\\xa0","").replace(" ","").replace("','","").replace("\\u3000","")
    #         if len(info)>0:
    #             info_s = info_s + info +"\n"
    #
    #     item["tiaoxuan"] = info_s
    #     item["a"] = 1
    #
    #     yield Request(item["url"],callback=self.parse_two,dont_filter=True,meta={"item":deepcopy(item)})
    #
    #
    #
    # def parse_yingyang(self,response):
    #     item = response.meta["item"]
    #     yingyangjiazhi_raw = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='营养价值']/../following-sibling::*[1]//text()").extract()
    #     yingyangjiazhi = str(yingyangjiazhi_raw).replace("['","").replace("']","").replace("[","").replace("]",
    #     "").replace("\\xa0","").replace(" ","").replace("','","").replace("\\n","\n").replace("\\u3000","")
    #     item["yingyangjiazhi"]  = yingyangjiazhi
    #
    #     # print(yingyangjiazhi)
    #
    #     shiyonggongxiao_raw = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='食用功效']/../following-sibling::*[1]//text()").extract()
    #     shiyonggongxiao = str(shiyonggongxiao_raw).replace("['","").replace("']","").replace("[","").replace("]",
    #     "").replace("\\xa0","").replace(" ","").replace("','","").replace("\\n","\n").replace("\\u3000","")
    #     item["shiyonggongxiao"]  = shiyonggongxiao
    #     # print(shiyonggongxiao)
    #
    #     shiyongrenqun_raw = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='适用人群']/../following-sibling::*[1]//text()").extract()
    #     shiyongrenqun = str(shiyongrenqun_raw).replace("['","").replace("']","").replace("[","").replace("]",
    #     "").replace("\\xa0","").replace(" ","").replace("','","").replace("\\n","\n").replace("\\u3000","")
    #     item["shiyirenqun"] = shiyongrenqun
    #     # print(shiyongrenqun)
    #
    #     jinjirenqun_raw = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='禁忌人群']/../following-sibling::*[1]//text()").extract()
    #     jinjirenqun = str(jinjirenqun_raw).replace("['","").replace("']","").replace("[","").replace("]",
    #     "").replace("\\xa0","").replace(" ","").replace("','","").replace("\\n","\n").replace("\\u3000","")
    #     item["jinjirenqun"] = jinjirenqun
    #
    #     xuangoujiqiao_raw = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='选购技巧']/../following-sibling::*[1]//text()").extract()
    #     xuangoujiqiao = str(xuangoujiqiao_raw).replace("['","").replace("']","").replace("[","").replace("]",
    #     "").replace("\\xa0","").replace(" ","").replace("','","").replace("\\n","\n").replace("\\u3000","")
    #     item["xuangoujiqiao"] = xuangoujiqiao
    #
    #     cunchu_raw = response.xpath("//div[@class='category_usebox mt10 clear']/div/p/strong[text()='储存简述']/../following-sibling::*[1]//text()").extract()
    #     cunchu = str(cunchu_raw).replace("['","").replace("']","").replace("[","").replace("]",
    #     "").replace("\\xa0","").replace(" ","").replace("','","").replace("\\n","\n").replace("\\u3000","")
    #     item["cunchu"] = cunchu
    #
    #
    #     item["b"] = 1
    #     yield Request(item["url"],callback=self.parse_two,dont_filter=True,meta={"item":deepcopy(item)})
    #
    #
    #
    #
    # def parse_f(self,response):
    #
    #     item = response.meta["item"]
    #     if len(list(item.keys())) == 16:
    #         yield item
    #         # print(item)






 # def parse(self, response):
    #     item = {}
    #     #大分类列标进入小分类的列表页
    #     div_list = response.xpath("//div[@class='category_box mt20']/div[1]/following-sibling::*")
    #     for div in div_list:
    #         big_class = div.xpath("./h3/text()").extract_first()
    #         item["big_class"] = big_class #大类别
    #         url_raw = div.xpath("./ul/li/a[text()='更多']/@href").extract_first()
    #         url = "http:" + url_raw
    #         yield Request(url,callback=self.parse_one,meta={"item":deepcopy(item)})
    #
    # def parse_one(self,response):
    #     item = response.meta["item"]
    #     div_list = response.xpath("//div[@class='category_box mt20']/div")
    #     for div in div_list:
    #         small_class = div.xpath("./h3/text()").extract_first()
    #
    #         item["small_class"] = small_class  #种类
    #
    #         li_list = div.xpath("./ul/li")
    #         for li in li_list:
    #             title = li.xpath("./a/text()").extract_first()
    #             item["title"] = title  #具体食材
    #
    #             url_raw = li.xpath("./a/@href").extract_first()
    #             item["url"] = url_raw
    #             # with open("H:/pycharmproject/project/meishitianxia/meishitianxia/spiders/url.txt","a+",encoding="utf-8") as f:
    #             #     f.write(url)
    #             #     f.write("\n")
    #
    #             url = url_raw +"tiyan/"
    #             yield Request(url,callback=self.parse_disease,meta={"item":deepcopy(item)})
    #
    # def parse_disease(self,response):
    #     item = response.meta["item"]
    #
    #     disease_info_raw = response.xpath("//div[@class='space_left']/p/text()").extract()
    #     disease_info = str(disease_info_raw).replace("['","").replace("']","").replace(" ","").replace("','",
    #     "").replace("\\n","\n").replace("\\xa0","").replace("\\u3000","")
    #     item["disease_info"] = disease_info
    #
    #
    #










