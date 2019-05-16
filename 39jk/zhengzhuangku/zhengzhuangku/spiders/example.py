# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import time
class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['jbk.39.net/']
    start_urls = ['http://jbk.39.net/bw_t2/']

    def parse(self, response):
        item = {}
        div_list = response.xpath("//div[@class='res_list']")
        for div in div_list:

            title = div.xpath("./dl/dt/h3/a/@title").extract_first()
            item["title"] = title
            # item["a"] = 0
            # item["b"] = 0
            # item["c"] = 0
            # item["d"] = 0
            # item["e"] = 0


            url = div.xpath("./dl/dt/h3/a/@href").extract_first()
            item["url"] = url
            print(url)

            yield Request(url,callback=self.parse_disease,dont_filter=True,meta={"item":deepcopy(item)})


        next_url_raw = response.xpath("//div[@class='site-pages']/a[text()='下页']/@href").extract_first()
        next_url = "http://jbk.39.net" + next_url_raw
        yield Request(next_url,callback=self.parse,dont_filter=True,meta={"item":deepcopy(item)})

    def parse_disease(self,response):
        item=response.meta["item"]
        #图片存储
        img_url  = response.xpath("//div[@class='intro clearfix']/a[@class='pic']/img/@src").extract_first()
        item["img_url"] = img_url

        yield Request(img_url,callback=self.img_cun,meta={"item":deepcopy(item)},dont_filter=True)

    def img_cun(self,response):
        item = response.meta["item"]

        # with open("I:/症状图片/39jk/{}.jpg".format(item["title"]),"wb") as f:
        #     f.write(response.body)

        with open("H:/pycharmproject/project/39jk/zhengzhuangku/zhengzhuangku/spiders/title.txt","a+",encoding="utf-8") as f:
            f.write(item["title"])
            f.write("、")
            f.write(item["img_url"])
            f.write("\n")

        # yield item




        #详细信息
    #     info_raw = response.xpath("//dd[@id='intro']/p[@class='sort2']/text()").extract()
    #     info = str(info_raw).replace("['","").replace("']","").replace("\\u3000","").replace("\\xa0","")
    #     item["disease"] = info
    #
    #     #可能疾病的列表
    #     tr_list = response.xpath("//div[@class='item']//tr[1]/following-sibling::*")
    #     name_s = ""
    #     for tr in tr_list:
    #         name_raw = tr.xpath("./td[1]/a/@title").extract_first()
    #         name_s = name_s + name_raw +"、"
    #
    #     item["kenengjibing"] = name_s[:-1]
    #     # print(item)
    #     url = item["url"] + "zzqy/"
    #     yield Request(url,callback=self.parse_qiyin,meta={"item":deepcopy(item)},dont_filter=True)
    #
    # def parse_qiyin(self,response):
    #     item = response.meta["item"]
    #     p_list = response.xpath("//div[@class='item catalogItem']/p")
    #     p_s = ""
    #     for p in p_list:
    #         p_raw = p.xpath(".//text()").extract()
    #         p_info = str(p_raw).replace("['","").replace("']","").replace("\\u3000","").replace("\\xa0",
    #         "").replace(" ","").replace("','","").replace("&rdquo;","").replace("&ldquo;","")
    #         if len(p_info)>1:
    #             p_s = p_s + p_info +"\n"
    #     # print(p_s)
    #     item["qiyin"] = p_s
    #
    #     url = item["url"] +"zdxs/"
    #     yield Request(url,callback=self.parse_zhenduan,meta={"item":deepcopy(item)},dont_filter=True)
    #
    # def parse_zhenduan(self,response):
    #     item = response.meta["item"]
    #
    #     p_list = response.xpath("//div[@class='item catalogItem']/p")
    #     p_s = ""
    #     for p in p_list:
    #         p_raw = p.xpath(".//text()").extract()
    #         p_info = str(p_raw).replace("['", "").replace("']", "").replace("\\u3000", "").replace("\\xa0",
    #         "").replace(" ","").replace("','", "").replace("&rdquo;","").replace("&ldquo;","")
    #         if len(p_info) > 1:
    #             p_s = p_s + p_info + "\n"
    #
    #     item["zhenduan"] = p_s
    #     url = item["url"] +"jcjb/"
    #     yield Request(url,callback=self.parse_jiancha,meta={"item":deepcopy(item)},dont_filter=True)
    #
    # def parse_jiancha(self,response):
    #     item = response.meta["item"]
    #     tr_list = response.xpath("//div[@class='checkbox-data']//tr[1]/following-sibling::*")
    #     name_s = ""
    #     for tr in tr_list:
    #         name_raw = tr.xpath("./td[1]/a/text()").extract_first()
    #         name_s = name_s + name_raw + "、"
    #
    #     item["jiancha"] = name_s[:-1]
    #     url = item["url"] + "jzzn/"
    #     yield Request(url,callback=self.parse_zhinan,meta={"item":deepcopy(item)},dont_filter=True)
    #
    # def parse_zhinan(self,response):
    #     item = response.meta["item"]
    #     dl_list = response.xpath("//div[@class='zn-main']/dl")
    #     p_s = ""
    #     for dl in dl_list:
    #         p_raw = dl.xpath(".//text()").extract()
    #         p_info = str(p_raw).replace("['","").replace("']","").replace(" ","").replace("\\r","").replace("\\n",
    #         "").replace("','','","\n").replace("','","").replace("\\u3000","").replace("\\xa0","")
    #         if len(p_info)>1:
    #             p_s = p_s + p_info+"\n"
    #     item["zhinan"] = p_s
    #
    #
    #     # print(item)
    #
    #     yield item






    # def parse_disease(self,response):
    #     item=response.meta["item"]
    #     if item["a"] == 0:
    #         info_raw = response.xpath("//dd[@id='intro']/p[@class='sort2']/text()").extract()
    #         info = str(info_raw).replace("['","").replace("']","").replace("\\u3000","").replace("\\xa0","")
    #         item["disease"] = info
    #         item["a"] = 1
    #     # print(item["title"],info)
    #
    #     if item["b"] ==0:
    #         qiyin_url = response.xpath("//div[@id='list_nav']/ul/li[text()='症状起因']/@href").extract_first()
    #         if qiyin_url is not None:
    #             yield Request(qiyin_url,callback=self.parse_qiyin,meta={"item":deepcopy(item)})
    #
    #     if item["c"] == 0:
    #         zhenduan_url =  response.xpath("//div[@id='list_nav']/ul/li[text()='诊断详述']/@href").extract_first()
    #         if zhenduan_url is not None:
    #             yield Request(zhenduan_url,callback=self.parse_zhenduan,meta={"item":deepcopy(item)})
    #
    #     if item["d"] == 0:
    #         jiancha_url = response.xpath("//div[@id='list_nav']/ul/li[text()='检查鉴别']/@href").extract_first()
    #         if jiancha_url is not None:
    #             yield Request(jiancha_url,callback=self.parse_jiancha,meta={"item":deepcopy(item)})
    #
    #     if item["e"] == 0:
    #         jiuzhen_url = response.xpath("//div[@id='list_nav']/ul/li[text()='就诊指南']/@href").extract_first()
    #         if jiuzhen_url is not None:
    #             yield Request(jiuzhen_url,callback=self.parse_jiuzhen,meta={"item":deepcopy(item)})
    #
    #
    #
    #
    # def parse_qiyin(self,response):
    #     item = response.meta["item"]
    #     item["b"] =1
    #
    #
    # def parse_zhenduan(self,response):
    #     item = response.meta["item"]
    #     item["c"] =1
    #
    # def parse_jiancha(self,response):
    #     item = response.meta["item"]
    #     item["d"] = 1
    #
    # def parse_jiuzhen(self,response):
    #     item = response.meta["item"]
    #     item["e"] = 1
