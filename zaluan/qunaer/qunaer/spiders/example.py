# -*- coding: utf-8 -*-
import scrapy
import re


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['hotel.qunar.com/']
    start_urls = ["http://hotel.qunar.com/city/shanghai_city/dt-15418/"]
    # def start_requests(self):
    #
    #     base_list = ["shanghai", "beijing"]
    #     for base in base_list:
    #         for i in range(50000):
    #             url = "http://hotel.qunar.com/city/{}_city/dt-{}/".format(base, i)
    #             yield scrapy.Request(url, callback=self.parse, dont_filter=True)


    def parse(self, response):

        # 初始化item
        item = {}
        item["jiudianfuwu"] = ""
        item["jiudiansheshi"] = ""
        item["fangjiansheshi"] = ""
        item["wangluosheshi"] = ""
        item["yudingxuzhi"] = ""
        item["fujiafeiyong"] = ""
        item["ertongzhengce"] = ""
        item["lidianshijian"] = ""
        item["rudianshijian"] = ""
        item["jianjie"] = ""
        item["cenggao"] = ""
        item["cenggao"] = ""
        item["kefangshuliang"] = ""
        item["kaiyeshijian"] = ""
        item["chuanzhen"] = ""
        item["dianhua"] = ""
        item["base_xiangxi"] = ""
        item["base"] = ""
        item["type"] = ""
        item["name"] = ""

        # 酒店名称
        name_raw = response.xpath(
            "//div[@class='hd-container']/div[@class='hd-name-price']//div[@class='hd-name']/div[@class='info']/h1/span[@class='name']/text()").extract()
        name = str(name_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
        item["name"] = name

        #酒店类型
        type_raw = response.xpath(
            "//div[@class='hd-container']/div[@class='hd-name-price']//div[@class='hd-name']/div[@class='info']/h1/span[@class='type']/text()").extract()
        type = str(type_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ", "")
        item["type"] = type

        # 所属区域
        base_raw = response.xpath(
            "//div[@class='hd-container']/div[@class='hd-name-price']//div[@class='hd-name']/div[@class='info']/p[@class='poi']/span[@class='trading']/a/text()").extract()
        base = str(base_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
        item["base"] = base

        # 详细地址
        base_xiangxi_raw = response.xpath(
            "//div[@class='hd-container']/div[@class='hd-name-price']//div[@class='hd-name']/div[@class='info']/p[@class='poi']/span[@class='position js_position']/text()").extract()
        base_xiangxi = str(base_xiangxi_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
        item["base_xiangxi"] = base_xiangxi

        #酒店详情
        detail = response.xpath("//div[@class='hd-bottom']/div[@class='hd-btm-l']/div[@class='hd-detail']")
        dl_list = detail.xpath(".//dl")
        for dl in dl_list:
            text = dl.xpath("./dt/text()").extract_first()
            if text == "联系方式":
                dianhua_raw = dl.xpath("./dd/span[contains(text(),'电话')]/text()").extract()
                dianhua = str(dianhua_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace("电话","")
                item["dianhua"] = dianhua
                chuanzhen_raw = dl.xpath("./dd/span[contains(text(),'传真')]/text()").extract()
                chuanzhen = str(chuanzhen_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace("传真", "")
                item["chuanzhen"] = chuanzhen

            if text == "基本信息":
                # print("*"*20)
                kaiyeshijian_raw = dl.xpath("./dd/span[contains(text(),'开业')]/text()").extract()
                kaiyeshijian = str(kaiyeshijian_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["kaiyeshijian"] = kaiyeshijian

                kefangshuliang_raw = dl.xpath("./dd/span[contains(text(),'客房')]/text()").extract()
                kefangshuliang = str(kefangshuliang_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["kefangshuliang"] = kefangshuliang

                cenggao_raw = dl.xpath("./dd/span[contains(text(),'层')]/text()").extract()
                cenggao = str(cenggao_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["cenggao"] = cenggao

                zhuangxiu_raw = dl.xpath("./dd/span[contains(text(),'装修')]/text()").extract()
                zhuangxiu = str(zhuangxiu_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["cenggao"] = cenggao

                # print(item)

            if text == "酒店简介":
                jianjie_raw = dl.xpath("./dd//text()").extract()
                jianjie = str(jianjie_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["jianjie"] = jianjie

            if text == "入离时间":
                rulitime_raw = dl.xpath("./dd/text()").extract()
                ruzhu_raw = (re.findall("入住时间:(.*?)离店时间", str(rulitime_raw)))[0]
                rudian = ruzhu_raw.replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["rudianshijian"] = rudian

                lidian_raw = (re.findall("离店时间:(.*?)'", str(rulitime_raw)))[0]
                lidian = lidian_raw.replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["lidianshijian"] = lidian

            if text == "儿童政策":
                ertongzhengce_raw = dl.xpath("./dd//text()").extract()
                ertongzhengce = str(ertongzhengce_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["ertongzhengce"] = ertongzhengce
                print(ertongzhengce)

            if text == "附加费用":
                fujiafeiyong_raw = dl.xpath("./dd//text()").extract()
                fujiafeiyong = str(fujiafeiyong_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["fujiafeiyong"] = fujiafeiyong

            if text == "预订须知":
                yudingxuzhi_raw = dl.xpath("./dd//text()").extract()
                yudingxuzhi = str(yudingxuzhi_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["yudingxuzhi"] = yudingxuzhi

            if text == "网络设施":
                wangluosheshi_raw = dl.xpath("./dd//text()").extract()
                wangluosheshi = str(wangluosheshi_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["wangluosheshi"] = wangluosheshi

            if text == "房间设施":
                fangjiansheshi_raw = dl.xpath("./dd//text()").extract()
                fangjiansheshi = str(fangjiansheshi_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["fangjiansheshi"] = fangjiansheshi

            if text == "酒店设施":
                jiudiansheshi_raw = dl.xpath("./dd//text()").extract()
                jiudiansheshi = str(jiudiansheshi_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["jiudiansheshi"] = jiudiansheshi

            if text == "酒店服务":
                jiudianfuwu_raw = dl.xpath("./dd//text()").extract()
                jiudianfuwu = str(jiudianfuwu_raw).replace("['", "").replace("']", "").replace("\\xa0", "").replace(" ","")
                item["jiudianfuwu"] = jiudianfuwu

        # 评分 js
        # pingfen = response.xpath("//div[@class='hd-img-ugc']/div[@class='hd-ugc']/div[@class='hd-ugc-intro']/div[@class='pointer js_comment']/p[@class='score']/span[@class='num']/em/text()").extract()
        # print(pingfen)

        # 地图

        # 床



