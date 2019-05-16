# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,FormRequest
import json
import re
import csv
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['baike.baidu.com']
    start_urls = ["https://baike.baidu.com/guanxi/jsondata?action=getViewLemmaData&args=%5B0%2C8%2C%7B%22fentryTableId%22%3A35446%2C%22lemmaId%22%3A245744%2C%22subLemmaId%22%3A245744%7D%2Cfalse%5D"]

    def parse(self, response):
        item = {}  # 存放处理完成的数据
        dict_name = {}
        item_name = []
        file = open("F:/pycharmproject/project/baidu/baikezheng190320/baikezheng190320/spiders/name1.csv", "rt", encoding="utf-8")

        read = csv.reader(file)

        for line in read:
            dict_name[line[0]] = line[1]
            if line[1] not in item_name:
                item_name.append(line[1])
        for item_name_one in item_name:
            item[item_name_one] = ""  # 初始化

        r = json.loads(response.body)
        r_list = re.findall('href=\"(.*?)"', str(r), re.S)

        b = r_list.index("http://baike.baidu.com/view/838756.htm")

        for i in range(b, len(r_list)):
            href = r_list[i]
            # href = "https://baike.baidu.com/item/%E9%98%B3%E6%98%8E%E7%97%85%E8%AF%81"
            yield Request(href, callback=self.parse_details, dont_filter=True, meta={
                "dict_name": deepcopy(dict_name), "item": deepcopy(item)})

    def parse_details(self, response):
        dict_name = response.meta["dict_name"]  # 名称对应字典
        item = response.meta["item"]
        dict_title = {}  # 二级标题的对应的位置的字典

        title = response.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()").extract_first()
        item["title"] = title

        li_list = response.xpath("//div[@class='lemma-catalog']/div/ol/li[@class='level1']")
        for li in li_list:
            text = li.xpath("./span[@class='text']/a/text()").extract_first()  # 拿到所有的二级标题
            # 拿到二级标题对应的快内容
            title_number = li.xpath("./span[@class='text']/a/@href").extract_first().replace("#", "")
            try:
                dict_title[title_number] = dict_name[text]  # 获得二级标题在目录中的第几位
            except:
                dict_title[title_number] = "暂不存储"

        # text = response.xpath("//a[@name='6']/following-sibling::*[following::a[@name='常用中药']]").extract()
        print(dict_title)
        for i in range(len(dict_title)):
            title_data_list = []
            title_data_str = ""
            i = i + 1
            if i == len(dict_title):   # 最后一个标签开始遍历，结束条件与平常情况不同
                select_choices = response.xpath(
                    "//a[@name={}]/../following-sibling::*[following::div[@class='rs-container-foot']]".format(i))

            else:  # 平常情况下按照标准的判断进行获取
                select_choices = response.xpath(
                    "//a[@name={}]/../following-sibling::*[following::div[@class='anchor-list']/a[@name={}]]".format(i,
                                                                                                                     i+1))
            for one_text in select_choices:
                one_text_text = one_text.xpath(".//text()").extract()
                title_data_list.append(one_text_text)
            for title_data_one in title_data_list[1:]:

                title_data_one_deal = str(title_data_one).replace("[", "").replace("]",
                "").replace(" ", "").replace("','", "").replace("\\n", "").replace("'", "").replace("\\xa0",
                "").replace("1-2", "")
                if "1-" in title_data_one_deal:
                    pass
                else:
                    if len(title_data_one_deal) > 0:
                        title_data_str += title_data_one_deal + "\n"

            item[dict_title[str(i)]] = title_data_str
        yield item
