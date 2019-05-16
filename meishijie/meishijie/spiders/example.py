# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import os


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.meishij.net/']
    start_urls = ['http://www.meishij.net/shicai/']

    def parse(self, response):
        item = {}
        for i in range(1,5):
            dl_list = response.xpath("//div[@class='other_c listnav_con clearfix']/dl[{}]".format(i))
            for dl in dl_list:
                big_class = dl.xpath("./dt/text()").extract_first()
                item["big_class"] = big_class  #大类别

                dd_list = dl.xpath("./dd")
                for dd in dd_list:
                    small_class = dd.xpath("./a/text()").extract_first()
                    item["small_class"] = small_class  #中类别

                    url = dd.xpath("./a/@href").extract_first()
                    print(url)
                    yield Request(url,callback=self.parse_one,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_one(self,response):
        item = response.meta["item"]
        # print("###############")
        a_list = response.xpath("//dd[@class='clearfix']/a")
        for a in a_list:
            big_title = a.xpath("./text()").extract_first()
            item["big_title"] = big_title  #食材属类

            url = a.xpath("./@href").extract_first()
            yield Request(url,callback=self.parse_two,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_two(self,response):
        item = response.meta["item"]
        div_list  = response.xpath("//div[@class='listtyle1_list clearfix']/div")
        for div in div_list:
            title = div.xpath("./div[@class='img']/a/@title").extract_first()  #食材名称
            item["title"] = title
            img_url = div.xpath("./div[@class='img']/a/img/@src").extract_first()   #图片地址
            url = div.xpath("./div[@class='img']/a/@href").extract_first() #食材详情地址

            yield Request(img_url,callback=self.parse_img,dont_filter=True,meta={"item":deepcopy(item)}) #图片存储

            yield Request(url,callback=self.parse_disease,dont_filter=True,meta={"item":deepcopy(item)}) #处理详情

    #保存图片到本地
    def parse_img(self,response):
        item = response.meta["item"]
        try:
            os.mkdir("I:/meishijie")
        except:
            pass

        try:
            os.mkdir("I:/meishijie/{}".format(item["big_class"]))
        except:
            pass

        try:
            os.mkdir("I:/meishijie/{}/{}".format(item["big_class"],item["small_class"]))

        except:
            pass

        try:
            os.mkdir("I:/meishijie/{}/{}/{}".format(item["big_class"],item["small_class"],item["big_title"]))

        except:
            pass

        with open("I:/meishijie/{}/{}/{}/{}.jpg".format(item["big_class"],item["small_class"],item["big_title"],item["title"]),"wb") as f:
            f.write(response.body)





    #处理详情页面
    def parse_disease(self,response):
        item = response.meta["item"]

        info_raw  = response.xpath("//div[@class='sc_header_con1']/p[@class='p2']//text()").extract()
        info = str(info_raw).replace("\\t\\t\\t","|")
        print(info)







