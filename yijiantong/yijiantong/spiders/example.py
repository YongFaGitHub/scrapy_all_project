# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ["www.51esou.com"]
    start_urls = ["http://www.51esou.com/Jibingku.php"]

    def parse(self, response):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        dl_list = response.xpath("//div[@class='xleft_list']/dl/dt")
        item = {}
        for dt in dl_list:

            url_raw  = dt.xpath("./a/@href").extract_first()
            url = "http://www.51esou.com/" + url_raw

            title_raw  = dt.xpath("./h3/text()").extract_first()
            title  = str(title_raw)
            item["title"] = title
            yield Request(url,callback=self.parse_disease,meta={"item" : deepcopy(item)})

        next_url_raw = response.xpath("//div[@class='site-pages']/li/a[text()='后一页']/@href").extract_first()
        next_url =  "http://www.51esou.com/" + next_url_raw
        yield Request(next_url,callback=self.parse,dont_filter=True,meta={"item": deepcopy(item)})

    def parse_disease(self,response):
        item = response.meta["item"]

        #别名
        title2_raw = response.xpath("//ul[@class='clearfix']/li/span[text()='别名：']/../text()").extract()
        title2 = str(title2_raw).replace("[","").replace("]","").replace("'","").replace(" ","").replace("\\r",
        "").replace("\\n","").replace("\\u3000","").replace("[","").replace("]","")
        if len(title2) >1:
            item["title2"] = title2
        else:
            item["title2"] = "暂无"
        #科室
        keshi_raw = response.xpath("//ul[@class='clearfix']/li/span[text()='就诊科室：']/../text()").extract()
        keshi = str(keshi_raw).replace("[","").replace("]","").replace("'","").replace("\\r",
        "").replace("\\n","").replace("\\u3000","").replace(" ","").replace("[","").replace("]","")

        if len(keshi)>1:
            item["keshi"] = keshi
        else:
            item["keshi"] = "暂无"

        #并发疾病
        bingfajibing_raw = response.xpath("//ul[@class='clearfix']/li/span[text()='并发疾病：']/../text()").extract()
        bingfajibing = str(bingfajibing_raw).replace("['","").replace("']","").replace("\\r",
        "").replace("\\n","").replace("\\u3000","").replace(" ","").replace("[","").replace("]","")

        if len(bingfajibing)>1:
            item["bingfajibing"] = bingfajibing
        else:
            item["bingfajibing"] = "暂无"


        #传播途径
        chuanbotujing_raw = response.xpath("//ul[@class='clearfix']/li/span[text()='传播途径：']/../text()").extract()
        chuanbotujing = str(chuanbotujing_raw).replace("['","").replace("']","").replace("\\r",
        "").replace("\\n","").replace("\\u3000","").replace(" ","").replace("[","").replace("]","")
        if len(chuanbotujing)>1:
            item["chuanbotujing"] = chuanbotujing

        else:
            item["chuanbotujing"] = "暂无"


        #多发人群
        duofarenqun_raw = response.xpath("//ul[@class='clearfix']/li/span[text()='多发人群：']/../text()").extract()
        duofarenqun = str(duofarenqun_raw).replace("['","").replace("']","").replace("\\r",
        "").replace("\\n","").replace("\\u3000","").replace(" ","").replace("[","").replace("]","")
        if len(duofarenqun)>1:

            item["duofarenqun"] = duofarenqun
        else:
            item["duofarenqun"] = "暂无"

        #症状
        zhengzhuang_raw = response.xpath("//div[@class='litem']/ul/li//h4/a/text()").extract()
        zhengzhuang = str(zhengzhuang_raw).replace("['","").replace("']","").replace("\\r",
        "").replace("\\n","").replace("\\u3000","").replace(" ","").replace("','","、").replace("[",
        "").replace("]","")

        if len(zhengzhuang)>1:

            item["zhengzhuang"] = zhengzhuang
        else:
            item["zhengzhuang"] = "暂无"


        #疾病介绍，简介
        disease_raw = response.xpath("//div[@class='gaishu mt20']/p/text()").extract()
        disease = str(disease_raw).replace("['","").replace("']","").replace("\\r",
        "").replace("\\n","").replace("\\u3000","").replace(" ","").replace("[","").replace("]","")
        if len(disease)>1:
            item["disease"] = disease
        else:
            item["disease"] = "暂无"


        xiangqing_disease_url = response.xpath("//div[@class='gaishu mt20']/p/a/@href").extract_first()
        xiangqing_url = "http://www.51esou.com/" + xiangqing_disease_url
        yield Request(xiangqing_url,callback=self.parse_disease_info,dont_filter=True,meta={"item": deepcopy(item)})
        # print(item)


    def parse_disease_info(self,response):

        item = response.meta["item"]
        p_list = response.xpath("//div[@class='moduleContent']/p")
        p_s = ""
        for p in p_list:
            p_info_raw = p.xpath("./text()").extract()
            p_info = str(p_info_raw).replace("[","").replace("]","").replace("'","").replace("\\xa0",
            "").replace("\\r","").replace("\\n","").replace(' ',"").replace("','","")
            if len(p_info)>1:
                p_s = p_s + p_info +"\n"
            # print(p_info_raw)
        item["disease_info"] = p_s

        # print(item)

        yield item



