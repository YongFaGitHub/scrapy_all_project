# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,FormRequest
from copy import deepcopy
import csv
import re


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['foodwake.com/']
    start_urls = ["http://www.foodwake.com/search/all"]

    def parse(self, response):
        item = {}

        key = re.findall('<meta name="_token" content="(.*?)">', response.body.decode())

        file = open("F:/知识图谱/all_data/base_name.csv", "rt", encoding="utf-8")
        read = csv.reader(file)
        for line in read:
            if line[1] == "nf":
                item["query"] = line[0]

                data = {"key": line[0],
                        "_token": key[0]
                        }

                yield FormRequest(url="http://www.foodwake.com/search/food",
                                  formdata=data, callback=self.parse_query,
                                  dont_filter=True, meta={"item": deepcopy(item)})

        # data = {"key": "黄精",
        #         "_token": key[0]
        #         }
        # item["query"] = "黄精"
        # yield FormRequest(url="http://www.foodwake.com/search/food",
        #                   formdata=data, callback=self.parse_query,
        #                   dont_filter=True, meta={"item": deepcopy(item)})

    def parse_query(self, response):
        item = response.meta["item"]

        query_tr_list = response.xpath("//div[@class='col-12']/table/tbody/tr")
        for query_tr in query_tr_list:
            name = query_tr.xpath("./td[1]/a/text()").extract_first()
            if name == item["query"]:
                url = query_tr.xpath("./td[1]/a/@href").extract_first()

                yield Request(url, callback=self.parse_datil, dont_filter=True, meta={"item": deepcopy(item)})
                break

    def parse_datil(self, response):
        item = response.meta["item"]
        # print(response.body.decode())
        food_ying_list = re.findall('var food = (.*?);', response.body.decode())
        food_score_list = re.findall('var score = (.*?);', response.body.decode())

        if len(food_ying_list) > 1:
            # 食物营养元素的字典
            food_ying_dict = eval(food_ying_list[0].replace("null", '0'))
            food_score_dict = eval(food_score_list[0].replace("null", '0'))
            # print(food_ying_dict)
            # print(food_score_dict)

            # 食物营养元素的含量和得分  每一百克 所含的量

            # 基本营养
            # 能量 千卡
            item["kcal"] = food_ying_dict["kcal"]
            item["kcal_fen"] = food_score_dict["kcal"]

            # 蛋白质 克
            item['protein'] = food_ying_dict['protein']
            item['protein_fen'] = food_score_dict['protein']

            # 脂肪 克
            item['fat'] = food_ying_dict['fat']
            item['fat_fen'] = food_score_dict['fat']

            # 碳水化合物 克
            item['carbo'] = food_ying_dict['carbo']
            item['carbo_fen'] = food_score_dict['carbo']

            # 粗纤维 克
            item['fibre'] = food_ying_dict['fibre']
            item['fibre_fen'] = food_score_dict['fibre']

            # 脂类
            # 单不饱和脂肪酸 克
            item['mufas'] = food_ying_dict['mufas']
            item['mufas_fen'] = food_score_dict['mufas']

            # 多不饱和脂肪酸 克
            item['pufas'] = food_ying_dict['pufas']
            item['pufas_fen'] = food_score_dict['pufas']

            # 多不饱和脂肪酸占总脂肪酸的比例 %
            item['pufas_percent'] = food_ying_dict['pufas_percent']
            item['pufas_percent_fen'] = food_score_dict['pufas_percent']

            # 反式脂肪酸 克
            item['tfa'] = food_ying_dict['tfa']
            item['tfa_fen'] = food_score_dict['tfa']

            # 反式脂肪酸占总脂肪酸的比例 %
            item['tfa_percent'] = food_ying_dict['tfa_percent']
            item['tfa_percent_fen'] = food_score_dict['tfa_percent']

            # 胆固醇 毫克
            item['cholesterol'] = food_ying_dict['cholesterol']
            item['cholesterol_fen'] = food_score_dict['cholesterol']

            # 植物固醇 毫克
            item['phytosterol'] = food_ying_dict['phytosterol']
            item['phytosterol_fen'] = food_score_dict['phytosterol']

            # 胡萝卜素  微克
            item['carotene'] = food_ying_dict['carotene']
            item['carotene_fen'] = food_score_dict['carotene']

            # 叶黄素类 微克
            item['l_z_c'] = food_ying_dict['l_z_c']
            item['l_z_c_fen'] = food_score_dict['l_z_c']

            # 番茄红素 微克
            item['lycopene'] = food_ying_dict['lycopene']
            item['lycopene_fen'] = food_score_dict['lycopene']

            # 矿物质
            # 钙 毫克
            item['ca'] = food_ying_dict['ca']
            item['ca_fen'] = food_score_dict['ca']

            # 镁 毫克
            item['mg'] = food_ying_dict['mg']
            item['mg_fen'] = food_score_dict['mg']

            # 钠 毫克
            item['na'] = food_ying_dict['na']
            item['na_fen'] = food_score_dict['na']

            # 钾 毫克
            item['k'] = food_ying_dict['k']
            item['k_fen'] = food_score_dict['k']

            # 磷 毫克
            item['p'] = food_ying_dict['p']
            item['p_fen'] = food_score_dict['p']

            # 硫 毫克
            item['s'] = food_ying_dict['s']
            item['s_fen'] = food_score_dict['s']

            # 氯 毫克
            item['cl'] = food_ying_dict['cl']
            item['cl_fen'] = food_score_dict['cl']

            # 铁 毫克
            item['fe'] = food_ying_dict['fe']
            item['fe_fen'] = food_score_dict['fe']

            # 碘 微克
            item['i'] = food_ying_dict['i']
            item['i_fen'] = food_score_dict['i']

            # 锌 毫克
            item['zu'] = food_ying_dict['zu']
            item['zu_fen'] = food_score_dict['zu']

            # 硒 微克
            item['se'] = food_ying_dict['se']
            item['se_fen'] = food_score_dict['se']

            # 铜 毫克
            item['cu'] = food_ying_dict['cu']
            item['cu_fen'] = food_score_dict['cu']

            # item['mo'] = food_ying_dict['mo']
            # item['mo'] = food_score_dict['mo']
            #
            #
            # item['cr'] = food_ying_dict['cr']
            # item['cr'] = food_score_dict['cr']
            #
            #
            # item['co'] = food_ying_dict['co']
            # item['co'] = food_score_dict['co']

            # 锰 毫克
            item['mn'] = food_ying_dict['mn']
            item['mn_fen'] = food_score_dict['mn']

            # 氟 微克
            item['f'] = food_ying_dict['f']
            item['f_fen'] = food_score_dict['f']

            # item['ni'] = food_ying_dict['ni']
            # item['ni'] = food_score_dict['ni']
            #
            #
            # item['sn'] = food_ying_dict['sn']
            # item['sn'] = food_score_dict['sn']
            #
            #
            # item['si'] = food_ying_dict['si']
            # item['si'] = food_score_dict['si']
            #
            #
            # item['v'] = food_ying_dict['v']
            # item['v'] = food_score_dict['v']

            # 维生素A 微克
            item['va'] = food_ying_dict['va']
            item['va_fen'] = food_score_dict['va']

            # 维生素C 毫克
            item['vc'] = food_ying_dict['vc']
            item['vc_fen'] = food_score_dict['vc']

            # 维生素D 微克
            item['vd'] = food_ying_dict['vd']
            item['vd_fen'] = food_score_dict['vd']

            # 维生素E 毫克
            item['ve'] = food_ying_dict['ve']
            item['ve_fen'] = food_score_dict['ve']

            # 维生素K 微克
            item['vk'] = food_ying_dict['vk']
            item['vk_fen'] = food_score_dict['vk']

            # 维生素P（类黄酮） 毫克
            item['vp'] = food_ying_dict['vp']
            item['vp_fen'] = food_score_dict['vp']

            # 维生素B1（硫胺素） 毫克
            item['b1'] = food_ying_dict['b1']
            item['b1_fen'] = food_score_dict['b1']

            # 维生素B2 （核黄素）  毫克
            item['b2'] = food_ying_dict['b2']
            item['b2_fen'] = food_score_dict['b2']

            # 维生素B3（烟酸）  毫克
            item['b3'] = food_ying_dict['b3']
            item['b3_fen'] = food_score_dict['b3']

            # 维生素B4（胆碱） 毫克
            item['b4'] = food_ying_dict['b4']
            item['b4_fen'] = food_score_dict['b4']

            # 维生素B5（泛酸） 毫克
            item['b5'] = food_ying_dict['b5']
            item['b5_fen'] = food_score_dict['b5']

            # 维生素B6 毫克
            item['b6'] = food_ying_dict['b6']
            item['b6_fen'] = food_score_dict['b6']

            # 维生素B7（生物素） 微克
            item['b7'] = food_ying_dict['b7']
            item['b7_fen'] = food_score_dict['b7']

            # 维生素B9（叶酸） 微克
            item['b9'] = food_ying_dict['b9']
            item['b9_fen'] = food_score_dict['b9']

            # 维生素B12 微克
            item['b12'] = food_ying_dict['b12']
            item['b12_fen'] = food_score_dict['b12']

            # 维生素B14（甜菜碱） 毫克
            item['b14'] = food_ying_dict['b14']
            item['b14_fen'] = food_score_dict['b14']

            # 氨基酸
            # 亮氨酸
            item['leu'] = food_ying_dict['leu']
            item['leu_fen'] = food_score_dict['leu']

            # 蛋氨酸 毫克
            item['met'] = food_ying_dict['met']
            item['met_fen'] = food_score_dict['met']

            # 苏氨酸 毫克
            item['thr'] = food_ying_dict['thr']
            item['thr_fen'] = food_score_dict['thr']

            # 赖氨酸 毫克
            item['lys'] = food_ying_dict['lys']
            item['lys_fen'] = food_score_dict['lys']

            # 色氨酸 毫克
            item['trp'] = food_ying_dict['trp']
            item['trp_fen'] = food_score_dict['trp']

            # 缬氨酸 毫克
            item['val'] = food_ying_dict['val']
            item['val_fen'] = food_score_dict['val']

            # 组氨酸 毫克
            item['his'] = food_ying_dict['his']
            item['his_fen'] = food_score_dict['his']

            # 异亮氨酸 毫克
            item['ile'] = food_ying_dict['ile']
            item['ile_fen'] = food_score_dict['ile']

            # 苯丙氨酸 毫克
            item['phe'] = food_ying_dict['phe']
            item['phe_fen'] = food_score_dict['phe']

            # # 半胱氨酸 毫克
            # item['cys'] = food_ying_dict['cys']
            # item['cys'] = food_score_dict['cys']

            # 酸碱初始化
            item['1_level'] = 0
            item["1_value"] = 0
            item['0_level'] = 0
            item["0_value"] = 0

            # 酸碱性
            if food_ying_dict['aa_switch'] == 1:
                item["aa_switch"] = "碱性"
                # 酸碱等级
                item['1_level'] = food_ying_dict['aa_level']
                # 酸碱值
                item["1_value"] = food_ying_dict['aa_value']

            if food_ying_dict['aa_switch'] == 0:
                item["aa_switch"] = "酸性"
                # 酸碱等级
                item['0_level'] = food_ying_dict['aa_level']
                # 酸碱值
                item["0_value"] = food_ying_dict['aa_value']
            # print('################################################')
            # print(item)
            yield item