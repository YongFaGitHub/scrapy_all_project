# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy



class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['zzk.xywy.com']
    start_urls = []

    def start_requests(self):
        list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u",'v',"w","x","y","z"]
        for i in list:
            url = "http://zzk.xywy.com/p/{}.html".format(i)
            yield Request(url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        item = {}
        div_list = response.xpath("//div[@class='ks-ill-txt']/div")
        for div in div_list:
            li_list = div.xpath("./ul/li")
            for li in li_list:
                title = li.xpath("./a/@title").extract_first()
                item["title"] = title
                url_raw = li.xpath("./a/@href").extract_first()
                url = "http://zzk.xywy.com"  + url_raw


                # url_one = url_raw.replace("gaishu","{}")
                # url_two = "http://zzk.xywy.com" + url_one
                # item["url"] = url_two
                #
                # url = url_two.format("gaishu")  #可能疾病的地址
                yield Request(url,callback=self.parse_img_cun,meta={"item":deepcopy(item)},dont_filter=True)


    def parse_img_cun(self,response):
        item = response.meta["item"]
        img_url = response.xpath("//div[@class='rec-imgbox fl bor mr15']/img/@src").extract_first()
        item["img_url"] = img_url

        yield Request(img_url,callback=self.img_cun,meta={"item":deepcopy(item)},dont_filter=True)

    def img_cun(self,response):
        item = response.meta["item"]

        with open("I:/症状图片/xywy/{}.jpg".format(item["title"]),"wb") as f:
            f.write(response.body)
        with open("H:/pycharmproject/project/xywy/zhengzhuang/zhengzhuang/spiders/title.txt","a+",encoding="utf-8") as f:
            f.write(item["title"])
            f.write("、")
            f.write(item["img_url"])
            f.write("\n")













    #可能疾病
    def parse_kenengjibing(self,response):
        item = response.meta["item"]
        p_s = ""
        ul_list = response.xpath("//div[@class='blood-item panel']/ul[1]/following-sibling::*")#可能疾病列表
        for ul in ul_list:
            p_one = ul.xpath("./li[1]/a/text()").extract_first()
            if len(p_one)>1:
                p_s = p_s + p_one +"、"
        item["kenengjibing"] = p_s[:-1]
        # print(item)
        url = (item["url"]).format("jieshao")
        yield Request(url, callback=self.parse_jieshao, meta={"item": deepcopy(item)}, dont_filter=True)

    #介绍
    def parse_jieshao(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='zz-articl fr f14']//p")
        p_s = ""
        for p in p_list:
            p_raw = p.xpath(".//text()").extract()
            p_info = str(p_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
            "").replace("\\n","").replace("\\t","").replace("\\r","").replace("','","").replace("\\u3000",
            "").replace("\\xa0","").replace("&alpha;","")
            if len(p_info)>1:
                p_s = p_s + p_info +"\n"
        item["disease"] = p_s[:-1]
        # print(item)
        url = (item["url"]).format("yuanyin") #病因
        yield Request(url, callback=self.parse_bingyin, meta={"item": deepcopy(item)}, dont_filter=True)

    #病因
    def parse_bingyin(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='zz-articl fr f14']//p")
        p_s = ""
        for p in p_list:
            p_raw = p.xpath(".//text()").extract()
            p_info = str(p_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
            "").replace("\\n","").replace("\\t","").replace("\\r","").replace("','","").replace("\\u3000",
            "").replace("\\xa0","")
            if len(p_info) > 1:
                p_s = p_s + p_info + "\n"
        item["bingyin"] = p_s[:-1]

        url = (item["url"]).format("yufang")  #预防
        yield Request(url, callback=self.parse_yufang, meta={"item": deepcopy(item)}, dont_filter=True)

    #预防
    def parse_yufang(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='zz-articl fr f14']//p")
        p_s = ""
        for p in p_list:
            p_raw = p.xpath(".//text()").extract()
            p_info = str(p_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
            "").replace("\\n","").replace("\\t","").replace("\\r","").replace("','","").replace("\\u3000",
            "").replace("\\xa0","")
            if len(p_info) > 1:
                p_s = p_s + p_info + "\n"
        item["yufang"] = p_s[:-1]

        url = (item["url"]).format("jiancha")  # 检查地址
        yield Request(url, callback=self.parse_jiancha, meta={"item": deepcopy(item)}, dont_filter=True)


    #检查
    def parse_jiancha(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='zz-articl fr f14']//p")
        p_s = ""
        for p in p_list:
            p_raw = p.xpath(".//text()").extract()
            p_info = str(p_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
            "").replace("\\n","").replace("\\t","").replace("\\r","").replace("','","").replace("\\u3000",
            "").replace("\\xa0","")
            if len(p_info) > 1:
                p_s = p_s + p_info + "\n"
        item["jiancha"] = p_s[:-1]

        url = (item["url"]).format("zhenduan")  # 鉴别地址
        yield Request(url, callback=self.parse_zhenduan, meta={"item": deepcopy(item)}, dont_filter=True)


    #鉴别
    def parse_zhenduan(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='zz-articl fr f14']//p")
        p_s = ""
        for p in p_list:
            p_raw = p.xpath(".//text()").extract()
            p_info = str(p_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
            "").replace("\\n","").replace("\\t","").replace("\\r","").replace("','","").replace("\\u3000",
            "").replace("\\xa0","")
            if len(p_info) > 1:
                p_s = p_s + p_info + "\n"
        item["jianbie"] = p_s[:-1]
        # print(item)
        yield item