# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import re


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.xiangha.com']
    start_urls = ['http://www.xiangha.com/shicai/']
    # start_urls = []

    # def start_requests(self):
    #     url = 'http://fetch.bestzsj.com/v1/validate_ip_https'
    #     yield Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        item = {"biaoshi": 0}
        #
        # xiangke_url = "https://www.xiangha.com/xiangke/38674"
        # yield Request(xiangke_url, callback=self.parse_xiangke,
        #               dont_filter=True, meta={"item": deepcopy(item)})

        # print(response.status,"#######")

        # 为后续工作初始化几个字段

        div_list = response.xpath("//div[@class='rec_classify_con']/div")
        for div in div_list:
            big_class = div.xpath('./h3/a/text()').extract_first()
            ul_list = div.xpath("./ul")
            item["big_class"] = big_class

            for ul in ul_list:
                small_class = ul.xpath("./li[1]/strong/a/text()").extract_first()
                item["small_class"] = small_class
                href_url = ul.xpath("./li[1]/strong/a/@href").extract_first()

                yield Request(href_url, callback=self.parse_detail,
                              dont_filter=True, meta={"item": deepcopy(item)})

    # 进入某一小类的分类
    def parse_detail(self, response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@class='cla_ing_info']/div[@class='cla_ing_i_list']/ul/li")
        for li in li_list:
            title = li.xpath("./div[@class='ins']/p[@class='name']/a/@title").extract_first()
            item["title"] = title

            url = li.xpath("./a/@href").extract_first()  # 某一食材的详细地址
            yield Request(url, callback=self.parse_one,
                          dont_filter=True, meta={"item": deepcopy(item)})

        next_page = response.xpath("//div[@class='cla_ing_info']//a[text()='下一页']/@href").extract_first()
        if next_page is not None:
            next_url = next_page
            # 调用本函数，进行解析下一页的列表
            yield Request(next_url, callback=self.parse_detail,
                          dont_filter=True, meta={"item": deepcopy(item)})

    def parse_one(self, response):
        item = response.meta["item"]
        try:
            yuansu = response.xpath("//div[@class='list_tab clearfix']/h2/span[2]")
            yuansu_text = yuansu.xpath("./a/text()").extract_first()
            if "功效与作用" in yuansu_text:
                yuansu_url = yuansu.xpath("./a/@href").extract_first()  # 食材的微量元素的接口
                # yuansu_url = "https://www.xiangha.com/shicai/%E5%92%B8%E9%B8%AD%E8%9B%8B"
                yield Request(yuansu_url, callback=self.parse_yuansu,
                              dont_filter=True, meta={"item": deepcopy(item)})

            if "相克" in yuansu_text:  # 判断是不是会出现第二个是相克的网址信息
                xiangke_url = yuansu.xpath("./a/@href").extract_first()
                yield Request(xiangke_url, callback=self.parse_xiangke,
                              dont_filter=True, meta={"item": deepcopy(item)})
        except:
            print("本食材只有简介，无其他内容")

        try:
            xiangke = response.xpath("//div[@class='list_tab clearfix']/h2/span[3]")
            xiangke_text = xiangke.xpath("./a/text()").extract_first()
            if "相克" in xiangke_text:
                xiangke_url = xiangke.xpath("./a/@href").extract_first()  # 食材的相克入口
                # xiangke_url = "https://www.xiangha.com/xiangke/39898"
                yield Request(xiangke_url, callback=self.parse_xiangke,
                              dont_filter=True, meta={"item": deepcopy(item)})
        except:
            pass

    # 获得微量元素
    def parse_yuansu(self, response):
        item = response.meta["item"]
        # 定义一个列表 包含所有的想要拿到的信息
        name_list = ["热量", "蛋白质", "脂肪",
                     "碳水化合物", "膳食纤维", "维生素A",
                     "胡萝卜素", "维生素B1", "维生素B2",
                     "胆固醇",
                     "烟酸", "维生素C", "维生素E",
                     "维生素B6",
                     "钙", "磷", "钾",
                     "钠", "镁", "铁",
                     "锌", "硒", "铜",
                     "锰", "水"]
        # 建立一个列表 对应上面的名称列表，进行对字段的定义， 已经重构完成
        name_ying_list = ["reliang", "danbaizhi", "zhifang", "tanshui", "qianwei",
                          "va", "huluobosu", "vb1", "vb2", "danguchun",
                          "yansuan", "vc", "ve", "vb6",
                          "ca", "p", "ka", "na", "mei", "tie",
                          "zn", "xi", "tong", "mn", "shui"]

        # 初始化item

        for name_ying in name_ying_list:
            item[name_ying] = ""

        li_list = response.xpath("//div[@class='info']/ul/li")
        if len(li_list) > 0:  # 判断是否有微量元素的存在
            for li in li_list:
                text = li.xpath("./span/a/text()").extract_first()
                # 在以下匹配 所有的微量元素 对应所有的字段
                if text in name_list:
                    title = name_ying_list[name_list.index(text)]
                    item[title] = li.xpath("./em/text()").extract_first()
            item["biaoshi"] = 1
            yield item

    def parse_xiangke(self, response):

        item = response.meta["item"]

        xiangke_tr_list = []
        xiangyi_tr_list = []

        # 分别获得所有的 相宜 相克的列表
        tr_list_all = response.xpath("//div[@class='ing_tips tab_con']//tr")  # 获得所有的tr标签，包含相克相宜
        tr_xiangke = response.xpath("//div[@class='ing_tips tab_con']//tr/th[@id='xiangke']")
        tr_xiangyi = response.xpath("//div[@class='ing_tips tab_con']//tr/th[@id='yida']")
        if len(tr_xiangke) > 0:
            if len(tr_xiangyi) > 0:
                # 在相宜相克都存在的情况下

                # 先将相宜的本次进行返回，后续不需要处理本次
                f_one_xiangyi_raw = tr_xiangyi.xpath("../td//text()").extract()
                f_one_xiangyi = str(f_one_xiangyi_raw).replace("['", "").replace("']",
                                "").replace(" ", "").replace("','", "").replace("查看菜谱>>", "")
                item["query"] = f_one_xiangyi
                item["ke_yi"] = 1
                # item["xiangyishicai"] = re.findall("\+(.*?)：", f_one_xiangyi)[0]
                # item["xiangyiyuanyin"] = re.findall("：(.*)", f_one_xiangyi)[0]
                # item["xiangkeshicai"] = ""
                # item["xiangkeyuanyin"] = ""

                xiangke_tr_list = tr_xiangyi.xpath("../preceding-sibling::tr")  # 包含第一个

                # 获取到所有的相宜食材
                xiangyi_tr_list = tr_xiangyi.xpath("../following-sibling::*")  # 获得(相宜)tr所有的后邻兄弟节点 不包含自己

                yield item  # 现将本次的数据返回
                # print(item, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

            else:
                # 在相克存在 相宜没有的情况下
                xiangke_tr_list = tr_xiangke.xpath("../following-sibling::tr")

                # 现将本次的相克数据返回
                f_one_xiangke_raw = tr_xiangke.xpath("../td//text()").extract()
                f_one_xiangke = str(f_one_xiangke_raw).replace("['", "").replace("']", "").replace(" ",
                                "").replace("','", "")
                item["query"] = f_one_xiangke
                item["ke_yi"] = 0

                # item["xiangyishicai"] = ""
                # item["xiangyiyuanyin"] = ""
                # item["xiangkeshicai"] = re.findall("\+(.*?)：", f_one_xiangke)[0]
                # item["xiangkeyuanyin"] = re.findall("：(.*)", f_one_xiangke)[0]

                yield item  # 先将所有的相克的本条数据
                # print(item, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        elif len(tr_xiangyi) > 0:
            # 在相宜存在 相克没有的情况下
            xiangyi_tr_list = tr_xiangyi.xpath("../following-sibling::tr")

            # 先将相宜的本次进行返回，后续不需要处理本次
            f_one_xiangyi_raw = tr_xiangyi.xpath("../td//text()").extract()
            f_one_xiangyi = str(f_one_xiangyi_raw).replace("['", "").replace("']","").replace(" ", "").replace("','",
                                "").replace("查看菜谱>>", "")
            item["query"] = f_one_xiangyi
            item["ke_yi"] = 1


            # item["xiangyishicai"] = re.findall("\+(.*?)：", f_one_xiangyi)[0]
            # item["xiangyiyuanyin"] = re.findall("：(.*)", f_one_xiangyi)[0]
            # item["xiangkeshicai"] = ""
            # item["xiangkeyuanyin"] = ""
            yield item  # 现将本次的数据返回
            # print(item, "################################")

        else: pass  # 都没有的情况下

        # 获得到的所有的相宜的列表
        if len(xiangyi_tr_list) > 0:
            for xiangyi in xiangyi_tr_list:
                xiangyi_text_raw = xiangyi.xpath("./td//text()").extract()
                xiangyi_text = str(xiangyi_text_raw).replace("['", "").replace("']",
                            "").replace(" ", "").replace("','", "").replace("查看菜谱>>", "")

                item["query"] = xiangyi_text
                item["ke_yi"] = 1
                # item["xiangyishicai"] = re.findall("\+(.*?)：", xiangyi_text)[0]
                # item["xiangyiyuanyin"] = re.findall("：(.*)", xiangyi_text)[0]
                # item["xiangkeshicai"] = ""
                # item["xiangkeyuanyin"] = ""
                yield item  # 返回列表的相宜信息
                # print(item, "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        # 获得的所有的相克的列表信息
        if len(xiangke_tr_list) > 0:
            for xiangke in xiangke_tr_list:
                xiangke_text_raw = xiangke.xpath("./td//text()").extract()
                xiangke_text = str(xiangke_text_raw).replace("['", "").replace("']", "").replace(" ",
                            "").replace("','", "")

                item["query"] = xiangke_text
                item["ke_yi"] = 0

                # item["xiangyishicai"] = ""
                # item["xiangyiyuanyin"] = ""
                # item["xiangkeshicai"] = re.findall("\+(.*?)：", xiangke_text)[0]
                # item["xiangkeyuanyin"] = re.findall("：(.*)", xiangke_text)[0]
                yield item  # 返回列表的相克信息
                # print(item,"%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^")

