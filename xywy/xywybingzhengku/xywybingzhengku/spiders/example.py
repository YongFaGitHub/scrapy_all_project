# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['club.xywy.com']
    start_urls = ['http://jib.xywy.com/']

    def parse(self, response):
        item = {}
        li_list = response.xpath("//ul[@class='illness-list clearfix']/li")

        for li in li_list:
            big_class_raw = li.xpath("./a/text()").extract_first()
            big_class = str(big_class_raw)
            item["big_class"] = big_class

            div_list = li.xpath("./div/div/div")
            for div in div_list:
                big_title_raw = div.xpath("./div/a/text()").extract_first()
                big_title = str(big_title_raw)
                item["big_title"] = big_title

                samll_list = div.xpath("./ul/li")
                for small in samll_list:
                    url_raw = small.xpath("./a/@href").extract_first()

                    small_title_raw = small.xpath("./a/text()").extract_first()
                    small_title = str(small_title_raw)
                    item["small_title"] = small_title
                    item["a"] = 0
                    item["b"] = 0
                    item["c"] = 0
                    item["d"] = 0
                    item["e"] = 0
                    item["f"] = 0
                    item["g"] = 0
                    item["h"] = 0
                    if len(url_raw) < 26:
                        url = "http://jib.xywy.com" + url_raw
                        item["url"] = url
                        # print(url)
                        yield Request(url,callback=self.parse_one,meta={"item": deepcopy(item)},dont_filter=True)



    def parse_one(self,response):
        item = response.meta["item"]

        #疾病简介
        if item["a"] ==0:
            url_raw = response.xpath("//a[text()='疾病介绍']/@href").extract_first()  #疾病简介
            item["a"] = 1
            if url_raw  is not None:
                url = "http://jib.xywy.com" + url_raw
            # print(url)
                yield Request(url, callback=self.parse_two, meta={"item": deepcopy(item)}, dont_filter=True)

        # 典型症状
        if item["b"] == 0:
            dianxingzhengzhuang_url = response.xpath("//a[text()='症状']/@href").extract_first()  # 症状地址
            item["b"] = 1
            if dianxingzhengzhuang_url is not None:
                durl = "http://jib.xywy.com" +dianxingzhengzhuang_url
                yield Request(durl, callback=self.dianxingzhengzhuang, meta={"item": deepcopy(item)},dont_filter=True)
            else:
                item["dianxingzhengzhuang"] = "暂无"


        if item["c"] == 0:  # 发病原因
            fabingyuanyin_url = response.xpath("//a[text()='病因']/@href").extract_first()  # 病因地址
            item["c"] = 1
            if fabingyuanyin_url is not None:
                furl = "http://jib.xywy.com" + fabingyuanyin_url
                yield Request(furl, callback=self.fabingyuanyin, meta={"item": deepcopy(item)},dont_filter=True)
            else:
                item["fabingyuanyin"] = "暂无"


        if item["d"] == 0:  # 疾病预防
            jibingyufang_url = response.xpath("//a[text()='预防']/@href").extract_first()   # 疾病预防地址
            item["d"] = 1
            if jibingyufang_url is not None:
                jibingyufangurl = "http://jib.xywy.com" + jibingyufang_url
                yield Request(jibingyufangurl, callback=self.jibingyufang, meta={"item": deepcopy(item)},dont_filter=True)
            else:
                item["jibingyufang"] = "暂无"


        if item["e"] == 0:  # 临床检查
            linchuangjiancha_url = response.xpath("//a[text()='检查']/@href").extract_first()    # 检查地址
            item["e"] = 1
            if linchuangjiancha_url is not None:
                linchuangjianchaurl = "http://jib.xywy.com" +linchuangjiancha_url
                yield Request(linchuangjianchaurl, callback=self.linchuangjiancha, meta={"item": deepcopy(item)},dont_filter=True)
            else:
                item["linchuangjiancha"] = "暂无"


        # 鉴别诊断
        if item["f"] == 0:
            jianbiezhenduan_url = response.xpath("//a[text()='诊断鉴别']/@href").extract_first()    # 诊断鉴别地址
            item["f"] = 1
            if jianbiezhenduan_url is not None:
                jianbiezhenduanurl= "http://jib.xywy.com" + jianbiezhenduan_url
                yield Request(jianbiezhenduanurl, callback=self.jianbiezhenduan, meta={"item": deepcopy(item)},dont_filter=True)
            else:
                item["jianbiezhenduan"] = "暂无"


        # 治疗方法
        if item["g"] == 0:
            zhiliaofangfa_url = response.xpath("//a[text()='治疗']/@href").extract_first()   # 治疗地址
            item["g"] = 1
            if zhiliaofangfa_url is not None:
                zhiliaofangfaurl = "http://jib.xywy.com" + zhiliaofangfa_url
                yield Request(zhiliaofangfaurl, callback=self.zhiliaofangfa, meta={"item": deepcopy(item)},dont_filter=True)
            else:
                item["zhiliaofangfa"] = "暂无"


        # 疾病护理
        if item["h"] == 0:
            jibinghuli_url = response.xpath("//a[text()='护理']/@href").extract_first()    # 护理地址
            item["h"] = 1
            if jibinghuli_url is not None:
                jibinghuliurl = "http://jib.xywy.com" +jibinghuli_url
                yield Request(jibinghuliurl, callback=self.jibinghuli, meta={"item": deepcopy(item)},dont_filter=True)
            else:
                item["jibinghuli"] = "暂无"
        #
        yield Request(item["url"], callback=self.parse_f, meta={"item": deepcopy(item)}, dont_filter=True)



    def parse_two(self,response):
        item = response.meta["item"]

        #疾病简介
        disease_raw = response.xpath("//div[@class='jib-articl-con jib-lh-articl']/p/text()").extract()
        disease = str(disease_raw).replace("\\r","").replace("\\n","").replace("\\t","").replace("['",
        "").replace("']","").replace(" ","").replace("[","").replace("]","").replace("\\xa0","").replace("\\u3000","")
        item['disease'] = disease

        #就诊科室
        keshi_raw = response.xpath("//span[text()='就诊科室：']/following-sibling::*/text()").extract()
        keshi = str(keshi_raw).replace("['","").replace("']","").replace(" ","").replace("[","").replace("]","")
        item["keshi"] = keshi

        #药品
        yaopin_raw = response.xpath("//span[text()='常用药品：']/following-sibling::*//text()").extract()
        yaopin  = str(yaopin_raw).replace("\\n","").replace("\\t","").replace(" ","").replace("['","").replace("']",
        "").replace("','','","、").replace("','","").replace("[","").replace("]","").replace("\\xa0","").replace("\\u3000","")
        item["yaopin"] = yaopin

        # print(item)
        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)}, dont_filter=True)


    # 典型症状
    def dianxingzhengzhuang(self, response):

        item = response.meta["item"]
        info_raw = response.xpath("//span[@class='db f12 lh240 mb15 ']//text()").extract()
        info = str(info_raw).replace("\\n","").replace("\\r","").replace("\\t","").replace(" ","").replace("','','",
        "、").replace("','","").replace("['","").replace("']","").replace("[","").replace("]","").replace("\\xa0",
        "").replace("\\u3000","")
        item["dianxingzhengzhuang"] = info
        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)}, dont_filter=True)

    # 发病原因
    def fabingyuanyin(self, response):
        item = response.meta["item"]

        p_list = response.xpath("//div[@class=' jib-articl fr f14 jib-lh-articl']/*")

        p_info_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            # print(p_info_raw)
            p_info = str(p_info_raw).replace("['","").replace("']","").replace("\\r","").replace("\\n","").replace("\\t",
            "").replace(" ","").replace("','","").replace("\\xa0","").replace("\\u3000","")
            if len(p_info) > 1:
                p_info_s = p_info_s + p_info +"\n"

        item["fabingyuanyin"] = p_info_s
        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)}, dont_filter=True)

    # 疾病预防
    def jibingyufang(self, response):
        item = response.meta["item"]

        p_list = response.xpath("//div[@class='jib-articl fr f14 jib-lh-articl']/*")

        p_info_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            # print(p_info_raw)
            p_info = str(p_info_raw).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n", "").replace("\\t",
            "").replace(" ", "").replace("','", "").replace("\\xa0", "").replace("\\u3000", "")
            if len(p_info) > 1:
                p_info_s = p_info_s + p_info + "\n"

        item["jibingyufang"] = p_info_s
        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)}, dont_filter=True)

    # 临床检查
    def linchuangjiancha(self, response):
        item = response.meta["item"]

        p_list = response.xpath("//div[@class='jib-articl fr f14 jib-lh-articl']/p")

        p_info_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            # print(p_info_raw)
            p_info = str(p_info_raw).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
            "").replace( "\\t", "").replace(" ", "").replace("','", "").replace("\\xa0", "").replace("\\u3000",
            "").replace("[","").replace("]","")
            if len(p_info) > 1:
                p_info_s = p_info_s + p_info + "\n"

        item["linchuangjiancha"] = p_info_s
        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)}, dont_filter=True)

    # 鉴别诊断
    def jianbiezhenduan(self, response):
        item = response.meta["item"]

        p_list = response.xpath("//div[@class='jib-articl fr f14 jib-lh-articl']/p")

        p_info_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            # print(p_info_raw)
            p_info = str(p_info_raw).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
             "").replace("\\t", "").replace(" ", "").replace("','", "").replace("\\xa0", "").replace("\\u3000",
              "").replace("[", "").replace("]", "")
            if len(p_info) > 1:
                p_info_s = p_info_s + p_info + "\n"

        item["jianbiezhenduan"] = p_info_s
        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)}, dont_filter=True)

    # 治疗方法
    def zhiliaofangfa(self, response):
        item = response.meta["item"]

        p_list = response.xpath("//div[@class='jib-articl fr f14 ']//*")

        p_info_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            # print(p_info_raw)
            p_info = str(p_info_raw).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
             "").replace("\\t", "").replace(" ", "").replace("','", "").replace("\\xa0", "").replace("\\u3000",
               "").replace("[", "").replace("]", "")
            if len(p_info) > 1:
                p_info_s = p_info_s + p_info + "\n"

        item["zhiliaofangfa"] = p_info_s
        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)}, dont_filter=True)



    # 疾病护理
    def jibinghuli(self, response):
        item = response.meta["item"]

        p_list = response.xpath("//div[@class='jib-articl fr f14 jib-lh-articl']/p")

        p_info_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            # print(p_info_raw)
            p_info = str(p_info_raw).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
             "").replace("\\t","").replace(" ", "").replace("','", "").replace("\\xa0", "").replace("\\u3000",
             "").replace("[", "").replace("]", "")
            if len(p_info) > 1:
                p_info_s = p_info_s + p_info + "\n"

        item["jibinghuli"] = p_info_s
        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)}, dont_filter=True)

    def parse_f(self, response):
        item = response.meta["item"]
        # print(len(list(item.keys())))

        if len(list(item.keys())) == 22:
            print(item)
            # pass
            yield item




    #
    #
    #
    #
    #
    #










        # fabingyuanyin_url = response.xpath("//div[@class='jib-nav fl bor']//a[text()='病因']") #病因地址
        #
        # jibingyufang_url = response.xpath("//div[@class='jib-nav fl bor']//a[text()='预防']")  # 疾病预防地址
        #
        # dianxingzhengzhuang_url = response.xpath("//div[@class='jib-nav fl bor']//a[text()='症状']")  # 症状地址
        #
        # linchuangjiancha_url = response.xpath("//div[@class='jib-nav fl bor']//a[text()='检查']")  # 检查地址
        #
        # jianbiezhenduan_url = response.xpath("//div[@class='jib-nav fl bor']//a[text()='诊断鉴别']")  # 诊断鉴别地址
        #
        # zhiliaofangfa_url = response.xpath("//div[@class='jib-nav fl bor']//a[text()='治疗']")  # 治疗地址
        #
        # jibinghuli_url = response.xpath("//div[@class='jib-nav fl bor']//a[text()='护理']")  # 护理地址

