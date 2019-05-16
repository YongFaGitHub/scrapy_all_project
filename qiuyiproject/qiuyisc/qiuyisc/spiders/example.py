# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import os


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['ci.qiuyi.cn/']
    start_urls = ['http://ci.qiuyi.cn/list/foodku/1/index.html']

    def parse(self, response):
        item = {}
        div_list = response.xpath("//div[@class='map_list_block']/div")
        for div in div_list:
            big_class = div.xpath("./h3/a/text()").extract_first()
            item["big_class"] = big_class
            a_list = div.xpath("./div/a")
            for a in a_list:
                title = a.xpath("./text()").extract_first()
                item["title"] = title
                url = a.xpath("./@href").extract_first()
                yield Request(url,callback=self.parse_disease,meta={"item":deepcopy(item)},dont_filter=True)

    def parse_disease(self,response):
        item = response.meta["item"]
        item["jibenmiaoshu"] =""
        item["xiaotieshi"] = ""
        item["shiyi"] =""
        item["jinji"] = ""
        item["gongxiao"] =""
        item["gongnengzhuzhi"] = ""
        item["mingjialunshu"] = ""




        # print(item)
        img_url = response.xpath("//img[@alt='基本描述']/@src").extract_first()
        if img_url is not None:

            item["img_url"] = img_url
            yield Request(img_url,callback=self.parse_img,dont_filter=True,meta={"item":deepcopy(item)})

        else:
            item["img_url"] = ""

        #页面中有哪几个标签的判断
        dd_list = response.xpath("//dl[@class='blue change_s']/dd")
        for dd in dd_list:
            text = dd.xpath("./a/text()").extract_first()
            if text == "适宜和禁忌":
                numble_raw = dd.xpath("./span/text()").extract_first()

                numble = int(numble_raw) + 2

                div_shiyijinji = response.xpath("//div[@id='o_l']/div[{}]".format(numble))
                #适宜人群
                shiyi_list = div_shiyijinji.xpath("./dl[1]/dd/p")
                shiyi_s = ""
                for shiyi in shiyi_list:
                    shiyi_raw = shiyi.xpath(".//text()").extract()

                    shiyi  = str(shiyi_raw).replace("['","").replace("']","").replace("[","").replace("]",
                    "").replace(" ","").replace("','","：")
                    shiyi_s = shiyi_s + shiyi + "\n"
                item["shiyi"] = shiyi_s

                #禁忌人群
                jinji_list = div_shiyijinji.xpath("./dl[2]/dd/p")
                jinji_s = ""
                for jinji in jinji_list:
                    jinji_raw = jinji.xpath(".//text()").extract()

                    jinji = str(jinji_raw).replace("['", "").replace("']", "").replace("[", "").replace("]",
                    "").replace(" ","").replace("','", "：")
                    jinji_s = jinji_s + jinji + "\n"
                item["jinji"] = jinji_s

            if text == "基本描述":
                numble_raw = dd.xpath("./span/text()").extract_first()
                numble = int(numble_raw) + 2
                div_shiyijinji = response.xpath("//div[@id='o_l']/div[{}]".format(numble))

                disease_p = div_shiyijinji.xpath("./p")
                disease_s  = ""
                for dis_p in disease_p:
                    disease_raw = dis_p.xpath(".//text()").extract()
                    disease = str(disease_raw).replace("['","").replace("']","").replace("[","").replace("]",
                    "").replace("\\u3000","").replace(" ","").replace("','","").replace("\\n","").replace("\\xa0","")
                    if len(disease)>1:
                        disease_s = disease_s + disease +"\n"
                if "小贴士" in disease_s:
                    diseas_s = disease_s.split("小贴士")
                    item["jibenmiaoshu"] = diseas_s[0]
                    item["xiaotieshi"] = diseas_s[1]
                else:
                    item["jibenmiaoshu"] = disease_s
                    item["xiaotieshi"] = ""





                # disease = str(disease_raw).replace("['","").replace("']","").replace("[","").replace("]",
                # "").replace("\\u3000","").replace(" ","").replace("\\n","").replace("\\r","").replace("\\t",
                # "").replace("','","\n")
                # item["disease"] = disease

            if text == "功效标签":
                numble_raw = dd.xpath("./span/text()").extract_first()
                numble = int(numble_raw) + 2
                #选择功能标签所在的位置
                div_shiyijinji = response.xpath("//div[@id='o_l']/div[{}]".format(numble))
                p_list = div_shiyijinji.xpath("./p")
                gongxiao_s = ""
                for p in p_list:
                    gongxiao_raw = p.xpath(".//text()").extract()
                    gongxiao = str(gongxiao_raw).replace("['","").replace("']","").replace("[","").replace("]",
                    "").replace("\\u3000","").replace(" ","").replace("','","").replace("\\n","").replace("\\xa0","")
                    if len(gongxiao)>1:
                        gongxiao_s = gongxiao_s + gongxiao + "\n"

                item["gongxiao"] = gongxiao_s

            if text == "功能主治":
                numble_raw = dd.xpath("./span/text()").extract_first()
                numble = int(numble_raw) + 2
                div_shiyijinji = response.xpath("//div[@id='o_l']/div[{}]".format(numble))
                gongneng_p = div_shiyijinji.xpath("./p")
                gongneng_s = ""
                for gong_p in gongneng_p:
                    gongneng_raw  = gong_p.xpath(".//text()").extract()
                    gongneng = str(gongneng_raw).replace("['","").replace("']","").replace("[","").replace("]",
                    "").replace("\\u3000","").replace(" ","").replace("','","").replace("\\n","").replace("\\xa0","")
                    if len(gongneng)>1:
                        gongneng_s = gongneng_s + gongneng + "\n"

                if "【名家论述】" in gongneng_s:
                    gongneng_raw_s = gongneng_s.split("【名家论述】")
                    item["gongnengzhuzhi"] = gongneng_raw_s[0]
                    item["mingjialunshu"] = gongneng_raw_s[1]
                else:
                    item["gongnengzhuzhi"] = gongneng_s
                    item["mingjialunshu"] =""

        yield item

    def parse_img(self,response):
        item = response.meta["item"]
        try:
            os.mkdir("I:/qiuyi_img")
        except:
            pass

        try:
            os.mkdir("I:/qiuyi_img/{}".format(item["big_class"]))
        except:
            pass

        with open("I:/qiuyi_img/{}/{}.jpg".format(item["big_class"],item["title"]),"wb") as f:
            f.write(response.body)


