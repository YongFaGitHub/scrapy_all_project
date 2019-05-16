# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from copy import deepcopy
'''
疾病：疾病简介、典型症状、发病原因、疾病预防、临床检查、鉴别诊断、治疗方法、疾病护理、就诊科室、常用药品
目前不拿取：
    疾病自测：网站的填写问答
    疾病图集：图片信息
    医院医生：图片信息
'''
class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['jbk.39.net/']
    start_urls = ['http://jbk.39.net/']

    def parse(self, response):
        item = {}
        dl_list = response.xpath("//div[@class='mapList']/dl")
        # 拿到部位

        for dl in dl_list:
            position_list = dl.xpath("./dd/div[1]/ul/li")
            for position in position_list:
                jibing_list = position.xpath("./span[@class='right']/a")  # 病症列表
                for jibing in jibing_list:
                    title_raw =jibing.xpath("./text()").extract_first()# 拿到标题
                    title = str(title_raw)
                    item["title"] = title
                    # item["a"] = 0
                    # item["b"] = 0
                    # item["c"] =0
                    # item["d"] = 0
                    # item["e"] = 0
                    # item["f"] = 0
                    # item["g"] = 0
                    # item["h"] = 0


                    url= jibing.xpath("./@href").extract()[0]  # 拿到标题的url
                    item["url"] = url
                    len_url = url.split("/")
                    if len(len_url) == 5:
                        yield Request(url,callback=self.parse_one, meta={"item": deepcopy(item)},dont_filter=True)

    def parse_one(self,response):
        item = response.meta["item"]
        # li_list = response.xpath("//div[@class='leftNav']/ul/li")
            # 疾病预后/常用药品
        img_url = response.xpath("//div[@class='pic']/img/@src").extract_first()
        item["img_url"] = img_url
        print(item["title"] ,img_url)

        yield Request(img_url,callback=self.parse_img, meta={"item": deepcopy(item)},dont_filter=True)

    def parse_img(self,response):

        item = response.meta["item"]

        with open("I:/疾病图片/39健康/{}.jpg".format(item["title"]),"wb") as f:
            f.write(response.body)

        with open("H:/pycharmproject/project/39jk/bingzhengku/bingzhengku/spiders/img_url.txt","a+",encoding="utf-8") as f:
            f.write(item["title"])
            f.write("、")
            f.write(item["img_url"])
            f.write("\n")








        # if item["a"] == 0:    #疾病简介
        #     jibingjianjie_url = response.xpath("//li/a[text()='疾病简介']/@href").extract_first()  #疾病简介
        #     item["a"] = 1
        #     if jibingjianjie_url is not None:
        #
        #         yield Request(jibingjianjie_url,callback=self.jibingjianjie,meta={"item": deepcopy(item)})
        #     else:
        #         item["keshi"] = "暂无"
        #         item["yaopin"] = "暂无"
        #         item["disease"] = "暂无"
        #
        #
        # if item["b"] ==0: # 典型症状
        #     dianxingzhengzhuang_url  = response.xpath("//li/a[text()='典型症状']/@href").extract_first() #典型症状
        #     item["b"] = 1
        #     if dianxingzhengzhuang_url is not None:
        #
        #         yield Request(dianxingzhengzhuang_url, callback=self.dianxingzhengzhuang, meta={"item": deepcopy(item)})
        #     else:
        #         item["dianxingzhengzhuang"] = "暂无"
        #
        #
        # if item["c"] ==0:# 发病原因
        #     fabingyuanyin_url = response.xpath("//li/a[text()='发病原因']/@href").extract_first()  # 发病原因
        #     item["c"] = 1
        #     if fabingyuanyin_url is not None:
        #
        #         yield Request(fabingyuanyin_url, callback=self.fabingyuanyin, meta={"item": deepcopy(item)})
        #     else:
        #         item["fabingyuanyin"] = "暂无"
        #
        #
        # if item["d"] ==0:# 疾病预防
        #     jibingyufang_url = response.xpath("//li/a[text()='预防']/@href").extract_first()  # 疾病预防
        #     item["d"] = 1
        #     if jibingyufang_url is not None:
        #
        #         yield Request(jibingyufang_url, callback=self.jibingyufang, meta={"item": deepcopy(item)})
        #     else:
        #         item["jibingyufang"] = "暂无"
        #
        # if item["e"] == 0:  # 临床检查
        #     linchuangjiancha_url = response.xpath("//li/a[text()='临床检查']/@href").extract_first()  # 临床检查
        #     item["e"] = 1
        #     if linchuangjiancha_url is not None:
        #         yield Request(linchuangjiancha_url, callback=self.linchuangjiancha,meta={"item": deepcopy(item)})
        #     else:
        #         item["linchuangjiancha"] = "暂无"
        #
        # # 鉴别诊断
        # if item["f"] == 0:
        #     jianbiezhenduan_url =response.xpath("//li/a[text()='鉴别']/@href").extract_first()  # 鉴别诊断
        #     item["f"] = 1
        #     if jianbiezhenduan_url is not None:
        #
        #         yield Request(jianbiezhenduan_url, callback=self.jianbiezhenduan,meta={"item": deepcopy(item)})
        #     else:
        #         item["jianbiezhenduan"] = "暂无"
        #
        # # 治疗方法
        # if item["g"] == 0:
        #     zhiliaofangfa_url = response.xpath("//li/a[text()='治疗方法']/@href").extract_first()  # 治疗方法
        #     item["g"] = 1
        #     if zhiliaofangfa_url is not None:
        #
        #         yield Request(zhiliaofangfa_url, callback=self.zhiliaofangfa, meta={"item": deepcopy(item)},
        #                       )
        #     else:
        #         item["zhiliaofangfa"] = "暂无"
        #
        #  # 疾病护理
        # if item["h"] == 0:
        #     jibinghuli_url = response.xpath("//li/a[text()='护理']/@href").extract_first()  # 疾病自测
        #     item["h"] = 1
        #     if jibinghuli_url is not None:
        #         yield Request(jibinghuli_url, callback=self.jibinghuli, meta={"item": deepcopy(item)},
        #                       )
        #     else:
        #         item["jibinghuli"] = "暂无"
        #
        # # # print(item)
        # yield Request(item["url"],callback=self.parse_f,meta={"item": deepcopy(item)},)


    # 就诊科室，疾病简介
    def jibingjianjie(self,response):
        item = response.meta["item"]
        keshi_raw= response.xpath("//i[text()='就诊科室：']/following-sibling::*/text()").extract()
        keshi = str(keshi_raw).replace("['","").replace("']","").replace(" ","").replace("','","、").replace("\\xa0", "").replace("\\u3000", "")
        item["keshi"] = keshi
        # print(keshi)

        deal_raw = response.xpath("//div[@class='chi-know']/dl[@class='intro']//text()").extract()
        deal = str(deal_raw).replace("\\r\\n","").replace(" ","").replace("['","").replace("']","").replace("','",
        "").replace('\\t',"").replace("\\xa0","").replace("\\u3000","").replace("&ldquo;",
        "").replace("&middot;","").replace("&rdquo;","").replace("&mdash;","")
        item["disease"] = deal


        yaopin_raw = response.xpath("//i[text()='常用药品：']/following-sibling::*/@title").extract()
        yaopin = str(yaopin_raw).replace("['","").replace("']","").replace(" ","").replace("','","、").replace("\\xa0", "").replace("\\u3000", "")
        item["yaopin"] = yaopin
        # print(item)


        yield Request(item["url"],callback=self.parse_one, meta={"item": deepcopy(item)})

    # 典型症状
    def dianxingzhengzhuang(self,response):

        item = response.meta["item"]
        zheng_raw = response.xpath("//dl[@class='links']/*")
        #症状头部
        zhengzhuang1 = ""
        for zheng in zheng_raw:
            zhengzhuang_raw = zheng.xpath(".//text()").extract()
            zhengzhuang_s_raw = str(zhengzhuang_raw).replace("['","").replace("']","").replace(" ","").replace("\\r",
            "").replace("\\xa0","").replace("\\n","").replace("：','","：").replace("','','","、").replace("','","").replace("\\u3000",
            "")
            zhengzhuang1 = zhengzhuang1 + zhengzhuang_s_raw +"\n"

        p_list = response.xpath("//div[@class='art-box']/p")
        zhengzhuang2_s = ""
        for p in p_list:
            zhengzhuang2_raw = p.xpath(".//text()").extract()
            zhengzhuang2 = str(zhengzhuang2_raw).replace("['","").replace("']","").replace(" ","").replace("','",
            "").replace("\\xa0","").replace("\\u3000","")

            zhengzhuang2_s = zhengzhuang2_s + zhengzhuang2 + "\n"

        zhengzhuang  = zhengzhuang1 +zhengzhuang2_s

        item["dianxingzhengzhuang"] = zhengzhuang
        # print(item)

        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)})


    # 发病原因
    def fabingyuanyin(self,response):
        item = response.meta["item"]
        info_list  = response.xpath("//dl[@class='info']/*")
        bingyin1_s = ""
        for info in info_list:
            bingyin1_raw = info.xpath(".//text()").extract()
            bingyin1  = str(bingyin1_raw).replace("['","").replace("']","").replace(" ",
            "").replace("\\r","").replace("\\n","").replace("','","")
            bingyin1_s = bingyin1_s + bingyin1 +"\n"

        p_list = response.xpath("//div[@class='art-box']/p")
        bingyin2_s = ""
        for p in p_list:
            bingyin2_raw = p.xpath(".//text()").extract()
            bingyin2 = str(bingyin2_raw).replace("['", "").replace("']", "").replace(" ", "").replace("','",
            "").replace("\\xa0","").replace("\\r","").replace("\\n","").replace("\\u3000", "")
            bingyin2_s = bingyin2_s + bingyin2 + "\n"

        bingyin_f = bingyin1_s +bingyin2_s
        bingyin = str(bingyin_f).replace("&ldquo;","").replace("&middot;","").replace("&rdquo;","").replace("&mdash;","")

        item["fabingyuanyin"] = bingyin

        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)})


    #疾病预防
    def jibingyufang(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='art-box']/*")
        yufang1_s = ""
        for p in p_list:
            yufang1_raw = p.xpath(".//text()").extract()
            yufang1 = str(yufang1_raw).replace("['","").replace("']","").replace(" ",
            "").replace("','","").replace("\\r","").replace("\\n","")
            yufang1_s = yufang1_s +yufang1 +"\n"

        yufang = yufang1_s.replace("&ldquo;","").replace("&middot;","").replace("&rdquo;","").replace("&mdash;",
        "").replace("\\xa0","").replace("\\u3000", "")

        item["jibingyufang"] = yufang

        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)})


    #临床检查
    def linchuangjiancha(self,response):
        item = response.meta["item"]

        p_list = response.xpath("//div[@class='art-box']/*")
        jiancha1_s = ""
        for p in p_list:
            jiancha1_raw = p.xpath(".//text()").extract()
            jiancha1 = str(jiancha1_raw).replace("[","").replace("]","").replace("'","").replace("\\xa0",
            "").replace("\\u3000","").replace("\\n","").replace("&ldquo;","").replace("&middot;","").replace("&rdquo;","").replace("&mdash;","")
            jiancha1_s = jiancha1_s+ jiancha1 +"\n"
        item["linchuangjiancha"] = jiancha1_s

        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)})


    # 鉴别诊断
    def jianbiezhenduan(self,response):
        item = response.meta["item"]

        p_list = response.xpath("//div[@class='art-box']/*")
        jianbie1_s = ""
        for p in p_list:
            jianbie1_raw = p.xpath(".//text()").extract()
            jianbie1 = str(jianbie1_raw).replace("['", "").replace("']", "").replace(" ","").replace("','",
            "").replace("\\r","").replace("\\n", "").replace("&ldquo;","").replace("&middot;","").replace("&rdquo;",
            "").replace("&mdash;","").replace("\\xa0","").replace("\\u3000", "")

            jianbie1_s = jianbie1_s + jianbie1 +"\n"

        item["jianbiezhenduan"] = jianbie1_s

        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)},dont_filter=True)


    # 治疗方法
    def zhiliaofangfa(self,response):
        item = response.meta["item"]

        p_list = response.xpath("//div[@class='art-box']/*")
        zhiliao1_s = ""
        for p in p_list:
            zhiliao1_raw = p.xpath(".//text()").extract()
            zhiliao1 = str(zhiliao1_raw).replace("['", "").replace("']", "").replace(" ", "").replace("','",
            "").replace("\\r","").replace("\\n", "").replace("&ldquo;", "").replace("&middot;", "").replace("&rdquo;",
             "").replace("&mdash;", "").replace("\\xa0", "").replace("\\u3000","")
            zhiliao1_s = zhiliao1_s + zhiliao1 +"\n"

        item["zhiliaofangfa"] = zhiliao1_s

        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)})


    # 疾病护理
    def jibinghuli(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@class='art-box']/*")
        huli1_s = ""
        for p in p_list:
            huli1_raw = p.xpath(".//text()").extract()
            huli1 = str(huli1_raw).replace("['", "").replace("']", "").replace(" ", "").replace("','",
            "").replace("\\r","").replace("\\n", "").replace("&ldquo;", "").replace("&middot;", "").replace("&rdquo;",
            "").replace("&mdash;", "").replace("\\xa0", "").replace("\\u3000", "")

            huli1_s  = huli1_s + huli1 + "\n"
            item["jibinghuli"] = huli1_s


        yield Request(item["url"], callback=self.parse_one, meta={"item": deepcopy(item)})




    def parse_f(self,response):
        item = response.meta["item"]
        # print(len(list(item.keys())))

        if len(list(item.keys())) ==20:
            print(item)
            # yield item











            # dianxingzhengzhuang_url  = li.xpath("./a[text()='典型症状']/@href").extract_first() #典型症状
            #
            # fabingyuanyin_url = li.xpath("./a[text()='发病原因']/@href").extract_first()  #发病原因
            #
            # jibingyufang_url = li.xpath("./a[text()='预防']/@href").extract_first()  #疾病预防
            #
            # linchuangjiancha_url = li.xpath("./a[text()='临床检查']/@href").extract_first()  #临床检查
            #
            # jianbiezhenduan_url = li.xpath("./a[text()='鉴别']/@href").extract_first() #鉴别诊断
            #
            # zhiliaofangfa_url = li.xpath("./a[text()='治疗方法']/@href").extract_first() #治疗方法
            #
            # jibingzice_url =  li.xpath("./a[text()='疾病自测']/@href").extract_first() #疾病自测
            #
            # jibingtuji_url = li.xpath("./a[text()='疾病图集']/@href").extract_first() #疾病图集
