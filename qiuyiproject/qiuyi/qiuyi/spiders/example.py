# -*- coding: utf-8 -*-


import scrapy
from scrapy.http import Request
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.qiuyi.cn']
    start_urls = []

    def start_requests(self):
        # http: // ask.qiuyi.cn / questionlist / 2.html
        for i in range(21000,31000 ): #52853
            url = 'http://ask.qiuyi.cn/questionlist/' + str(i) + '.html'
            # print()

            yield Request(url, callback=self.parse_one, dont_filter=True)

    def parse_one(self, response):
        item = {}
        urls = response.xpath("//ul[@class='active']/li/span[1]/a[@target='_blank']/@href").extract()
        n = len(urls)
        # print(n)
        for i in range(0, n):
            all_urls = urls[i]
            # print(all_urls)

            yield Request(all_urls, callback=self.parse_two, dont_filter=True)

    def parse_two(self, response):
        items = {}
        big_class_raw = response.xpath("//p[@class='position']/a[3]/text()").extract_first()
        big_class = str(big_class_raw)
        items["big_class"] = big_class

        # 小分类
        small_class_raw = response.xpath("//p[@class='position']/a[4]/text()").extract_first()
        small_class = str(small_class_raw)
        items["small_class"] = small_class

        # 病症的名称
        title_raw = response.xpath("//p[@class='position']/a[5]/text()").extract_first()
        title = str(title_raw)
        items["title"] = title

        # 问题的 头部
        ask_title_raw = response.xpath("//div[@class='ask_title']/h1/text()").extract_first()
        ask_title = str(ask_title_raw).replace("\n", "")
        items["ask_title"] = ask_title

        # 病症描述
        disease_Description_raw = response.xpath("//div[@class='wd_cont_s']/p[1]/text()").extract_first()
        disease_Description = str(disease_Description_raw).replace("\n", "")
        items["disease_Description"] = disease_Description

            #以往状况
        before_raw = response.xpath("//div[@class='wd_cont_s']/p[2]/text()").extract_first()
        before = str(before_raw).replace("\n", "")
        items["before"] = before


        #想要得到什么帮助
        help_raw = response.xpath("//div[@class='wd_cont_s']/p[2]/text()").extract_first()
        help = str(help_raw).replace("\n", "")
        items["help"] = help

        # 医师回答（包括多条，每条使用[] 分隔）
        list = []
        answer_raw = response.xpath("//div[@class='wd_box_2 bor answer']//div[@class='wd_cont_s']/p[1]")
        for answer_ra in answer_raw:
            list.append("[" + str(answer_ra.xpath("./text()").extract_first().replace("\\n", "") + "]"))
        items["answer"] = str(list)
        # print(items)
        yield items





    # allowed_domains = ['www.qiuyi.cn']
    # start_urls = ['http://ask.qiuyi.cn/']
    #
    # def parse(self, response):
    #     items = {}
    #     ul_list = response.xpath("//div[@class='content_text content']/ul") #所在的ul列表标签
    #
    #
    #     for ul in ul_list:
    #         li_list = ul.xpath("./li")
    #         for li in li_list:
    #             # 944种疾病
    #             url = li.xpath("./a/@href").extract_first()   #获得进入病症问答的列表页面
    #             title_raw = li.xpath("./a/text()").extract_first() #病症的title
    #             title = str(title_raw)
    #             items["title"] = title
    #             yield Request(url, callback=self.parse_one, meta={"items": deepcopy(items)}, dont_filter=True)
    #
    #
    # def parse_one(self,response):
    #     items = response.meta["items"]
    #     li_list = response.xpath("//ul[@class='active']/li")
    #     for li in li_list:
    #         url  = li.xpath("./span[1]/a[2]/@href").extract_first()
    #         yield Request(url, callback=self.parse_two, meta={"items": deepcopy(items)}, dont_filter=True)
    #
    #
    #     #下一页的请求
    #     next_url_temp = response.xpath("//div[@class='page']/a[@class='next']/@href").extract_first()
    #     if next_url_temp is not None:
    #         next_url = next_url_temp
    #         yield scrapy.Request(
    #             next_url,
    #             callback=self.parse_one,  # 列表页的数据解析调用自己
    #             meta={"items": response.meta["items"]}
    #         )
    #
    #
    # def parse_two(self,response):
    #     list = []
    #     items = response.meta["items"]
    #     #大分类
    #     big_class_raw = response.xpath("//p[@class='position']/a[3]/text()").extract_first()
    #     big_class = str(big_class_raw)
    #     items["big_class"] = big_class
    #
    #     #小分类
    #     small_class_raw = response.xpath("//p[@class='position']/a[4]/text()").extract_first()
    #     small_class = str(small_class_raw)
    #     items["small_class"] = small_class
    #
    #     # 问题的 头部
    #     ask_title_raw = response.xpath("//div[@class='ask_title']/h1/text()").extract_first()
    #     ask_title  = str(ask_title_raw).replace("\n","")
    #     items["ask_title"] = ask_title
    #
    #     # 病症描述
    #     disease_Description_raw = response.xpath("//div[@class='wd_cont_s']/p[1]/text()").extract_first()
    #     disease_Description = str(disease_Description_raw).replace("\n","")
    #     items["disease_Description"] = disease_Description
    #
    #     #以往状况
    #     before_raw = response.xpath("//div[@class='wd_cont_s']/p[2]/text()").extract_first()
    #     before = str(before_raw).replace("\n", "")
    #     items["before"] = before
    #
    #
    #     #想要得到什么帮助
    #     help_raw = response.xpath("//div[@class='wd_cont_s']/p[2]/text()").extract_first()
    #     help = str(help_raw).replace("\n", "")
    #     items["help"] = help
    #     #医师回答（包括多条，每条使用[] 分隔）
    #     answer_raw = response.xpath("//div[@class='wd_box_2 bor answer']//div[@class='wd_cont_s']/p[1]")
    #     for answer_ra in answer_raw:
    #         list.append("[" + str(answer_ra.xpath("./text()").extract_first().replace("\\n","")+"]"))
    #     items["answer"] = str(list)
    #
    #
    #     yield items
