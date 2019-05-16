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
                items['position'] = positions
                title_list = position.xpath("./span[@class='right']/a") #病症列表
                for title in title_list:
                    # items["title"] =title.xpath("./text()").extract_first()# 拿到标题
                    url = title.xpath("./@href").extract()[0]#拿到标题的url
                    # print(url) 网址没问题
                    yield Request(url,callback=self.parse_one,meta={"items":deepcopy(items)},dont_filter=True)

    #
    def parse_one(self,response):

        items = response.meta["items"]
    #     #找到详情（details）的url,    可能没有详情！！！！！！！！！！！！！！！！！！！
    #     try:  # 有详情的网页才=会进入
        details_url = response.xpath("//dl[@class='intro']/dd/a/@href").extract()[0]  #详情的url地址,里面包括想要获得的数据
        yield Request(details_url,callback=self.parse_two,meta={"items":deepcopy(items)},dont_filter=True)
    #      #没有详情的网页，不进入，拿到介绍后返回
    #     except Exception as e :
    #         print(Exception, ":",e)
    #         #处理无详情链接的页面
    #         details_raw = response.xpath("//p[@class='sort2']/text()").extract()
    #         details = str(details_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '').replace("[", "").replace("]", "")
    #         items['details'] = details
    #         items['basic']="暂无"
    #         items['diagnosis'] = "暂无"
    #         items['Hospital_must_read'] = "暂无"
    #         yield items
    #         # items["bingfajibing"] = "暂无"
    #         # items["xiangguanzhengzhuang"] = "暂无"
    #         # # yield items
    #
    def parse_two(self,response):

    #     #进入详情页的后续操作
    #     print("**"*20)
        items = response.meta["items"]

        details_list = response.xpath("//div[@class='chi-know']")
        xiangguanzhengzhuang = details_list.xpath("./dl[2]/dd/i[text()='相关症状：']/../a[@class='more']/@href")  # 选择病症相关的url

        yield Request(xiangguanzhengzhuang, callback=self.parse_xiangguan, meta={"items": deepcopy(items)})

    def parse_xiangguan(self,response):
        items = response.meta["items"]
        info_raw = response.xpath("//dl[@class='links']//text()").extract()
        items["info"] = str(info_raw)
        info2 = response.xpath("//div[@class='art-box']//text()").extract()
        items["info2"] = str(info2)
        print(items)








    #     details_list = response.xpath("//div[@class='chi-know']")
    #     #病症详情没问题
    #     details_raw = details_list.xpath("./dl[1]/dd/text()").extract()
    #     details = str(details_raw).replace('\\t', '').replace('\\r', '').replace('\\n','').replace("'","").replace(" ","").replace("\\u3000","").replace("[详细]","").replace("[", "").replace("]", "")
    #     items['details'] = details#病症详情
    #     #基础知识
    #     basic_raw = details_list.xpath("./dl[2]/dd//text()").extract()
    #     basic = str(basic_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '').replace("'", "").replace(" ","").replace("[详细]","").replace("[", "").replace("]", "")
    #     items['basic'] = basic
    #
    #     #诊断：diagnosis
    #     #诊疗知识没问题
    #     diagnosis_raw = details_list.xpath("./dl[3]/dd//text()").extract()
    #     diagnosis = str(diagnosis_raw).replace('\\t', '').replace('\\r', '').replace('\\n','').replace("'","").replace(" ","").replace("[详细]","").replace("[", "").replace("]", "")
    #     items['diagnosis'] = diagnosis #诊疗知识
    #
    #     # 就医必读没问题
    #     hospital_must_read_raw = details_list.xpath("./dl[4]/dd//text()").extract()
    #     hospital_must_read = str(hospital_must_read_raw).replace('\\t', '').replace('\\r', '').replace('\\n','').replace("'","").replace(" ","").replace("[详细]","").replace(",,了解更多就诊知识>>","").replace("[", "").replace("]", "")
    #     items['Hospital_must_read'] = hospital_must_read #就医必读
    #     yield items



        # yield Request(xiangguanzheng_url, callback=self.parse_xiangguanzheng, meta={"items": deepcopy(items)})
        # yield Request(bingfazheng_url, callback=self.parse_bingfazheng, meta={"items": deepcopy(items)})

        # try:#如果有并发疾病
        #     bingfajibing = details_list.xpath("./dl[2]/dd/i[text()='并发疾病：']")#选择并发疾病的url
        #     print("****"*5)
        #     try: #如果有并发疾病的详情
        #         bingfajibing_details_url = bingfajibing.xpath("./following-sibling::a[@class='more']/@href").extract()[0] #获得并发疾病的详情
        #         print("((("*5,bingfajibing_details_url)
        #         yield Request(bingfajibing_details_url, callback=self.parse_bingfajibing, meta={"items": deepcopy(items)}, dont_filter=True)
        #
        #     except: #如果没有并发疾病详情，则。。。
        #         bingfa_raw =  bingfajibing.xpath("../text()").extract()
        #         bingfa = str(bingfa_raw).replace('\\r', '').replace('\\n','').replace("'","").replace(" ","")
        #         items["complication"]  = bingfa
        #         items["complication_details"] = "暂无"
        #         print(items)
        #
        # except: #如果没有并发疾病 则。。。。。
        #     items["complication"] = "暂无"
        #     items["complication_details"] = "暂无"
        #     print(items)


    #
    #
    #     # 处理相关症状的
    #     try:#如果有相关病症
    # Associated_symptoms
    #         xiangguanzhengzhuang = details_list.xpath("./dl[2]/dd/i[text()='相关症状:']")#选择病症相关的url
    #         try: #如果有相关病症的详情
    #             xiangguanzhengzhuang_details_url = xiangguanzhengzhuang.xpath("./following-sibling::a[@class='more']/@href").extract()[0] #获得相关病症的详情
    #             yield Request(xiangguanzhengzhuang_details_url, callback=self.parse_xiangguanzheng, meta={"items": deepcopy(items)})
    #         except: #如果没有病症详情，则。。。
    #             xiangguan_raw = xiangguanzhengzhuang.xpath("./a/text()").extract()
    #             xiangguan = str(xiangguan_raw).replace('\\r', '').replace('\\n', '').replace("'", "").replace(" ", "").replace("[详细]","")
    #             items[""] = xiangguan
    #             items["complication_details"] = "暂无"
    #             yield Request(items["bingfajibing_details_url"], callback=self.parse_bingfajibing,meta={"items": deepcopy(items)})

    #
        # except: #如果没有相关病症 则。。。。。
        #     items["complication"]= "暂无"
        #     items["complication_details"]= "暂无"
        #
        # print(items)
    #         yield Request(items["bingfajibing_details_url"], callback=self.parse_bingfajibing,meta={"items": deepcopy(items)})
    #
    #
    #
    #
    #     # 处理并发疾病的

    # def parse_bingfajibing(self,response):
    #     #提取相关症状
    #     #并发症：complication
    #     print("%%%%%%%%%")
    #     items = response.meta["items"]
    #     complication_raw= response.xpath("//div[@class='chi-know chi-int']/dl[2]//text()").extract() #症状
    #     complication = str(complication_raw).replace('\\r', '').replace('\\n', '').replace("'", "").replace(" ", "")
    #     items["complication"] = complication
    #     complication_details_raw = response.xpath("//div[@class='art-box']//text()").extract()
    #     complication_details = str(complication_details_raw).replace('\\r', '').replace('\\n', '').replace("'", "").replace(" ", "")
    #     items["complication_details"] = complication_details
    #     print("%%%%%%%%%")
    # #     return items
    # #     yield items
    #     print(items)

    #
    #     # yield Request(items["bingfazheng_url"], callback=self.parse_bingfazheng, meta={"items": deepcopy(items)})
    # def parse_xiangguanzheng(self,response):
    #     items = response.meta["items"]
    #     #相关症状：Associated symptoms
    #     Associated_symptoms_raw = response.xpath("//div[@class='chi-know chi-int']/dl[2]/text()").extract()
    #     Associated_symptoms = str(Associated_symptoms_raw).replace('\\r', '').replace('\\n', '').replace("'", "").replace(" ", "")
    #     items["Associated_symptoms"] =Associated_symptoms
    #
    #     Associated_symptoms_details_raw = response.xpath("//div[@class='art-box']/text()").extract()
    #     Associated_symptoms_details = str(Associated_symptoms_details_raw).replace('\\r', '').replace('\\n', '').replace("'", "").replace(" ", "")
    #     items["Associated_symptoms_details"] =Associated_symptoms_details
    #     yield Request(items["bingfajibing_details_url"], callback=self.parse_bingfajibing,
    #                   meta={"items": deepcopy(items)})






# items["xiangguanzheng_url"] = details_list.xpath("./dl[2]/dd[6]/a[@class='more']/@href").extract() #相关症的url
        # xiangguanzheng_url = details_list.xpath("./dl[2]/dd[6]//a[@class='more']/@href").extract()[0]
        # print(xiangguanzheng_url)

        # items["bingfazheng_url"] = details_list.xpath("./dl[2]/dd[7]/a[@class='more']/@href").extract_first() #并发症的url
        # bingfazheng_url = details_list.xpath("./dl[2]/dd[7]/a[@class='more']/@href").extract()[0]
