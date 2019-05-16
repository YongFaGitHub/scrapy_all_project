# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from copy import deepcopy

# 1，部位，2，大类名 3，详情，详情页的数据

#  注意点进url链接时的 地址可能为空!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['jbk.39.net/']
    start_urls = ['http://jbk.39.net/']

    def parse(self, response):
        items = {}
        dl_list = response.xpath("//div[@class='mapList']/dl")
        # print(url_list)
        # print("*"*100)
        #拿到部位
        for dl in dl_list:
            position_list =dl.xpath("./dd/div[1]/ul/li")
            for position in position_list:
                positions_raw = position.xpath("./span[@class='left']/a/text()").extract_first()  #部位
                positions = str(positions_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '').replace("[", "").replace("]", "")
                # print(type(positions))
                # print(positions_raw,"######")
                items["position"] = positions
                title_list = position.xpath("./span[@class='right']/a") #病症列表
                for title in title_list:
                    items["title"] =title.xpath("./text()").extract_first()# 拿到标题
                    url = title.xpath("./@href").extract()[0]#拿到标题的url
                    print(url) #网址没问题

                    yield Request(url,callback=self.parse_one,meta={"items":deepcopy(items)},dont_filter=True)


    def parse_one(self,response):

        items = response.meta["items"]
        #找到详情（details）的url,    可能没有详情！！！！！！！！！！！！！！！！！！！
        # 有详情的网页才=会进入
        details_url = response.xpath("//dl[@class='intro']/dd/a/@href").extract()[0]  #详情的url地址,里面包括想要获得的数据
        if details_url is not None:
            pass
            # yield Request(details_url,callback=self.parse_two,meta={"items":deepcopy(items)},dont_filter=True)
        print("###########")
         #没有详情的网页，不进入，拿到介绍后返回

        # print(Exception, ":",e)
        # #处理无详情链接的页面
        # details_raw = response.xpath("//dl[@class='intro']/dd/text()").extract()
        # details = str(details_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '').replace("[", "").replace("]", "")
        # items["details"] = details
        # items["basic"]="暂无"
        # items["diagnosis"] = "暂无"
        # items["Hospital_must_read"] = "暂无"
        # yield items
        # items["bingfajibing"] = "暂无"
        # items["xiangguanzhengzhuang"] = "暂无"
        # # yield items

    def parse_two(self,response):

        #进入详情页的后续操作
        print("**"*20)
        items = response.meta["items"]
        details_list = response.xpath("//div[@class='chi-know']")
        #病症详情没问题
        details_raw = details_list.xpath("./dl[1]/dd/text()").extract()
        details = str(details_raw).replace('\\t', '').replace('\\r', '').replace('\\n','').replace("'","").replace(" ","").replace("\\u3000","").replace("[详细]","").replace("[", "").replace("]", "")
        items["details"] = details#病症详情
        #基础知识
        basic_raw = details_list.xpath("./dl[2]/dd//text()").extract()
        basic = str(basic_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '').replace("'", "").replace(" ","").replace("[详细]","").replace("[", "").replace("]", "")
        items["basic"] = basic

        #诊断：diagnosis
        #诊疗知识没问题
        diagnosis_raw = details_list.xpath("./dl[3]/dd//text()").extract()
        diagnosis = str(diagnosis_raw).replace('\\t', '').replace('\\r', '').replace('\\n','').replace("'","").replace(" ","").replace("[详细]","").replace("[", "").replace("]", "")
        items["diagnosis"] = diagnosis #诊疗知识

        # 就医必读没问题
        hospital_must_read_raw = details_list.xpath("./dl[4]/dd//text()").extract()
        hospital_must_read = str(hospital_must_read_raw).replace('\\t', '').replace('\\r', '').replace('\\n','').replace("'","").replace(" ","").replace("[详细]","").replace(",,了解更多就诊知识>>","").replace("[", "").replace("]", "")
        items["Hospital_must_read"] = hospital_must_read #就医必读
        yield items


