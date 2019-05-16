# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import os

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['tag.120ask.com/']
    start_urls = ['http://tag.120ask.com/zhengzhuang/ks/nk.html']

    def parse(self, response):
        #科室
        # print("@@@@@@@@@@@@@@@@@2")
        item = {}
        li_list = response.xpath("//ul[@class='p_chazhaoul']/li")
        for li in li_list:
            big_class=li.xpath("./div[1]/a/@title").extract_first()
            item["big_class"] = big_class
            url_raw = li.xpath("./div[1]/a/@href").extract_first()
            url = "http://tag.120ask.com" + url_raw
            # print(url,"@@@@@@@@@@@@@@@@@@@@@@")
            # print(url)
            #进入每一个科室的列表
            yield Request(url,callback=self.parse_liebiao,dont_filter=True,meta={"item":deepcopy(item)})
    #

    def parse_liebiao(self,response):
        item = response.meta["item"]
        ul_list = response.xpath("//div[@class='w_neike clears']/ul")
        for ul in ul_list:
            li_list  = ul.xpath("./li")
            for li in li_list:
                title = li.xpath("./a/@title").extract_first()
                item["title"] = title
                url_raw = li.xpath("./a/@href").extract_first()
                url_data = "http://tag.120ask.com" + url_raw
                item["url"] = url_data
                # print(url_data)
                url = url_data + "gaishu/"
                yield Request(url_data, callback=self.parse_disease, dont_filter=True, meta={"item": deepcopy(item)})
    #详情
    def parse_disease(self,response):
        item = response.meta["item"]
        img_url_raw = response.xpath("//dl[@class='p_sibox1dl clears']/dt/a/img/@src").extract_first()
        img_url = "http:" + img_url_raw
        item["img_url"] = img_url
        yield Request(img_url,callback=self.img_cun, dont_filter=True, meta={"item": deepcopy(item)})

    def img_cun(self,response):
        item = response.meta["item"]

        try: os.mkdir("I:/症状图片/ask120/{}".format(item["big_class"]))
        except:pass

        with open("I:/症状图片/ask120/{}/{}.png".format(item["big_class"],item["title"]),"wb") as f :
            f.write(response.body)

        # yield item
        with open("H:/pycharmproject/project/ask120/zhengzhuangku/zhengzhuangku/spiders/img_url.txt","a+",encoding="utf-8") as f:
            f.write(item["title"])
            f.write("、")
            f.write(item["img_url"])
            f.write("\n")





        # print(item)
        # p_s = ""
        # p_list  = response.xpath("//div[@class='p_cleftartbox']/p")
        # for p in p_list:
        #     p_raw = p.xpath(".//text()").extract()
        #     p_info = str(p_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
        #     "").replace("\\u3000","").replace("','","").replace("\\xa0","").replace("\\n","").replace("\\r",
        #     "").replace("\\t","")
        #     if len(p_info)>1:
        #         p_s = p_s + p_info + "\n"
        # # print(p_s)
        # item["disease"] = p_s
        #
        # url = item["url"] + "bingyin/"
        # yield Request(url,callback=self.parse_bingyin ,dont_filter=True, meta={"item": deepcopy(item)})
    #病因
    def parse_bingyin(self,response):
        item = response.meta["item"]
        p_s = ""
        p_list = response.xpath("//div[@class='p_cleftartbox']/p")
        for p in p_list:
            p_raw = p.xpath(".//text()").extract()
            p_info = str(p_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace(" ",
            "").replace("\\u3000", "").replace("','", "").replace("\\xa0", "").replace("\\n","").replace("\\r",
            "").replace("\\t","")
            if len(p_info) > 1:
                p_s = p_s + p_info + "\n"
        item["bingyin"] = p_s

        url = item["url"] + "jiancha/"
        yield Request(url, callback=self.parse_jiancha, dont_filter=True, meta={"item": deepcopy(item)})

    #检查
    def parse_jiancha(self,response):
        item = response.meta["item"]
        p_s = ""
        p_list = response.xpath("//div[@class='p_cleftartbox']/p")
        for p in p_list:
            p_raw = p.xpath(".//text()").extract()
            p_info = str(p_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace(" ",
            "").replace("\\u3000", "").replace("','", "").replace("\\xa0", "").replace("\\n", "").replace("\\r",
            "").replace("\\t", "")
            if len(p_info) > 1:
                p_s = p_s + p_info + "\n"
        item["jiancha"] = p_s

        url = item["url"] + "jianbie/"
        yield Request(url, callback=self.parse_jianbie, dont_filter=True, meta={"item": deepcopy(item)})

    #鉴别
    def parse_jianbie(self,response):
        item = response.meta["item"]
        p_s = ""
        p_list = response.xpath("//div[@class='p_cleftartbox']/p")
        for p in p_list:
            p_raw = p.xpath(".//text()").extract()
            p_info = str(p_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace(" ",
            "").replace("\\u3000", "").replace("','", "").replace("\\xa0", "").replace("\\n", "").replace("\\r",
            "").replace("\\t", "")
            if len(p_info) > 1:
                p_s = p_s + p_info + "\n"
        item["jianbie"] = p_s

        url = item["url"] + "yufang/"
        yield Request(url, callback=self.parse_yufang, dont_filter=True, meta={"item": deepcopy(item)})

    #预防
    def parse_yufang(self,response):
        item = response.meta["item"]
        p_s = ""
        p_list = response.xpath("//div[@class='p_cleftartbox']/p")
        for p in p_list:
            p_raw = p.xpath(".//text()").extract()
            p_info = str(p_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace(" ",
            "").replace("\\u3000", "").replace("','", "").replace("\\xa0", "").replace("\\n", "").replace("\\r",
            "").replace("\\t", "")
            if len(p_info) > 1:
                p_s = p_s + p_info + "\n"
        item["yufang"] = p_s

        url = item["url"] + "shiliao/"
        yield Request(url, callback=self.parse_shiliao, dont_filter=True, meta={"item": deepcopy(item)})


    def parse_shiliao(self,response):
        item = response.meta["item"]
        shiyi_list = response.xpath("//div[@id='p_bigbox0']/div[1]")
        shiyi_info_raw = shiyi_list.xpath("./div/span/text()").extract()
        shiyi = str(shiyi_info_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
        "").replace("\\n","\n")
        item["shiyi"] = shiyi

        jinjin_list = response.xpath("//div[@id='p_bigbox0']/div[2]")
        jinji_info_raw = jinjin_list.xpath("./div/span/text()").extract()
        jinji = str(jinji_info_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
        "").replace("\\n","\n")
        item["jinji"] = jinji

        # print(item)
        yield item
        # print(shiyi)
        #
        # print(jinji)