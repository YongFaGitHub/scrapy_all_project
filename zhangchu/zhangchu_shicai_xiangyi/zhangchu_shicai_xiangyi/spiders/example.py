# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, FormRequest
from copy import deepcopy
import json
import re
from pymysql import *

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['api.izhangchu.com/']
    start_urls = []

    def start_requests(self):
        url = "http://api.izhangchu.com/"

        form_data = {
            "methodName": "MaterialSubtype",
            "verson": "5.3.0"
        }
        yield FormRequest(url, callback=self.parse, formdata=form_data, dont_filter=True)

    def parse(self, response):
        item = {}
        data_list_json = json.loads(response.body)
        data_list_raw = data_list_json["data"]["data"]
        data_class_list = data_list_raw[2:]
        for data_class in data_class_list:
            item["class_name"] = (data_class["text"])
            data_small_list = data_class["data"]
            for data in data_small_list:
                item["title"] = data["text"]
                id = data["id"]
                formdata = {
                    "material_id": id,
                    "methodName": "MaterialView",
                    "token": "9B79FAD3D54F21FA267C0A89E91E38AF",
                    "user_id": "2672290",
                    "version": "4.4.0"
                }
                yield FormRequest("http://api.izhangchu.com/",
                                  callback=self.parse_details,
                                  meta={"item": deepcopy(item)},
                                  formdata=formdata,
                                  dont_filter=True)

    def parse_details(self, response):

        conn = connect(host='127.0.0.1',
                       port=3306,
                       database='shicaidata',
                       user='root',
                       password='jing1995',
                       charset='utf8')
        cs1 = conn.cursor()

        item = response.meta["item"]
        data_raw = re.findall("【搭配宜忌】(.*?)\",", response.body.decode())

        if len(data_raw) > 0:  # 如果有适宜禁忌内容
            # 处理多余字符
            data_long = str(data_raw[0]).replace("\\r\\n", "").replace("相宜", "").replace(' ', "")
            # 初始化
            yi_name = ""
            yi_t = ""
            ke_name = ""
            ke_t = ""

            data_yi_ke_list = re.split("相克", data_long)
            if len(data_yi_ke_list) == 2:
                yi_list = (data_yi_ke_list[0]).split(item["title"])
                ke_list = (data_yi_ke_list[1]).split(item["title"])
                print(yi_list, ke_list)
                for i in yi_list:
                    if len(i) > 0:
                        yi_name = re.findall("\+(.*?)=", i)[0]
                        yi_t = re.findall("=(.*)", i)[0]
                        cs1.execute(
                            "insert into zhangchu_yiji(calss_name, title, xiangyishicai, xiangyiyuanyin) values(%s, %s, %s, %s)"
                            , (item["class_name"], item["title"], yi_name, yi_t))
                        conn.commit()
                for j in ke_list:
                    if len(j) > 0:
                        ke_name = re.findall("\+(.*?)=", j)[0]
                        ke_t = re.findall("=(.*)", j)[0]

                        cs1.execute(
                            "insert into zhangchu_yiji(calss_name, title, xiangkeshicai, xiangkeyuanyin) values(%s, %s, %s, %s)"
                            , (item["class_name"], item["title"], ke_name, ke_t))
                        conn.commit()







