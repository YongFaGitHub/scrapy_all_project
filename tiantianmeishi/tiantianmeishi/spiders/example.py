# -*- coding: utf-8 -*-
import scrapy
from  scrapy import Request
from copy import deepcopy
import time
import os

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['ttmeishi.com/']
    start_urls = ['http://www.ttmeishi.com/YuanLiao/']


    def parse(self, response):
        # self.conn = connect(host='127.0.0.1', port=3306, database='tiantianmeishi', user='root', password='jing1995',
        #                charset='utf8')
        # self.cs1 = self.conn.cursor()
        div_list = response.xpath("//div[@class='yl_leibie']")
        for div in div_list:
            item = {}
            a_s = div.xpath("./div/strong/a")
            big_class = a_s.xpath("./text()").extract_first()
            item["big_class"] = big_class

            url_raw = a_s.xpath("./@href").extract_first()
            url = "http://www.ttmeishi.com" + url_raw
            # print(url)

            yield Request(url,callback=self.parse_liebiao,meta={"item":deepcopy(item)},dont_filter=True)

    def parse_liebiao(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@class='yl_leibie']/ul/li")
        for li in li_list[:-2]:
            title  = li.xpath("./a/text()").extract_first()
            item["title"] = title
            # yield item

    #
            url_raw = li.xpath("./a/@href").extract_first()
            url = "http://www.ttmeishi.com" + url_raw
            item["url"]  = url
            # print(url)
            yield Request(url,callback=self.parse_disease,meta={"item":deepcopy(item)},dont_filter=True)

    def parse_disease(self,response):
        item = response.meta["item"]
        url_raw = response.xpath("//div[@class='sbox']/img/@src").extract_first()
        if url_raw is not None:
            url = "http://www.ttmeishi.com" + url_raw
            with open("H:/pycharmproject/deal_data/tiantianmeishi/img_url/{}.csv".format(item["title"]),"w",encoding="utf-8") as f:
                f.write(url)


            # yield Request(url,callback=self.img_data,meta={"item":deepcopy(item)},dont_filter=True)

    def img_data(self,response):
        item = response.meta["item"]
        try:
            os.mkdir("I:/tiantianmeishi_img/{}".format(item["big_class"]))

        except:
            pass


        with open("I:/tiantianmeishi_img/{}/{}.jpg".format(item["big_class"],item["title"]),"wb") as f:
            f.write(response.body)



        # try:
        #     bieming_raw = response.xpath("//div[@class='sidebar']/div[1]/h3//text()").extract()
        #     bieming = str(bieming_raw)
        #     if "别名" in bieming:
        #         bieming = bieming.replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
        #         "").replace("','","")
        #         item["bieming"] = bieming
        #     else:
        #         item["bieming"] = ""
        #
        # except:
        #     item["bieming"] = ""

        # url_raw = response.xpath("//div[@class='sidebar']/div/ul/li/a[text()='{}的小贴士']/@href".format(item["title"])).extract_first()
    #     if url_raw is not None:
    #         url = item["url"] + url_raw
    #         yield Request(url,callback=self.parse_jieshao,dont_filter=True,meta={"item":deepcopy(item)})
    #     else:
    #         item["disease_info"] =""
    #         # yield item
    #
    #
    # def parse_jieshao(self,response):
    #     item = response.meta["item"]
    #     p_list = response.xpath("//div[@class='content']/p")
    #     info_s = ""
    #     for p in p_list:
    #         info_raw = p.xpath("./text()").extract()
    #         info = str(info_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace("\\r",
    #         "").replace("\\n","").replace("\\t","").replace("\\u3000","").replace("\\xa0","").replace(" ",
    #         "").replace("','","").replace('"',"“").replace("'","‘")
    #         if len(info) >2:
    #             info_s = info_s + info +"\n"
    #
    #     item["disease_info"] = info_s
    #     print(info_s)
    #
    #     with open("H:/pycharmproject/deal_data/tiantianmeishi/xiaotieshi/{}.csv".format(item["title"]),"w",encoding="utf-8") as f:
    #         f.write(info_s)
    #
    #
    #
    #     # yield item
    #     # time.sleep(2)
    #     # print(item)
    #     #
    #     #
    #     #
    #     # self.count = self.cs1.execute('update tiantianmeishisc set yingyangfenxi="{}" where title="{}"'.format(item["disease_info"],
    #     # item["title"]))
    #     # self.cs1.close()
    #     # self.conn.commit()
    #     # self.conn.close()
    #

















    # def parse(self, response):
    #     div_list = response.xpath("//div[@class='yl_leibie']")
    #     for div in div_list:
    #         url_raw = div.xpath("./ul/li/a[text()='更多']/@href").extract_first()
    #         url = "http://www.ttmeishi.com" + url_raw
    #         print(url)
    #         yield Request(url,callback=self.parse_liebiao,dont_filter=True)
    #
    # def parse_liebiao(self,response):
    #     item = {}
    #     small_class = response.xpath("//div[@class='yl_leibie']/div/strong/a/text()").extract_first()
    #     item["small_class"] = small_class
    #     #食材的链接地址
    #     li_list = response.xpath("//div[@class='yl_leibie']//ul[@class='yl_ul']/li")
    #     for li in li_list[:-2]:
    #     #     url_raw = li.xpath("./a/@href").extract_first()
    #     #     url = "http://www.ttmeishi.com" + url_raw
    #     # # print(url,"@@@@@@@@@@@@@@@@@@@@@@@@@@2")
    #     #     item["url"] = url
    #
    #
    #
    #     #食材名称
    #         title = li.xpath("./a/text()").extract_first()
    #
    #         item["title"] = title
    #         yield item

    #     #判断条件
    #     item["a"] = 0
    #     item["b"] = 0
    #     item["c"] = 0
    #     item["d"] = 0
    #     item["e"] = 0
    #     item["f"] = 0
    #     #食材所属类别

    #     yield Request(url,callback=self.parse_disease,dont_filter=True,meta={"item":deepcopy(item)})
    #
    # def parse_disease(self,response):
    #     item = response.meta["item"]
    #     #别名的判断
    #     if item["a"] == 0:
    #         item["bieming"] = ""
    #         try:
    #             bieming_raw = response.xpath("//div[@class='sidebar']/div[1]/h3//text()").extract()
    #             bieming = str(bieming_raw)
    #             if "别名" in bieming:
    #                 item["bieming"] = bieming
    #
    #         except:
    #             item["bieming"] = ""
    #
    #         item["a"] = 1
    #
    #     #详细信息的获取
    #
    #
    #     li_list = response.xpath("//div[@class='sidebar']/div/ul/li")
    #
    #     for li in li_list:
    #         text_raw = li.xpath("./a/text()").extract()
    #         text = str(text_raw)
    #         url_raw = li.xpath("./a/@href").extract_first()
    #         url = item["url"] + url_raw
    #
    #         # 判断食材的介绍
    #
    #         if "介绍" in text :
    #             if item["b"] == 0:
    #
    #                 yield Request(url, callback=self.parse_jieshao, meta={"item": deepcopy(item)},
    #                               dont_filter=True)
    #
    #         #判断食材的营养
    #     #
    #         if "营养" in text:
    #             if item["c"] == 0:
    #                 yield Request(url, callback=self.parse_yingyang,dont_filter=True,meta={"item":deepcopy(item)})
    #
    #         #食材的适合人群
    #
    #         if "适合人群" in text :
    #             if item["d"] == 0:
    #
    #                 yield Request(url, callback=self.parse_shiherenqun,meta={"item":deepcopy(item)},dont_filter=True)
    #
    #         #食材作用
    #
    #         if "食疗作用" in text :
    #             if  item["e"] == 0:
    #
    #                 yield Request(url, callback=self.parse_shiliaozuoyong,meta={"item":deepcopy(item)},dont_filter=True)
    #
    #         #食材的小贴士
    #
    #         if "小贴士" in text :
    #             if item["f"] == 0:
    #                 yield Request(url, callback=self.parse_xiaotieshi,meta={"item":deepcopy(item)},dont_filter=True)
    #
    #
    #     # yield Request("http://www.ttmeishi.com/YuanLiao",callback=self.parse_f,dont_filter=True,meta={"item":deepcopy(item)})
    #
    #
    # # 判断食材的介绍
    # def parse_jieshao(self,response):
    #     item = response.meta["item"]
    #     item["b"] = 1
    #     p_list = response.xpath("//div[@class='content']/p")
    #     info_s = ""
    #     for p in p_list:
    #         info_raw = p.xpath("./text()").extract()
    #         info = str(info_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace("\\r",
    #         "").replace("\\n","").replace("\\t","").replace("\\u3000","").replace("\\xa0","").replace(" ",
    #         "").replace("','","")
    #         if len(info) >2:
    #             info_s = info_s + info +"\n"
    #     item["disease_info"] = info_s
    #     # print(item)
    #     yield Request(item["url"],callback=self.parse_disease,dont_filter=True,meta={"item": deepcopy(item)})
    #
    # # 判断食材的营养
    # def parse_yingyang(self, response):
    #     item = response.meta["item"]
    #     item["c"] = 1
    #     p_list = response.xpath("//div[@class='content']/p")
    #     info_s = ""
    #     for p in p_list:
    #         info_raw = p.xpath("./text()").extract()
    #         info = str(info_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace("\\r",
    #         "").replace("\\n", "").replace("\\t", "").replace("\\u3000", "").replace("\\xa0", "").replace(" ",
    #         "").replace("','", "")
    #         if len(info) > 2:
    #             info_s = info_s + info + "\n"
    #     item["yingyang"] = info_s
    #     # print(item)
    #     yield Request(item["url"], callback=self.parse_disease, dont_filter=True, meta={"item": deepcopy(item)})
    #
    # # 食材的适合人群
    # def parse_shiherenqun(self, response):
    #     item = response.meta["item"]
    #     item["d"] = 1
    #     p_list = response.xpath("//div[@class='content']/p")
    #     info_s = ""
    #     for p in p_list:
    #         info_raw = p.xpath("./text()").extract()
    #         info = str(info_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace("\\r",
    #                                                                                                            "").replace(
    #             "\\n", "").replace("\\t", "").replace("\\u3000", "").replace("\\xa0", "").replace(" ",
    #                                                                                               "").replace("','", "")
    #         if len(info) > 2:
    #             info_s = info_s + info + "\n"
    #     item["shiherenqun"] = info_s
    #     yield Request(item["url"], callback=self.parse_disease, dont_filter=True, meta={"item": deepcopy(item)})
    #
    # # 食材作用
    # def parse_shiliaozuoyong(self, response):
    #     item = response.meta["item"]
    #     item["e"] = 1
    #     p_list = response.xpath("//div[@class='content']/p")
    #     info_s = ""
    #     for p in p_list:
    #         info_raw = p.xpath("./text()").extract()
    #         info = str(info_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace("\\r",
    #                                                                                                            "").replace(
    #             "\\n", "").replace("\\t", "").replace("\\u3000", "").replace("\\xa0", "").replace(" ",
    #                                                                                               "").replace("','", "")
    #         if len(info) > 2:
    #             info_s = info_s + info + "\n"
    #     item["shicaizuoyong"] = info_s
    #     yield Request(item["url"], callback=self.parse_disease, dont_filter=True, meta={"item": deepcopy(item)})
    #
    # # 食材的小贴士
    # def parse_xiaotieshi(self, response):
    #     item = response.meta["item"]
    #     item["f"] = 1
    #     p_list = response.xpath("//div[@class='content']/p")
    #     info_s = ""
    #     for p in p_list:
    #         info_raw = p.xpath("./text()").extract()
    #         info = str(info_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace("\\r",
    #                                                                                                            "").replace(
    #             "\\n", "").replace("\\t", "").replace("\\u3000", "").replace("\\xa0", "").replace(" ",
    #                                                                                               "").replace("','", "")
    #         if len(info) > 2:
    #             info_s = info_s + info + "\n"
    #     if len(info_s) >1:
    #         item["xiaotieshi"] = info_s
    #     else:
    #         item["xiaotieshi"] = ""
    #     # print(info_s)
    #     yield Request(item["url"], callback=self.parse_disease, dont_filter=True, meta={"item": deepcopy(item)})
    #
    # #最后的数据导出
    # def parse_f(self,response):
    #     item = response.meta["item"]
    #
    #     # if len(list(item.keys())) == 15:
    #         # print(item)
            # yield item
