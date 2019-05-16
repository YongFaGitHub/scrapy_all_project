# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import re

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['zzk.fh21.com.cn/']
    start_urls = []

    def start_requests(self):
        list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for i in list:
            url = "http://zzk.fh21.com.cn/letter/symptoms/{}.html".format(i)
            yield Request(url,callback=self.parse,dont_filter=True)


    def parse(self, response):
        item = {}
        ul_list = response.xpath("//div[@class='border03_body']/ul")
        for ul in ul_list:
            li_list = ul.xpath("./li")
            for li in li_list:
                title = li.xpath("./a/text()").extract_first()
                item["title"] = title
                url_raw = li.xpath("./a/@href").extract_first()
                url_one_raw = "http://zzk.fh21.com.cn" + url_raw
                url_two_raw = url_one_raw.replace("detail","{}") #http://zzk.fh21.com.cn/symptom/{}/6918.html  格式
                # print(url_two_raw)
                item["url"] = url_two_raw

                url = url_two_raw .format("details")  #详细描述，地址

                yield Request(url,callback=self.parse_disease,meta={"item":deepcopy(item)},dont_filter=True)

        next_url_raw = response.xpath("//div[@class='pageStyle']/p/a[text()='下一页']/@href").extract_first()

        if next_url_raw is not  None:
            next_url = "http://zzk.fh21.com.cn" + next_url_raw
            yield Request(next_url,callback=self.parse,dont_filter=True)

    #症状详述
    def parse_disease(self,response):
        item = response.meta["item"]
        disease_raw = response.xpath("//div[@class='detailc']//text()").extract()
        disease = str(disease_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace("\\r",
        "").replace("\\n","").replace("\\t","").replace(" ","").replace("\\u3000","").replace("\\xa0","").replace("','","")
        b = re.findall(r"\n(.*[\┘\┐])\n",disease,re.S)
        try:
            disease = disease.replace(b[0], "")
        except:pass

        item["disease"] = disease


        url = (item["url"]).format("reason")  #起因地址
        yield Request(url,callback=self.parse_qiyin,dont_filter=True,meta={"item":deepcopy(item)})

    #症状起因
    def parse_qiyin(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@id='art_content']/p")
        p_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            p_info = str(p_info_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
            "").replace("\\u3000","").replace("\\xa0","").replace("\\n","").replace("\\t","").replace("\\r","").replace("','","")
            if len(p_info)>1:
                p_s = p_s +p_info +"\n"
        b = re.findall(r"\n(.*[\┘\┐])\n",p_s,re.S)
        try:
            p_s = p_s.replace(b[0], "")
        except:pass

        item["qiyin"] = p_s


        url = (item["url"]).format("identify")  # 鉴别诊断
        yield Request(url, callback=self.parse_jianbie, dont_filter=True, meta={"item": deepcopy(item)})
        # print(disease_raw)

    #鉴别诊断
    def parse_jianbie(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@id='art_content']/p")
        p_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            p_info = str(p_info_raw).replace("['","").replace("']","").replace("[","").replace("]","").replace(" ",
            "").replace("\\u3000","").replace("\\xa0","").replace("\\n","").replace("\\t","").replace("\\r","").replace("','","")
            if len(p_info)>1:
                p_s = p_s +p_info +"\n"
        b = re.findall(r"\n(.*[\┘\┐])\n", p_s, re.S)
        try:
            p_s = p_s.replace(b[0], "")
        except:pass

        item["jianbie"] = p_s
        # print(item)
        url = (item["url"]).format("prevention") #预防地址
        yield Request(url,callback=self.parse_yufang, dont_filter=True, meta={"item": deepcopy(item)})

    #预防
    def parse_yufang(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@id='art_content']/p")
        p_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            p_info = str(p_info_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace(" ",
            "").replace("\\u3000", "").replace("\\xa0", "").replace("\\n", "").replace("\\t", "").replace("\\r",
            "").replace("','","")
            if len(p_info) > 1:
                p_s = p_s + p_info + "\n"

        b = re.findall(r"\n(.*[\┘\┐])\n", p_s, re.S)
        try:
            p_s = p_s.replace(b[0], "")
        except:pass

        item["yufang"] = p_s
        # print(item)
        url = (item["url"]).format("die")  #饮食禁忌
        yield Request(url, callback=self.parse_jinji, dont_filter=True, meta={"item": deepcopy(item)})

    #饮食禁忌
    def parse_jinji(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@id='art_content']/p")
        p_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            p_info = str(p_info_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace(" ",
            "").replace("\\u3000", "").replace("\\xa0", "").replace("\\n", "").replace("\\t", "").replace("\\r", "").replace("','","")
            if len(p_info) > 1:
                p_s = p_s + p_info + "\n"
        b = re.findall(r"\n(.*[\┘\┐])\n", p_s, re.S)
        try:
            p_s = p_s.replace(b[0], "")
        except:pass

        item["jinji"] = p_s

        url = (item["url"]).format("methods") #治疗地址
        yield Request(url, callback=self.parse_zhiliao, dont_filter=True, meta={"item": deepcopy(item)})

    def parse_zhiliao(self,response):
        item = response.meta["item"]
        p_list = response.xpath("//div[@id='art_content']/p")
        p_s = ""
        for p in p_list:
            p_info_raw = p.xpath(".//text()").extract()
            p_info = str(p_info_raw).replace("['", "").replace("']", "").replace("[", "").replace("]", "").replace(" ",
            "").replace("\\u3000", "").replace("\\xa0", "").replace("\\n", "").replace("\\t", "").replace("\\r", "").replace("','","")
            if len(p_info) > 1:
                p_s = p_s + p_info + "\n"
        b = re.findall(r"\n(.*[\┘\┐])\n", p_s, re.S)
        try:
            p_s = p_s.replace(b[0], "")
        except:pass

        item["zhiliao"] = p_s

        url = (item["url"]).format("detail")
        yield Request(url, callback=self.parse_kenengjibing, dont_filter=True, meta={"item": deepcopy(item)})

    def parse_kenengjibing(self,response):
        item = response.meta["item"]

        dl_list =   response.xpath("//div[@class='z_block08_con']/dl")
        p_s = ""
        for dl in dl_list:
            p_raw = dl.xpath("./dt/a/@title").extract_first()
            if len(p_raw)>1:
                p_s = p_s + p_raw +"、"

        item["kenengjibing"] = p_s[:-1]



        # print(item)
        yield item

