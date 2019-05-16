# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.fh21.com.cn/']
    start_urls = []

    def start_requests(self):

        list = ['http://iask.fh21.com.cn/question/list-392.html', 'http://iask.fh21.com.cn/question/list-231.html',
                'http://iask.fh21.com.cn/question/list-344.html',
                'http://iask.fh21.com.cn/question/list-352.html', 'http://iask.fh21.com.cn/question/list-285.html',
                'http://iask.fh21.com.cn/question/list-10.html',
                'http://iask.fh21.com.cn/question/list-22.html', 'http://iask.fh21.com.cn/question/list-625.html',
                'http://iask.fh21.com.cn/question/list-468.html',
                'http://iask.fh21.com.cn/question/list-375.html', 'http://iask.fh21.com.cn/question/list-5.html',
                'http://iask.fh21.com.cn/question/list-346.html',
                'http://iask.fh21.com.cn/question/list-133.html', 'http://iask.fh21.com.cn/question/list-147.html',
                'http://iask.fh21.com.cn/question/list-549.html',
                'http://iask.fh21.com.cn/question/list-40.html', 'http://iask.fh21.com.cn/question/list-143.html',
                'http://iask.fh21.com.cn/question/list-299.html',
                'http://iask.fh21.com.cn/question/list-281.html', 'http://iask.fh21.com.cn/question/list-430.html',
                'http://iask.fh21.com.cn/question/list-175.html',
                'http://iask.fh21.com.cn/question/list-202.html', 'http://iask.fh21.com.cn/question/list-308.html',
                'http://iask.fh21.com.cn/question/list-165.html',
                'http://iask.fh21.com.cn/question/list-167.html', 'http://iask.fh21.com.cn/question/list-336.html',
                'http://iask.fh21.com.cn/question/list-81.html',
                'http://iask.fh21.com.cn/question/list-36.html', 'http://iask.fh21.com.cn/question/list-108.html',
                'http://iask.fh21.com.cn/question/list-302.html',
                'http://iask.fh21.com.cn/question/list-229.html', 'http://iask.fh21.com.cn/question/list-402.html',
                'http://iask.fh21.com.cn/question/list-563.html',
                'http://iask.fh21.com.cn/question/list-445.html', 'http://iask.fh21.com.cn/question/list-588.html',
                'http://iask.fh21.com.cn/question/list-350.html',
                'http://iask.fh21.com.cn/question/list-136.html', 'http://iask.fh21.com.cn/question/list-152.html',
                'http://iask.fh21.com.cn/question/list-502.html',
                'http://iask.fh21.com.cn/question/list-31.html', 'http://iask.fh21.com.cn/question/list-64.html',
                'http://iask.fh21.com.cn/question/list-340.html',
                'http://iask.fh21.com.cn/question/list-412.html', 'http://iask.fh21.com.cn/question/list-421.html',
                'http://iask.fh21.com.cn/question/list-67.html',
                'http://iask.fh21.com.cn/question/list-28.html', 'http://iask.fh21.com.cn/question/list-145.html',
                'http://iask.fh21.com.cn/question/list-335.html',
                'http://iask.fh21.com.cn/question/list-624.html', 'http://iask.fh21.com.cn/question/list-212.html',
                'http://iask.fh21.com.cn/question/list-59.html',
                'http://iask.fh21.com.cn/question/list-325.html', 'http://iask.fh21.com.cn/question/list-284.html',
                'http://iask.fh21.com.cn/question/list-234.html',
                'http://iask.fh21.com.cn/question/list-171.html', 'http://iask.fh21.com.cn/question/list-230.html',
                'http://iask.fh21.com.cn/question/list-462.html',
                'http://iask.fh21.com.cn/question/list-309.html', 'http://iask.fh21.com.cn/question/list-121.html',
                'http://iask.fh21.com.cn/question/list-547.html',
                'http://iask.fh21.com.cn/question/list-235.html', 'http://iask.fh21.com.cn/question/list-174.html',
                'http://iask.fh21.com.cn/question/list-29.html',
                'http://iask.fh21.com.cn/question/list-153.html', 'http://iask.fh21.com.cn/question/list-9.html',
                'http://iask.fh21.com.cn/question/list-283.html',
                'http://iask.fh21.com.cn/question/list-450.html', 'http://iask.fh21.com.cn/question/list-164.html',
                'http://iask.fh21.com.cn/question/list-46.html',
                'http://iask.fh21.com.cn/question/list-163.html', 'http://iask.fh21.com.cn/question/list-422.html',
                'http://iask.fh21.com.cn/question/list-127.html',
                'http://iask.fh21.com.cn/question/list-113.html', 'http://iask.fh21.com.cn/question/list-496.html',
                'http://iask.fh21.com.cn/question/list-248.html',
                'http://iask.fh21.com.cn/question/list-60.html', 'http://iask.fh21.com.cn/question/list-50.html',
                'http://iask.fh21.com.cn/question/list-69.html',
                'http://iask.fh21.com.cn/question/list-479.html', 'http://iask.fh21.com.cn/question/list-120.html',
                'http://iask.fh21.com.cn/question/list-177.html',
                'http://iask.fh21.com.cn/question/list-550.html', 'http://iask.fh21.com.cn/question/list-66.html',
                'http://iask.fh21.com.cn/question/list-331.html',
                'http://iask.fh21.com.cn/question/list-274.html', 'http://iask.fh21.com.cn/question/list-119.html',
                'http://iask.fh21.com.cn/question/list-25.html',
                'http://iask.fh21.com.cn/question/list-148.html', 'http://iask.fh21.com.cn/question/list-383.html',
                'http://iask.fh21.com.cn/question/list-312.html',
                'http://iask.fh21.com.cn/question/list-434.html', 'http://iask.fh21.com.cn/question/list-307.html',
                'http://iask.fh21.com.cn/question/list-187.html',
                'http://iask.fh21.com.cn/question/list-16.html', 'http://iask.fh21.com.cn/question/list-543.html',
                'http://iask.fh21.com.cn/question/list-49.html',
                'http://iask.fh21.com.cn/question/list-84.html', 'http://iask.fh21.com.cn/question/list-216.html',
                'http://iask.fh21.com.cn/question/list-63.html',
                'http://iask.fh21.com.cn/question/list-466.html', 'http://iask.fh21.com.cn/question/list-561.html',
                'http://iask.fh21.com.cn/question/list-95.html',
                'http://iask.fh21.com.cn/question/list-313.html', 'http://iask.fh21.com.cn/question/list-272.html',
                'http://iask.fh21.com.cn/question/list-90.html',
                'http://iask.fh21.com.cn/question/list-385.html', 'http://iask.fh21.com.cn/question/list-362.html',
                'http://iask.fh21.com.cn/question/list-501.html',
                'http://iask.fh21.com.cn/question/list-341.html', 'http://iask.fh21.com.cn/question/list-215.html',
                'http://iask.fh21.com.cn/question/list-189.html',
                'http://iask.fh21.com.cn/question/list-568.html', 'http://iask.fh21.com.cn/question/list-388.html',
                'http://iask.fh21.com.cn/question/list-44.html',
                'http://iask.fh21.com.cn/question/list-524.html', 'http://iask.fh21.com.cn/question/list-88.html',
                'http://iask.fh21.com.cn/question/list-52.html',
                'http://iask.fh21.com.cn/question/list-519.html', 'http://iask.fh21.com.cn/question/list-86.html',
                'http://iask.fh21.com.cn/question/list-589.html',
                'http://iask.fh21.com.cn/question/list-76.html', 'http://iask.fh21.com.cn/question/list-82.html',
                'http://iask.fh21.com.cn/question/list-134.html',
                'http://iask.fh21.com.cn/question/list-371.html', 'http://iask.fh21.com.cn/question/list-252.html',
                'http://iask.fh21.com.cn/question/list-389.html',
                'http://iask.fh21.com.cn/question/list-401.html', 'http://iask.fh21.com.cn/question/list-469.html',
                'http://iask.fh21.com.cn/question/list-345.html',
                'http://iask.fh21.com.cn/question/list-404.html', 'http://iask.fh21.com.cn/question/list-246.html',
                'http://iask.fh21.com.cn/question/list-116.html',
                'http://iask.fh21.com.cn/question/list-33.html', 'http://iask.fh21.com.cn/question/list-382.html',
                'http://iask.fh21.com.cn/question/list-329.html',
                'http://iask.fh21.com.cn/question/list-213.html', 'http://iask.fh21.com.cn/question/list-61.html',
                'http://iask.fh21.com.cn/question/list-158.html',
                'http://iask.fh21.com.cn/question/list-57.html', 'http://iask.fh21.com.cn/question/list-437.html',
                'http://iask.fh21.com.cn/question/list-429.html',
                'http://iask.fh21.com.cn/question/list-65.html', 'http://iask.fh21.com.cn/question/list-144.html',
                'http://iask.fh21.com.cn/question/list-110.html',
                'http://iask.fh21.com.cn/question/list-251.html', 'http://iask.fh21.com.cn/question/list-579.html',
                'http://iask.fh21.com.cn/question/list-101.html',
                'http://iask.fh21.com.cn/question/list-567.html', 'http://iask.fh21.com.cn/question/list-306.html',
                'http://iask.fh21.com.cn/question/list-89.html',
                'http://iask.fh21.com.cn/question/list-342.html', 'http://iask.fh21.com.cn/question/list-115.html',
                'http://iask.fh21.com.cn/question/list-238.html',
                'http://iask.fh21.com.cn/question/list-544.html', 'http://iask.fh21.com.cn/question/list-333.html',
                'http://iask.fh21.com.cn/question/list-576.html',
                'http://iask.fh21.com.cn/question/list-146.html', 'http://iask.fh21.com.cn/question/list-244.html',
                'http://iask.fh21.com.cn/question/list-135.html',
                'http://iask.fh21.com.cn/question/list-530.html', 'http://iask.fh21.com.cn/question/list-141.html',
                'http://iask.fh21.com.cn/question/list-151.html',
                'http://iask.fh21.com.cn/question/list-470.html', 'http://iask.fh21.com.cn/question/list-250.html',
                'http://iask.fh21.com.cn/question/list-387.html',
                'http://iask.fh21.com.cn/question/list-100.html', 'http://iask.fh21.com.cn/question/list-374.html',
                'http://iask.fh21.com.cn/question/list-150.html',
                'http://iask.fh21.com.cn/question/list-96.html', 'http://iask.fh21.com.cn/question/list-23.html',
                'http://iask.fh21.com.cn/question/list-348.html',
                'http://iask.fh21.com.cn/question/list-154.html', 'http://iask.fh21.com.cn/question/list-160.html',
                'http://iask.fh21.com.cn/question/list-123.html',
                'http://iask.fh21.com.cn/question/list-376.html', 'http://iask.fh21.com.cn/question/list-83.html',
                ]

        for url in list:
            yield Request(url, callback=self.parse_one)

    def parse_one(self,response):
        item = {}
        # print("@@@@@")
        ul_list = response.xpath("//div[@class='iask10_con']/ul")
        for ul in ul_list:
            title_raw = ul.xpath("./li[1]/span/a/text()").extract_first()
            title = str(title_raw)
            item["title"] = title
            question_title_raw = ul.xpath("./li[1]/a/text()").extract_first()
            question_title = str(question_title_raw )
            item["question_title"] = question_title

            url_raw = ul.xpath("./li[1]/a/@href").extract_first()
            url = 'http://iask.fh21.com.cn' +url_raw
            yield Request(url, callback=self.parse_three, meta={"item": deepcopy(item)}, dont_filter=True)

        next_url_raw = response.xpath("//div[@class='pageStyle']//a[text()='下一页']/@href").extract_first()
        next_url = 'http://iask.fh21.com.cn' + next_url_raw
        yield Request(next_url, callback=self.parse_one, meta={"item": deepcopy(item)}, dont_filter=True)

    def parse_three(self, response):
            list = []
            item = response.meta["item"]

            #个人信息
            info_raw = response.xpath("//div[@class='iask_detail01b1']/dl[1]/dd/text()").extract()
            info = str(info_raw)
            item["info"] = info

            #问题
            question_raw = response.xpath("//div[@class='iask_detail01b1']/dl[2]/dd//text()").extract()
            question = str(question_raw)
            item["question"] = question

            #回答
            div_list = response.xpath("//div[@class='iask_detail03']/div")
            for div in div_list:
                answer_raw = div.xpath(".//div[@class='iask_answer02a']/dl/dd//text()").extract()
                list.append(answer_raw)

            item["answer"] = str(list)
            yield item
            # print(item)














    #     dl_list = response.xpath("//div[@class='iask02']/dl[1]/following-sibling::*")
    #     for dl in dl_list:
    #         p_list = dl.xpath("./dd/p")
    #         for p in p_list:
    #             #大类的标签
    #             title_raw = p.xpath("./a/text()").extract_first()
    #             title = str(title_raw)
    #             item["title"] = title
    #             #进入小分类的地址
    #             url_raw = p.xpath("./a/@href").extract_first()
    #             url = "http:" + url_raw  #没问题
    #             yield Request(url, callback=self.parse_one, meta={"item": deepcopy(item)},dont_filter=True)
    #
    #
    # def parse_one(self,response):
    #     item = response.meta["item"]
    #     a_list = response.xpath("//ul[@class='w645 left']/div[1]/div[2]/a")
    #     print(a_list)
    #     for a in a_list:
    #         #中级标签
    #         small_title_raw = a.xpath("./text()").extract_first()
    #         small_title = str(small_title_raw)
    #         item["small_title"] = small_title
    #
    #
    #         url_raw = a.xpath("./@href").extract_first()
    #         url = "http://iask.fh21.com.cn" + url_raw
    #         # print(small_title)
    #         # yield Request(url,callback=self.parse_two, meta={"item": deepcopy(item)}, dont_filter=True)
    #
    #         # https: // iask.fh21.com.cn
    #
    # def parse_two(self,response):
    #     item = response.meta["item"]
    #     ul_list = response.xpath("//div[@class='iask10_con']/ul")
    #     for ul in ul_list:
    #         #文问题头部
    #         question_title_raw = ul.xpath("./li[1]/a/text()").extract_first()
    #         question_title = str(question_title_raw)
    #         item["question_title"] = question_title
    #
    #         url_raw = ul.xpath("./li[1]/a/@href").extract_first()
    #         url = "http://iask.fh21.com.cn/" + url_raw
    #         yield Request(url, callback=self.parse_three, meta={"item": deepcopy(item)}, dont_filter=True)
    #
    # def parse_three(self,response):
    #     list = []
    #     item = response.meta["item"]
    #
    #     #个人信息
    #     info_raw = response.xpath("//div[@class='iask_detail01b1']/dl[1]/dd/text()").extract()
    #     info = str(info_raw)
    #     item["info"] = info
    #
    #     #问题
    #     question_raw = response.xpath("//div[@class='iask_detail01b1']/dl[2]/dd//text()").extract()
    #     question = str(question_raw)
    #     item["question"] = question
    #
    #     #回答
    #     div_list = response.xpath("//div[@class='iask_detail03']/div")
    #     for div in div_list:
    #         answer_raw = div.xpath(".//div[@class='iask_answer02a']/dl/dd//text()").extract()
    #         list.append(answer_raw)
    #
    #     item["answer"] = str(list)
    #     yield item
    #     # print(item)


