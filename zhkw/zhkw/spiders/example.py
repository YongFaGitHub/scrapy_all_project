# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from copy import deepcopy

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['www.cnkang.com']
    start_urls = ['http://www.cnkang.com/dise/keshi/list_1.html']

    def parse(self, response):
        div_list = response.xpath("//div[@class='w920 right']/div")
        #884种疾病
        item = {}
        for div in div_list:
            div2_list = div.xpath("./div")
            for div2 in div2_list:
                li_list = div2.xpath("./ul/li")
                for li in li_list:
                    title_raw = li.xpath("./a/text()").extract_first()
                    title = str(title_raw)
                    item["title"] = title
                    # print(text)
                    url_raw = li.xpath("./a/@href").extract_first()
                    url = "http://www.cnkang.com" +url_raw
                    # print(url)
                    yield Request(url, callback=self.parse_one, meta={"item": deepcopy(item)})

    def parse_one(self,response):
        item = response.meta["item"]
        zhengzhuang_url_raw = response.xpath("//dl[@class='dise_menu01']/dd/p[3]/a/@href").extract_first()   # 症状地址
        zhengzhuang_url = "http://www.cnkang.com" +str(zhengzhuang_url_raw)

        zhenduan_url_raw = response.xpath("//dl[@class='dise_menu02']/dd/p[1]/a/@href").extract_first()  #诊断地址
        zhenduan_url = "http://www.cnkang.com" + str(zhenduan_url_raw)
        item["zhenduan_url"] = zhenduan_url


        jiancha_url_raw = response.xpath("//dl[@class='dise_menu02']/dd/p[2]/a/@href").extract_first()  # 检查地址
        jiancha_url = "http://www.cnkang.com" + str(jiancha_url_raw)
        item["jiancha_url"] = jiancha_url

        yongyao_url_raw = response.xpath("//dl[@class='dise_menu02']/dd/p[3]/a/@href").extract_first()  # 用药地址
        yongyao_url = "http://www.cnkang.com" + str(yongyao_url_raw)
        item["yongyao_url"] =yongyao_url

        zhiliao_url_raw = response.xpath("//dl[@class='dise_menu02']/dd/p[4]/a/@href").extract_first()  # 治疗地址
        zhiliao_url = "http://www.cnkang.com" + str(zhiliao_url_raw)
        item["zhiliao_url"] = zhiliao_url

        yield Request(zhengzhuang_url, callback=self.parse_zhengzhuang, meta={"item": deepcopy(item)})






    def parse_zhengzhuang(self,response):
        item = response.meta["item"]
        zhengzhuang1_url_raw = response.xpath("//div[@class='w680 left']/dl[1]/dt/a/@href").extract_first() #症状1
        zhengzhuang1_url  = "http://www.cnkang.com" +str(zhengzhuang1_url_raw)
        item["zhengzhuang1_url"] = zhengzhuang1_url


        zhengzhuang2_url_raw = response.xpath("//div[@class='w680 left']/dl[2]/dt/a/@href").extract_first() #症状2
        zhengzhuang2_url = "http://www.cnkang.com" + str(zhengzhuang2_url_raw)
        item["zhengzhuang2_url"] = zhengzhuang2_url

        zhengzhuang3_url_raw = response.xpath("//div[@class='w680 left']/dl[3]/dt/a/@href").extract_first() #症状3
        zhengzhuang3_url = "http://www.cnkang.com" + str(zhengzhuang3_url_raw)
        item["zhengzhuang3_url"] = zhengzhuang3_url
        # print(item)
        yield Request(item["zhengzhuang1_url"], callback=self.parse_zhengzhuang1, meta={"item": deepcopy(item)})


    def parse_zhengzhuang1(self,response):
        item = response.meta["item"]
        zhengzhuang1_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        zhengzhuang1 = str(zhengzhuang1_raw).replace("\\u3000","").replace("[","").replace("]","").replace("'","").replace("。, ","。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")

        item["zhengzhuang1"] = zhengzhuang1
        yield Request(item["zhengzhuang2_url"], callback=self.parse_zhengzhuang2, meta={"item": deepcopy(item)})

    def parse_zhengzhuang2(self,response):
        item = response.meta["item"]
        zhengzhuang2_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        zhengzhuang2 = str(zhengzhuang2_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'","").replace("。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["zhengzhuang2"] = zhengzhuang2
        yield Request(item["zhengzhuang3_url"], callback=self.parse_zhengzhuang3, meta={"item": deepcopy(item)})

    def parse_zhengzhuang3(self,response):
        item = response.meta["item"]
        zhengzhuang3_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        zhengzhuang3 = str(zhengzhuang3_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'", "").replace("。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["zhengzhuang3"] = zhengzhuang3
        # print(item)                                                                                                                               #没问题
        yield Request(item["zhenduan_url"], callback=self.parse_zhenduan, meta={"item": deepcopy(item)})

    def parse_zhenduan(self,response):
        item = response.meta["item"]

        zhenduan1_url_raw = response.xpath("//div[@class='w680 left']/dl[1]/dt/a/@href").extract_first()  # 1
        zhenduan1_url = "http://www.cnkang.com" + str(zhenduan1_url_raw)
        item["zhenduan1_url"] = zhenduan1_url

        zhenduan2_url_raw = response.xpath("//div[@class='w680 left']/dl[2]/dt/a/@href").extract_first()  # 2
        zhenduan2_url = "http://www.cnkang.com" + str(zhenduan2_url_raw)
        item["zhenduan2_url"] = zhenduan2_url

        zhenduan3_url_raw = response.xpath("//div[@class='w680 left']/dl[3]/dt/a/@href").extract_first()  # 3
        zhenduan3_url = "http://www.cnkang.com" + str(zhenduan3_url_raw)
        item["zhenduan3_url"] = zhenduan3_url

        yield Request(item["zhenduan1_url"], callback=self.parse_zhenduan1, meta={"item": deepcopy(item)})

    def parse_zhenduan1(self, response):
        item = response.meta["item"]
        zhenduan1_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        zhenduan1 = str(zhenduan1_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'", "").replace("。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["zhenduan1"] = zhenduan1
        yield Request(item["zhenduan2_url"], callback=self.parse_zhenduan2, meta={"item": deepcopy(item)})

    def parse_zhenduan2(self, response):
        item = response.meta["item"]
        zhenduan2_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        zhenduan2 = str(zhenduan2_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'","").replace("。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["zhenduan2"] = zhenduan2
        yield Request(item["zhenduan3_url"], callback=self.parse_zhenduan3, meta={"item": deepcopy(item)})

    def parse_zhenduan3(self, response):
        item = response.meta["item"]
        zhenduan3_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        zhenduan3 = str(zhenduan3_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'","").replace( "。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["zhenduan3"] = zhenduan3
        # print(item)                                                                                                                        #没问题

        yield Request(item["jiancha_url"], callback=self.parse_jiancha, meta={"item": deepcopy(item)})

    def parse_jiancha(self, response):
        item = response.meta["item"]

        jiancha1_url_raw = response.xpath("//div[@class='w680 left']/dl[1]/dt/a/@href").extract_first()  # 1
        jiancha1_url = "http://www.cnkang.com" + str(jiancha1_url_raw)
        item["jiancha1_url"] = jiancha1_url

        jiancha2_url_raw = response.xpath("//div[@class='w680 left']/dl[2]/dt/a/@href").extract_first()  # 2
        jiancha2_url = "http://www.cnkang.com" + str(jiancha2_url_raw)
        item["jiancha2_url"] = jiancha2_url

        jiancha3_url_raw = response.xpath("//div[@class='w680 left']/dl[3]/dt/a/@href").extract_first()  # 3
        jiancha3_url = "http://www.cnkang.com" + str(jiancha3_url_raw)
        item["jiancha3_url"] = jiancha3_url

        yield Request(item["jiancha1_url"], callback=self.parse_jiancha1, meta={"item": deepcopy(item)})

    def parse_jiancha1(self, response):
        item = response.meta["item"]
        jiancha1_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        jiancha1 = str(jiancha1_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'","").replace("。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["jiancha1"] = jiancha1
        yield Request(item["jiancha2_url"], callback=self.parse_jiancha2, meta={"item": deepcopy(item)})

    def parse_jiancha2(self, response):
        item = response.meta["item"]
        jiancha2_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        jiancha2 = str(jiancha2_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'","").replace("。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["jiancha2"] = jiancha2
        yield Request(item["jiancha3_url"], callback=self.parse_jiancha3, meta={"item": deepcopy(item)})

    def parse_jiancha3(self, response):
        item = response.meta["item"]
        jiancha3_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        jiancha3 = str(jiancha3_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'", "").replace( "。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["jiancha3"] = jiancha3
        # print(item)                                                                                                                       #没问题
        yield Request(item["yongyao_url"], callback=self.parse_yongyao, meta={"item": deepcopy(item)})



    def parse_yongyao(self, response):
        item = response.meta["item"]

        yongyao1_url_raw = response.xpath("//div[@class='w680 left']/dl[1]/dt/a/@href").extract_first()  # 1
        yongyao1_url = "http://www.cnkang.com" + str(yongyao1_url_raw)
        item["yongyao1_url"] = yongyao1_url

        yongyao2_url_raw = response.xpath("//div[@class='w680 left']/dl[2]/dt/a/@href").extract_first()  # 2
        yongyao2_url = "http://www.cnkang.com" + str(yongyao2_url_raw)
        item["yongyao2_url"] = yongyao2_url

        yongyao3_url_raw = response.xpath("//div[@class='w680 left']/dl[3]/dt/a/@href").extract_first()  # 3
        yongyao3_url = "http://www.cnkang.com" + str(yongyao3_url_raw)
        item["yongyao3_url"] = yongyao3_url

        yield Request(item["yongyao1_url"], callback=self.parse_yongyao1, meta={"item": deepcopy(item)})

    def parse_yongyao1(self, response):
        item = response.meta["item"]
        yongyao1_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        yongyao1 = str(yongyao1_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'", "").replace(
            "。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["yongyao1"] = yongyao1
        yield Request(item["yongyao2_url"], callback=self.parse_yongyao2, meta={"item": deepcopy(item)})

    def parse_yongyao2(self, response):
        item = response.meta["item"]
        yongyao2_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        yongyao2 = str(yongyao2_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'", "").replace(
            "。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["yongyao2"] = yongyao2
        yield Request(item["yongyao3_url"], callback=self.parse_yongyao3, meta={"item": deepcopy(item)})

    def parse_yongyao3(self, response):
        item = response.meta["item"]
        yongyao3_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        yongyao3 = str(yongyao3_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'", "").replace(
            "。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["yongyao3"] = yongyao3
        # print(item)                                                                                                                       #没问题
        yield Request(item["zhiliao_url"], callback=self.parse_zhiliao, meta={"item": deepcopy(item)})





    def parse_zhiliao(self, response):
        item = response.meta["item"]

        zhiliao1_url_raw = response.xpath("//div[@class='w680 left']/dl[1]/dt/a/@href").extract_first()  # 1
        zhiliao1_url = "http://www.cnkang.com" + str(zhiliao1_url_raw)
        item["zhiliao1_url"] = zhiliao1_url

        zhiliao2_url_raw = response.xpath("//div[@class='w680 left']/dl[2]/dt/a/@href").extract_first()  # 2
        zhiliao2_url = "http://www.cnkang.com" + str(zhiliao2_url_raw)
        item["zhiliao2_url"] = zhiliao2_url

        zhiliao3_url_raw = response.xpath("//div[@class='w680 left']/dl[3]/dt/a/@href").extract_first()  # 3
        zhiliao3_url = "http://www.cnkang.com" + str(zhiliao3_url_raw)
        item["zhiliao3_url"] = zhiliao3_url

        yield Request(item["zhiliao1_url"], callback=self.parse_zhiliao1, meta={"item": deepcopy(item)})

    def parse_zhiliao1(self, response):
        item = response.meta["item"]
        zhiliao1_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        zhiliao1 = str(zhiliao1_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'","").replace("。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["zhiliao1"] = zhiliao1
        yield Request(item["zhiliao2_url"], callback=self.parse_zhiliao2, meta={"item": deepcopy(item)})

    def parse_zhiliao2(self, response):
        item = response.meta["item"]
        zhiliao2_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        zhiliao2 = str(zhiliao2_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'","").replace("。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["zhiliao2"] = zhiliao2
        yield Request(item["zhiliao3_url"], callback=self.parse_zhiliao3, meta={"item": deepcopy(item)})

    def parse_zhiliao3(self, response):
        item = response.meta["item"]
        zhiliao3_raw = response.xpath("//div[@class='detailc']/p/text()").extract()
        zhiliao3 = str(zhiliao3_raw).replace("\\u3000", "").replace("[", "").replace("]", "").replace("'", "").replace( "。, ", "。").replace("\\xa0","").replace("\\r\\n","").replace("\\r","").replace("\\n","").replace("\r","").replace("\n","").replace(", ,","").replace(" ","")
        item["zhiliao3"] = zhiliao3
        # print(item)                                                                                                                       #没问题
        # yield Request(item["zhiliao_url"], callback=self.parse_zhiliao, meta={"item": deepcopy(item)})
        yield item






