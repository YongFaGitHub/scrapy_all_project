# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from scrapy import Request
import os



class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['ci.qiuyi.cn/']
    start_urls = ['http://ci.qiuyi.cn/list/symptomsku/1/index.html']

    def parse(self, response):
        item = {}
        div_list = response.xpath("//div[@class='map_list_block']/div")
        for div in div_list:
            body_raw = div.xpath("./h3/a/text()").extract_first()
            item["body"] = body_raw
            a_list = div.xpath("./div/a")
            for a in a_list:
                title_raw = a.xpath("./text()").extract_first()
                item["title"] = title_raw
                url = a.xpath("./@href").extract_first()
                yield Request(url,callback=self.parse_disease,dont_filter=True,meta={"item":deepcopy(item)})


    def parse_disease(self,response):
        item=response.meta["item"]
        item["img_url"] = ""
        item["huanbingbuwei"] =""
        item["suoshukeshi"] =""
        item["xifenzhengzhuang"] =""
        item["xiangguanjibing"] =""
        item["xiangguanjiancha"] =""
        item["xiangguanyaopin"] =""
        item["xiangguanzhengzhuang"] =""
        item["zhengzhuangqiyin"] = ""
        item["zhengzhuangmiaoshu"] =""
        item["jiancha"] =""
        item["zhenduan_jianbie"] =""
        item["zhiliao_yufang"] =""

        img_url = response.xpath("//div[@class='img_tool']/img/@src").extract_first()
        if img_url is not None:
            item["img_url"] = img_url
            yield Request(img_url,callback=self.parse_img,dont_filter=True,meta={"item":deepcopy(item)})


        li_list = response.xpath("//ul[@class='ul_h']/li")
        for li in li_list:
            text_m = li.xpath("./strong/text()").extract_first()
            if text_m == "患病部位:":
                huanbingbuwei_raw = li.xpath("./span/text()").extract()
                huanbingbuwei = str(huanbingbuwei_raw).replace("['","").replace("']","").replace("[",
                "").replace("]","").replace("\\u3000","").replace("\\xa0","")
                item["huanbingbuwei"] = huanbingbuwei

            if text_m == "所属科室:":
                suoshukeshi_raw = li.xpath("./span/text()").extract()
                suoshukeshi = str(suoshukeshi_raw).replace("['","").replace("']","").replace("[",
                "").replace("]","").replace("\\u3000","").replace("\\xa0","")
                item["suoshukeshi"] = suoshukeshi

            if text_m == "细分症状:":
                xifenzhengzhuang_raw = li.xpath("./span/text()").extract()
                xifenzhengzhuang = str(xifenzhengzhuang_raw).replace("['","").replace("']","").replace("[",
                "").replace("]","").replace("\\u3000","").replace("\\xa0","")
                item["xifenzhengzhuang"] = xifenzhengzhuang

            if text_m == "相关疾病:":
                xiangguanjibing_raw = li.xpath("./span/text()").extract()
                xiangguanjibing = str(xiangguanjibing_raw).replace("['","").replace("']","").replace("[",
                "").replace("]","").replace("\\u3000","").replace("\\xa0","")
                item["xiangguanjibing"] = xiangguanjibing

            if text_m == "相关检查:":
                xiangguanjiancha_raw = li.xpath("./span/text()").extract()
                xiangguanjiancha = str(xiangguanjiancha_raw).replace("['", "").replace("']", "").replace("[",
                "").replace("]","").replace("\\u3000", "").replace("\\xa0", "")
                item["xiangguanjiancha"] = xiangguanjiancha

            if text_m == "相关药品:":
                xiangguanyaopin_raw = li.xpath("./span/text()").extract()
                xiangguanyaopin = str(xiangguanyaopin_raw).replace("['", "").replace("']", "").replace("[",
                "").replace("]", "").replace("\\u3000", "").replace("\\xa0", "")
                item["xiangguanyaopin"] = xiangguanyaopin

            if text_m == "相关症状:":
                xiangguanzhengzhuang_raw = li.xpath("./span/text()").extract()
                xiangguanzhengzhuang = str(xiangguanzhengzhuang_raw).replace("['", "").replace("']", "").replace("[",
                "").replace("]","").replace("\\u3000", "").replace("\\xa0", "")
                item["xiangguanzhengzhuang"] = xiangguanzhengzhuang


        dd_list = response.xpath("//dl[@class='blue change_s']/dd")
        # print(dd_list)
        for dd in dd_list:
            text_raw = dd.xpath("./a/text()").extract_first()
            print(text_raw)

            #症状描述
            if text_raw == "症状描述" or text_raw == "概述":
                numble_raw = dd.xpath("./span/text()").extract_first()
                numble = int(numble_raw) + 2
                zhengzhuang_div = response.xpath("//div[@id='o_l']/div[{}]".format(numble))
                p_zhengzhuang_list = zhengzhuang_div.xpath("./p")
                zhengzhuang_s = ""
                for p_zhengzhuang in p_zhengzhuang_list:
                    zhengzhuang_raw = p_zhengzhuang.xpath(".//text()").extract()
                    zhengzhuang = str(zhengzhuang_raw).replace("['","").replace("']","").replace("[","").replace("]",
                    "").replace(" ","").replace("\\u3000","").replace("\\xa0","").replace("\\n","").replace("\\r",
                    "").replace("\\t","").replace("','","")
                    if len(zhengzhuang)>1:
                        zhengzhuang_s = zhengzhuang_s + zhengzhuang +"\n"
                #删除“来源地址：，来源资料：” 之后的内容
                if "来源资料：" in zhengzhuang_s:
                    zhengzhuang1 = zhengzhuang_s.split("来源资料：")
                    zhengzhuang_s = zhengzhuang1[0]
                if "来源地址：" in zhengzhuang_s:
                    zhengzhuang_2 = zhengzhuang_s.split("来源地址：")
                    zhengzhuang_s = zhengzhuang_2[0]
                if "参考资料：" in zhengzhuang_s:
                    zhengzhuang_3 = zhengzhuang_s.split("参考资料：")
                    zhengzhuang_s = zhengzhuang_3[0]
                item["zhengzhuangmiaoshu"] = zhengzhuang_s

            if text_raw == "症状起因" or text_raw == "病因":
                numble_raw = dd.xpath("./span/text()").extract_first()
                numble = int(numble_raw) + 2
                qiyin_div = response.xpath("//div[@id='o_l']/div[{}]".format(numble))

                p_qiyin_list = qiyin_div.xpath("./p")
                qiyin_s = ""
                for p_qiyin in p_qiyin_list:
                    qiyin_raw = p_qiyin.xpath(".//text()").extract()
                    qiyin = str(qiyin_raw).replace("['","").replace("']","").replace("[","").replace("]",
                    "").replace(" ","").replace("\\u3000","").replace("\\xa0","").replace("\\n","").replace("\\r",
                    "").replace("\\t","").replace("','","")
                    if len(qiyin)>1:
                        qiyin_s = qiyin_s + qiyin +"\n"
                if "来源资料：" in qiyin_s:
                    qiyin1 = qiyin_s.split("来源资料：")
                    qiyin_s = qiyin1[0]
                if "来源地址：" in qiyin_s:
                    qiyin_2 = qiyin_s.split("来源地址：")
                    qiyin_s = qiyin_2[0]
                if "参考资料：" in qiyin_s:
                    qiyin_3 = qiyin_s.split("参考资料：")
                    qiyin_s = qiyin_3[0]
                item["zhengzhuangqiyin"] = qiyin_s

            if text_raw == "症状诊断/鉴别" or text_raw=="诊断":
                numble_raw = dd.xpath("./span/text()").extract_first()
                numble = int(numble_raw) + 2
                zhenduan_jianbie_div = response.xpath("//div[@id='o_l']/div[{}]".format(numble))
                p_zhenduan_jianbie_list = zhenduan_jianbie_div.xpath("./p")
                zhenduan_jianbie_s = ""
                for p_zhenduan_jianbie in p_zhenduan_jianbie_list:
                    zhenduan_jianbie_raw = p_zhenduan_jianbie.xpath(".//text()").extract()
                    zhenduan_jianbie = str(zhenduan_jianbie_raw).replace("['","").replace("']","").replace("[","").replace("]",
                    "").replace(" ","").replace("\\u3000","").replace("\\xa0","").replace("\\n","").replace("\\r",
                    "").replace("\\t","").replace("','","")
                    if len(zhenduan_jianbie)>1:
                        zhenduan_jianbie_s = zhenduan_jianbie_s + zhenduan_jianbie +"\n"

                if "来源资料：" in zhenduan_jianbie_s:
                    zhenduan_jianbie1 = zhenduan_jianbie_s.split("来源资料：")
                    zhenduan_jianbie_s = zhenduan_jianbie1[0]
                if "来源地址：" in zhenduan_jianbie_s:
                    zhenduan_jianbie_2 = zhenduan_jianbie_s.split("来源地址：")
                    zhenduan_jianbie_s = zhenduan_jianbie_2[0]
                if "参考资料：" in zhenduan_jianbie_s:
                    zhenduan_jianbie_3 = zhenduan_jianbie_s.split("来源地址：")
                    zhenduan_jianbie_s = zhenduan_jianbie_3[0]


                item["zhenduan_jianbie"] = zhenduan_jianbie_s

            if text_raw == "症状检查" or text_raw == "检查":
                numble_raw = dd.xpath("./span/text()").extract_first()
                numble = int(numble_raw) + 2
                jiancha_div = response.xpath("//div[@id='o_l']/div[{}]".format(numble))

                p_jiancha_list = jiancha_div.xpath("./p")
                jiancha_s = ""
                for p_jiancha in p_jiancha_list:
                    jiancha_raw = p_jiancha.xpath(".//text()").extract()
                    jiancha= str(jiancha_raw).replace("['","").replace("']","").replace("[","").replace("]",
                    "").replace(" ","").replace("\\u3000","").replace("\\xa0","").replace("\\n","").replace("\\r",
                    "").replace("\\t","").replace("','","")
                    if len(jiancha) > 1:
                        jiancha_s = jiancha_s + jiancha + "\n"

                if "来源资料：" in jiancha_s:
                    jiancha1 = jiancha_s.split("来源资料：")
                    jiancha_s = jiancha1[0]
                if "来源地址：" in jiancha_s:
                    jiancha_2 = jiancha_s.split("来源地址：")
                    jiancha_s = jiancha_2[0]
                if "参考资料：" in jiancha_s:
                    jiancha_3 = jiancha_s.split("来源地址：")
                    jiancha_s = jiancha_3[0]

                item["jiancha"] = jiancha_s

            if text_raw == "治疗/预防" or text_raw=="预防":
                numble_raw = dd.xpath("./span/text()").extract_first()
                numble = int(numble_raw) + 2
                zhiliao_yufang_div = response.xpath("//div[@id='o_l']/div[{}]".format(numble))


                p_zhiliao_yufang_list = zhiliao_yufang_div.xpath("./p")
                zhiliao_yufang_s = ""
                for p_zhiliao_yufang in p_zhiliao_yufang_list:
                    zhiliao_yufang_raw = p_zhiliao_yufang.xpath(".//text()").extract()
                    zhiliao_yufang= str(zhiliao_yufang_raw).replace("['","").replace("']","").replace("[","").replace("]",
                    "").replace(" ","").replace("\\u3000","").replace("\\xa0","").replace("\\n","").replace("\\r",
                    "").replace("\\t","").replace("','","")
                    if len(zhiliao_yufang) > 1:
                        zhiliao_yufang_s = zhiliao_yufang_s + zhiliao_yufang + "\n"

                if "来源资料：" in zhiliao_yufang_s:
                    zhiliao_yufang1 = zhiliao_yufang_s.split("来源资料：")
                    zhiliao_yufang_s = zhiliao_yufang1[0]
                if "来源地址：" in zhiliao_yufang_s:
                    zhiliao_yufang_2 = zhiliao_yufang_s.split("来源地址：")
                    zhiliao_yufang_s = zhiliao_yufang_2[0]
                if "参考资料：" in zhiliao_yufang_s:
                    zhiliao_yufang_3 = zhiliao_yufang_s.split("来源地址：")
                    zhiliao_yufang_s = zhiliao_yufang_3[0]
                item["zhiliao_yufang"] = zhiliao_yufang_s

        yield item
    def parse_img(self,response):
        item = response.meta["item"]
        try:
            os.mkdir("I:/qiuyi_img")
        except:
            pass
        try:
            os.mkdir("I:/qiuyi_img/{}".format(item["body"]))
        except:
            pass
        with open("I:/qiuyi_img/{}/{}.jpg".format(item["body"],item["title"]),"wb") as f:
            f.write(response.body)


