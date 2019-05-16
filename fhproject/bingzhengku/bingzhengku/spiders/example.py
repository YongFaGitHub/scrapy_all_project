# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from copy import deepcopy
import csv


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.fh21.com.cn/']
    start_urls = ['http://dise.fh21.com.cn/department/illness/1.html']


    def start_requests(self):
        item = {}
        list1 = []
        file = open("H:/pycharmproject/project/39jk/bingzhengku/bingzhengku/spiders/url.csv","rt",encoding="utf-8")
        item["a"] = 0
        item["b"] = 0
        item["c"] = 0
        item["d"] = 0
        item["e"] = 0
        item["f"] = 0
        read = csv.reader(file)
        for line in read:
            if line[0] in list1:
                print("重复")
            else:
                list1.append(line[0])


        list2 = set(list1)
        print(len(list2),"##########################################")
        for i in list2:
            item["url"] = i
            yield Request(i,callback=self.parse,meta={"item":deepcopy(item)})


    def parse(self,response):
        item = response.meta["item"]
        title = response.xpath("//ol[@class='dise01']/p/text()").extract_first()
        item["title"] = title
        img_url = response.xpath("//dl[@class='dise02']/dt/a/img/@src").extract_first()
        item["img_url"] = img_url
        yield Request(img_url,callback=self.parse_img, meta={"item": deepcopy(item)}, dont_filter=True)

    def parse_img(self,response):
        item = response.meta["item"]
        with open("I:/疾病图片/fh/{}.jpg".format(item["title"]),"wb") as f:
            f.write(response.body)

        with open("H:/pycharmproject/project/fhproject/bingzhengku/bingzhengku/spiders/img_url.txt","a+",encoding="utf-8") as f:
            f.write(item["title"])
            f.write("、")
            f.write(item["img_url"])
            f.write("\n")

        print(item["title"])





        # if item["f"] == 0:
        #     item["f"] = 1
        #     yield Request(item["url"], callback=self.parse_tt, meta={"item": deepcopy(item)}, dont_filter=True)
        #
        #
        # if item["a"] == 0:
        #     item["a"] = 1
        #     disease_raw = response.xpath("//dd[@class='dise02b']/p[1]/a[text()='[详细]']/@href").extract_first()
        #     disease_url = "http://dise.fh21.com.cn" + disease_raw
        #     yield Request(disease_url,callback=self.disease,meta={"item":deepcopy(item)},dont_filter=True)
        #
        # if item["b"] == 0:
        #     item["b"] = 1
        #     bingyin_raw = response.xpath("//dd[@class='dise02b']/p[2]/a[text()='[详细]']/@href").extract_first()
        #     bingyin_url = "http://dise.fh21.com.cn" + bingyin_raw
        #     yield Request(bingyin_url,callback=self.bingyin,meta={"item":deepcopy(item)},dont_filter=True)
        #
        # if item["c"] == 0:
        #     item["c"] = 1
        #     jiancha_raw = response.xpath("//dd[@class='dise02b']/p[4]/a[text()='[详细]']/@href").extract_first()
        #     jiancha_url = "http://dise.fh21.com.cn" + jiancha_raw
        #     yield Request(jiancha_url,callback=self.jiancha,meta={"item":deepcopy(item)},dont_filter=True)
        #
        # if item["d"] == 0:
        #     item["d"] = 1
        #     zhiliao_raw = response.xpath("//dd[@class='dise02b']/p[5]/a[text()='[详细]']/@href").extract_first()
        #     zhiliao_url = "http://dise.fh21.com.cn" + zhiliao_raw
        #     yield Request(zhiliao_url,callback=self.zhiliao,meta={"item":deepcopy(item)},dont_filter=True)
        #
        # if item["e"] == 0:
        #     item["e"] = 1
        #     yufang_raw = response.xpath("//dd[@class='dise02b']/p[7]/a[text()='[详细]']/@href").extract_first()
        #     yufang_url = "http://dise.fh21.com.cn" + yufang_raw
        #     yield Request(yufang_url,callback=self.yufang,meta={"item":deepcopy(item)},dont_filter=True)
        #
        # yield Request(item["url"],callback=self.parse_f,meta={"item":deepcopy(item)},dont_filter=True)


    def parse_tt(self,response):

        item = response.meta["item"]
        try:
            title = response.xpath("//ol[@class='dise01']/p/text()").extract_first()
            item["title"] = title

        except:
            item["title"] = "暂无"

        try:
            keshi_raw = response.xpath("//div[@class='dise03']/dl[2]/dd/text()").extract()
            keshi = str(keshi_raw).replace("[", "").replace("]", "").replace("'", "")
            item["keshi"] = keshi

        except:
            item["keshi"] = "暂无"
        try:
            zhengzhuang_raw = response.xpath("//div[@class='dise03']/dl[3]/dd/text()").extract()
            zhengzhaung = str(zhengzhuang_raw).replace("[", "").replace("]", "").replace("'", "")
            item["zhengzhuang"] = zhengzhaung
        except:
            item["zhengzhuang"] = "暂无"

        try:

            jiancha_raw = response.xpath("//div[@class='dise03']/dl[4]/dd/text()").extract()
            jiancha = str(jiancha_raw).replace("[", "").replace("]", "").replace("'", "")
            item["jiancha"] = jiancha

        except:
            item["jiancha"] = "暂无"

        yield Request(item["url"], callback=self.parse, meta={"item": deepcopy(item)},dont_filter=True)


    def disease(self,response):
        item = response.meta["item"]
        try:
            disease_raw = response.xpath("//ul[@class='detailc']//text()").extract()
            disease = str(disease_raw).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
            "").replace(" ", "").replace("\\n","").replace("\n","").replace("','\\u3000\\u3000", "\n").replace("','",
            "").replace('\\xa0',"").replace("\\u3000", "").replace("\\t","")
            if disease[0] == "\n":
                item["disease"] = disease[1:-1]
            else:
                item["disease"] = disease

        except:
            item["disease"] = "暂无"

        yield Request(item["url"],callback=self.parse,meta={"item":deepcopy(item)},dont_filter=True)

    def bingyin(self, response):
        item = response.meta["item"]
        p_list = response.xpath("//ul[@class='detailc']//text()").extract()
        info_disease = str(p_list).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
        "").replace(" ", "").replace("\\n","").replace("\n","").replace("','\\u3000\\u3000", "\n").replace("','",
        "").replace('\\xa0',"").replace("\\u3000", "").replace("\\t","")
        if info_disease[0] == "\n":
            item["bingyin"] = info_disease[1:-1]
        else:
            item["bingyin"] = info_disease


        yield Request(item["url"], callback=self.parse, meta={"item": deepcopy(item)},dont_filter=True)

    def jiancha(self, response):
        item = response.meta["item"]
        try:
            p_list = response.xpath("//ul[@class='detailc']//text()").extract()
            info_disease = str(p_list).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
            "").replace(" ","").replace("\\n", "").replace("\n", "").replace("','\\u3000\\u3000",
            "\n").replace("','", "").replace('\\xa0',"").replace("\\u3000", "").replace("\\t", "")

            if info_disease[0] == "\n":
                item["jiancha_disease"] = info_disease[1:-1]
            else:
                item["jiancha_disease"] = info_disease
        # print(item)
        except:
            item["jiancha_disease"] = "暂无"

        # print(item)
        yield Request(item["url"], callback=self.parse, meta={"item": deepcopy(item)},dont_filter=True)

    def zhiliao(self, response):
        item = response.meta["item"]
        try:
            p_list = response.xpath("//ul[@class='detailc']//text()").extract()
            info_disease = str(p_list).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
            "").replace(" ","").replace("\\n", "").replace("\n", "").replace("','\\u3000\\u3000",
             "\n").replace("','", "").replace('\\xa0', "").replace("\\u3000","").replace("\\t", "")

            if info_disease[0] == "\n":
                item["zhiliao"] = info_disease[1:-1]
            else:
                item["zhiliao"] = info_disease
        except:
            item["zhiliao"] = "暂无"


        yield Request(item["url"], callback=self.parse, meta={"item": deepcopy(item)},dont_filter=True)

    def yufang(self, response):
        item = response.meta["item"]
        try:
            p_list = response.xpath("//ul[@class='detailc']//text()").extract()
            info_disease = str(p_list).replace("['", "").replace("']", "").replace("\\r", "").replace("\\n",
            "").replace(" ","").replace("\\n", "").replace("\n", "").replace("','\\u3000\\u3000",
            "\n").replace("','", "").replace('\\xa0', "").replace("\\u3000","").replace("\\t", "")

            if info_disease[0] == "\n":
                item["yufang"] = info_disease[1:-1]
            else:
                item["yufang"] = info_disease
        except:
            item["yufang"] = "暂无"

        yield Request(item["url"], callback=self.parse, meta={"item": deepcopy(item)},dont_filter=True)

    def parse_f(self,response):
        item = response.meta["item"]
        if len(list(item.keys())) == 16:
            # print(item)
            yield item
    #     # response.xpath("//div[@class='block_tag block_tag02']/li/a[text()='']")


        # disease_raw = response.xpath("//div[@class='dise02b']/p[1]/a[ytext()='[详细]']/@href").extract_first()
        # bingyin_raw = response.xpath("//div[@class='dise02b']/p[2]/a[ytext()='[详细]']/@href").extract_first()
        # jiancha_raw = response.xpath("//div[@class='dise02b']/p[4]/a[ytext()='[详细]']/@href").extract_first()
        # zhiliao_raw = response.xpath("//div[@class='dise02b']/p[5]/a[ytext()='[详细]']/@href").extract_first()
        # yufang_raw = response.xpath("//div[@class='dise02b']/p[7]/a[ytext()='[详细]']/@href").extract_first()





    # def parse(self, response):
    #     item = {}
    #     dl_list = response.xpath("//div[@class='menu_con']/dl/dt")
    #     for dl in dl_list:
    #         url_raw = dl.xpath("./a[1]/@href").extract_first()
    #         item["big"] = dl.xpath("./a[1]/text()").extract_first()
    #         url = "http://dise.fh21.com.cn" + url_raw
    #         yield Request(url,callback=self.parse_one,meta={"item":deepcopy(item)},dont_filter=True)
    #
    #
    # def parse_one(self,response):
    #     # print("@@@@@@@2")
    #     item = response.meta["item"]
    #     ul_list = response.xpath("//div[@class='dise_list']/ul/li")
    #
    #     for li in ul_list:
    #         url = li.xpath("./a/@href").extract_first()
    #         title = li.xpath("./a/text()").extract_first()
    #         item["title"] = title
    #         item["a"] = 0
    #         item["b"] = 0
    #         item["c"] = 0
    #         item["d"] = 0
    #         item["e"] = 0
    #         item["f"] = 0
    #         item["url"] = url
            # if url is not None:
            #     with open("H:/pycharmproject/project/39jk/bingzhengku/bingzhengku/spiders/url.csv","a+",encoding="utf-8") as f:
            #         f.write(url)
            #
            #
            #         f.write("\n")
            # yield Request(url,callback=self.parse_t,meta={"item":deepcopy(item)},dont_filter=True)
