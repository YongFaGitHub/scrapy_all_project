# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['club.xywy.com/']
    start_urls = []

    def start_requests(self):

        #问答的日期页面
        # for i in range(44, 45):
        #     url = "http://club.xywy.com/keshi/{}.html".format(i)0
        #     yield Request(url,callback=self.parse,dont_filter=True)
        for i in range(1, 32):
            if len(str(i)) == 1:
                i = "0" + str(i)
            item = {}
            # url = "http://club.xywy.com/keshi/{}.html".format(i)
            url_d = "http://club.xywy.com/keshi/2007-12-{}/1.html".format(i)
            item["qian"] = url_d.replace("1.html", "")
            yield Request(url_d, callback=self.parse, dont_filter=True, meta={"item": deepcopy(item)})

    # def parse(self, response):
    #     item={}
    #
    #     #问答的日期页面的进入
    #     li_list = response.xpath("//ul[@class='club_Date clearfix']/li")
    #     for li in li_list:
    #         url  = li.xpath("./a/@href").extract_first()
    #         item["qian"] = url.replace("1.html","")
    #         yield Request(url,callback=self.parse_list,meta={"item":deepcopy(item)},dont_filter=True)

    def parse(self, response):
        item = response.meta["item"]
        #问答的列表页
        div_list = response.xpath("//div[@class='bc mt15 DiCeng']/div[@class='club_dic']")
        for div in div_list:
            #进入详情页
            disease_url = div.xpath("./h4/em/a/@href").extract_first()
            yield Request(disease_url,callback=self.parse_disease,dont_filter=True,meta={"item":deepcopy(item)})
        try:
            next_url_raw = response.xpath("//div[@class='club_page']/div/a[text()='[下一页]']/@href").extract_first()
            next_url = item["qian"] + next_url_raw
            # print(next_url)
            yield Request(next_url,callback=self.parse,dont_filter=True,meta={"item":deepcopy(item)})

        except:pass
            # print("无下一页")


    def parse_disease(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//p[@class='pt10 pb10 lh180 znblue normal-a']")

        big_title_raw = p_list.xpath("./a[3]/text()").extract_first()
        item["big_title"] = big_title_raw

        title_raw =  p_list.xpath("./a[4]/text()").extract_first()
        item["title"] = title_raw

        question_raw = response.xpath("//div[@class='graydeep User_quecol pt10 mt10']/text()").extract()
        question = str(question_raw).replace("\\r","").replace("\\t","").replace("\\n","").replace("['",
        "").replace("']","").replace("[","").replace("]","").replace(" ","").replace("','",
        "").replace("\\u3000","").replace(",","，").replace("请输入您的健康疑问，点击“我要提问”来获得全国各地百名知名专家回复。",
        "").replace("你好，","").replace("??","?").replace("!!!","!").replace(">>>>-","").replace(">>>>",
        "").replace("你好，","").replace("你好！","").replace("你好!","").replace("你好：","").replace("你好。",
        "").replace("您好:","").replace("你好1","").replace("请帮助","").replace("00","").replace("您好，",
        "").replace("请问一下，","").replace("111","").replace("医生你好:","").replace("医生：","").replace("医生你好，",
        "").replace("请问医生，","").replace("。，","。").replace("输入您的问题","")
        if len(question) >1:
            item["question"] = question
        else:
            title2_raw = p_list.xpath("./text()").extract()
            title2 = str(title2_raw).replace("['","").replace("']","").replace(" ","").replace("\\r",
            "").replace("\\t","").replace("\\n","").replace("','","")
            item["question"] = title2

        answer_list = response.xpath("//div[@class='docall clearfix ']/div[2]/div[2]/div[1]")
        if answer_list is not None:
            answer_s = ""
            for an in answer_list:
                answer_raw = an.xpath("./text()").extract()
                answer = str(answer_raw).replace("']","").replace("['","").replace("\\u3000","").replace(" ",
                "").replace("','","").replace("[","").replace("]","").replace(",","，").replace("\\r",
                "").replace("\\t","").replace("\\n","").replace("你好，","").replace("你好！","").replace("你好!",
                "").replace("您好，","").replace('朋友好!',"").replace("朋友好！","").replace("你好:",
                "").replace("你好：","").replace("你好。","").replace("您好:","").replace("你好1","").replace("这位朋友您好：",
                "").replace("。，","。").replace("您好！","").replace("您好!","")
                if len(answer)> 2 :
                    answer_f =answer +","
                    answer_s = answer_s + answer_f
            if len(answer_s) >3:
                item["answer"] = answer_s[:-2]

        yield item