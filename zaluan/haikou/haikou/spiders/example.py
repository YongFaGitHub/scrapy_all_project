# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest, Request
import json
from copy import deepcopy
import datetime
import os


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['hainanxf.gov.cn']
    start_urls = []

    def start_requests(self):
        url = 'http://old.hainanxf.gov.cn/wsxf/tousu/findAllByOrgCode.json'
        data = {"orgCode": "460100000012",
                "type": "ldxx"}
        yield FormRequest(url, callback=self.parse,formdata= data)

    def parse(self, response):
        item = {}

        response_dict = json.loads(response.body)
        for one_dict in response_dict["resultData"]:
            bianhao = one_dict["xfjbh"]
            item["bianhao"] = bianhao
            laixinshijian = one_dict["tssj"]
            shijian = int(laixinshijian[:4])
            if shijian >= 2017 and shijian <= 2018:
                laixinneirong = str(one_dict["tsnr"]).replace(" ", "").replace("\n", "").replace("\r",
                                                            "").replace("\u3000", "").replace(",", "，")
                # item["laixin"] = laixinneirong
                banlidanwei = str(one_dict["blfs"]["bljgmc"]).replace(" ", "").replace("\n", "").replace("\r","")
                banlishijian = one_dict["blfs"]["blsj"]
                huifuxingzhi = one_dict["blfs"]["blfsmc"]
                huifuneirong = ""

                s_time = datetime.datetime.strptime(laixinshijian[:10], '%Y-%m-%d')
                e_time = datetime.datetime.strptime(banlishijian[:10], '%Y-%m-%d')
                intime = str((e_time - s_time).days)

                if huifuxingzhi == "直接回复":
                    huifuneirong = str(one_dict["blfs"]["hfgznr"]).replace(" ", "").replace("\n","").replace("\\n",
                                                "").replace("\\r", "").replace("\u3000", "").replace(",", "，")
                    # item["huifuneirong"] = huifuneirong
                    # print(item)

                else:

                    url = "http://old.hainanxf.gov.cn/wsxf/tousu/findXFJByXFJID.json"
                    data = {"xfjId": one_dict["id"]}

                    yield FormRequest(url, callback=self.parse_dateil, dont_filter=True,
                                      formdata=data, meta={"item": deepcopy(item)})

                with open("H:/haikou.csv", "a+", encoding="utf-8") as f:
                    f.write(bianhao + "," +
                            laixinshijian + "," +
                            laixinneirong + "," +
                            banlishijian + "," +
                            banlidanwei + "," +
                            huifuneirong + "," +
                            huifuxingzhi + "," +
                            intime + "\n")

    def parse_dateil(self, response):
        item = response.meta["item"]
        data_list = json.loads(response.body.decode())
        huifuliebiao = data_list["resultData"]["fjs"]
        for one_dict in huifuliebiao:
            file_id = one_dict["id"]
            wenjianming = one_dict["xsmc"]
            item["wenjianming"] = wenjianming

            wenjiandizhi = "http://old.hainanxf.gov.cn/wsxf/tousu/downAffixByBuffer.do?affixId=" + file_id
            yield Request(wenjiandizhi,callback=self.parse_cun, dont_filter=True, meta={"item": deepcopy(item)})

    def parse_cun(self, response):
        item = response.meta["item"]
        try:
            os.mkdir("H:/海口/{}".format(item["bianhao"]))
        except:pass

        with open("H:/海口/{}/{}".format(item["bianhao"], item["wenjianming"]), "wb", ) as f:
            f.write(response.body)
