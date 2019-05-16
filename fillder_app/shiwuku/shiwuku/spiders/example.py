# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['food.boohee.com/']
    start_urls = []

    def start_requests(self):

        for i in range(1, 13):

            for j in range(1, 11):

                url = "http://food.boohee.com/fb/v1/foods?kind=group&value={}&order_by=1&page={}".format(i,j)

                yield Request(url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        item = {}
        food_list_json = json.loads(response.body)
        food_list = food_list_json["foods"]
        for food in food_list:
            code = food["code"]
            # 名称
            item["name"] = food["name"]
            url = "http://food.boohee.com/fb/v1/foods/{}/".format(code)

            yield Request(url, callback=self.parse_disease,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_disease(self, response):
        item = response.meta["item"]
        food_disease = json.loads(response.body)

        # 质量评估
        item["appraise"] = food_disease["appraise"]

        item["calory"] = food_disease["ingredient"]["calory"]
        item["protein"] = food_disease["ingredient"]["protein"]
        item["fat"] = food_disease["ingredient"]["fat"]
        item["carbohydrate"] = food_disease["ingredient"]["carbohydrate"]
        item["fiber_dietary"] = food_disease["ingredient"]["fiber_dietary"]
        item["vitamin_a"] = food_disease["ingredient"]["vitamin_a"]
        item["vitamin_c"] = food_disease["ingredient"]["vitamin_c"]
        item["vitamin_e"] = food_disease["ingredient"]["vitamin_e"]
        item["carotene"] = food_disease["ingredient"]["carotene"]
        item["thiamine"] = food_disease["ingredient"]["thiamine"]
        item["lactoflavin"] = food_disease["ingredient"]["lactoflavin"]
        item["niacin"] = food_disease["ingredient"]["niacin"]
        item["cholesterol"] = food_disease["ingredient"]["cholesterol"]
        item["magnesium"] = food_disease["ingredient"]["magnesium"]
        item["calcium"] = food_disease["ingredient"]["calcium"]
        item["iron"] = food_disease["ingredient"]["iron"]
        item["zinc"] = food_disease["ingredient"]["zinc"]
        item["copper"] = food_disease["ingredient"]["copper"]
        item["manganese"] = food_disease["ingredient"]["manganese"]
        item["kalium"] = food_disease["ingredient"]["kalium"]
        item["phosphor"] = food_disease["ingredient"]["phosphor"]
        item["natrium"] = food_disease["ingredient"]["natrium"]
        item["selenium"] = food_disease["ingredient"]["selenium"]

        item["calory_disease"] = food_disease["lights"]["calory"]
        item["protein_disease"] = food_disease["lights"]["protein"]
        item["fat_disease"] = food_disease["lights"]["fat"]
        url = "http://food.boohee.com/fb/v1/foods/yumi_xian/"
        yield Request(url,callback=self.parse_fin,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_fin(self,response):
        item = response.meta["item"]
        yield item





