# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['http://www.9939.com/']
    start_urls = ['http://jb.9939.com/jbzz_t1/']

    def parse(self, response):
        item = {}
        div_list = response.xpath("//div[@class='sbox']/div[@class='doc_anwer disline']")
        for div in div_list:
            url_raw = div.xpath("./div[1]/div//a/@href").extract_first()

            title_raw = div.xpath("./div[1]/div//a/text()").extract_first()
            title = str(title_raw).replace("\r","").replace("\n","").replace("\t","")
            item["title"] = title
            # print(url_raw)
            #进入小类别的页面
            yield Request(url_raw,callback=self.parse_one,meta={"item": deepcopy(item)},dont_filter=True)
        #进入下一页的地址
        next_url_raw = response.xpath("//a[text()='下一页>>']/@href").extract_first()
        next_url = "http://jb.9939.com" + next_url_raw
        yield Request(next_url,callback=self.parse,dont_filter=True)
    #进入详情页面
    def parse_one(self,response):
        item = response.meta["item"]
        url_raw = response.xpath("//div[@class='widsp']//a[text()='[详细]']/@href").extract_first()
        url = "http://jb.9939.com" + url_raw
        yield Request(url,callback=self.parse_two,meta={"item": deepcopy(item)},dont_filter=True)

    #疾病简介、科室、药品
    def parse_two(self,response):
        item = response.meta["item"]

        disease_raw = response.xpath("//div[@class='tost bshare spread graco']/p/text()").extract_first()
        disease = str(disease_raw)
        item["disease"] = disease

        keshi_len = response.xpath("//div[@class='tost nickn aknol graco']//span[text()='就诊科室：']/../*")
        if len(keshi_len) > 1:

            keshi_raw = response.xpath("//div[@class='tost nickn aknol graco']//span[text()='就诊科室：']/following-sibling::*/text()").extract()
            keshi = str(keshi_raw).replace(" ","").replace("[","").replace("]","").replace("'","").replace(",","、")
            item["keshi"] = keshi
        else:
            item["keshi"] = '暂无'



        yaopin_raw = response.xpath("//div[@class='tost nickn aknol graco']//span[text()='常用药品：']/following-sibling::*//text()").extract()
        yaopin = str(yaopin_raw).replace("\\r\\n","").replace(" ","").replace("','','","、").replace("['",
        "").replace("']","").replace("','","")
        if len(yaopin) > 2:
            item["yaopin"] = yaopin

        else:
            item["yaopin"] = "暂无"


        zhiliao_raw = response.xpath("//div[@class='tost nickn aknol graco']//span[text()='治疗方法：']/../text()").extract()
        zhiliao = str(zhiliao_raw)
        item["zhiliao"] = zhiliao.replace("[","").replace("]","").replace("'","").replace(" ","、")

        dianxingzhengzhuang_raw = response.xpath("//div[@class='tost nickn graco']//span[text()='典型症状：']/../following-sibling::*//text()").extract()

        dianxingzhengzhuang = str(dianxingzhengzhuang_raw).replace("\\r\\n","").replace(" ","").replace("','','","、").replace("['",
            "").replace("']","").replace("','","")
        if len(dianxingzhengzhuang) > 1:
            item["dianxingzhengzhuang"] = dianxingzhengzhuang
        else:
            item["dianxingzhengzhuang"] = "暂无"

        bingyin_url_raw = response.xpath("//div[@class='absbar']/ul/li/a[text()='病 因']/@href").extract_first()
        bingyin_url = "http://jb.9939.com" + bingyin_url_raw


        yield Request(bingyin_url,callback=self.parse_bingyin,meta={"item": deepcopy(item)},dont_filter=True)

    #疾病病因
    def parse_bingyin(self,response):
        item = response.meta["item"]

        bingyin_list = response.xpath("//div[@class='tost nickn bshare prevp spread graco']/p")
        bingyin_f = ""
        for bingyin_s in bingyin_list:
            bingyin_raw = bingyin_s.xpath(".//text()").extract()
            bingyin = str(bingyin_raw).replace("[","").replace("]","").replace("'","").replace("\\r",
            "").replace(" ","")
            if len(bingyin) > 1 :
                bingyin_f = bingyin_f + bingyin +"\n"
        item["bingyin"] = bingyin_f


        yufang_url_raw = response.xpath("//div[@class='absbar']/ul/li/a[text()='预 防']/@href").extract_first()
        yufang_url = "http://jb.9939.com" + yufang_url_raw


        yield Request(yufang_url, callback=self.parse_yufang, meta={"item": deepcopy(item)}, dont_filter=True)


#疾病预防
    def parse_yufang(self,response):
        item = response.meta["item"]
        yufang_f = ""
        yufang_list = response.xpath("//div[@class='tost nickn bshare spread graco']/p")
        for yufang_s in yufang_list:
            yufang_raw = yufang_s.xpath(".//text()").extract()
            yufang = str(yufang_raw).replace("[","").replace(" ","").replace("\\r","").replace("','","").replace("]",
            "").replace("'","")
            if len(yufang) >1:
                yufang_f = yufang_f + yufang +"\n"

        item["yufang"] = yufang_f

        jiancha_url_raw = response.xpath("//div[@class='absbar']/ul/li/a[text()='检 查']/@href").extract_first()
        jiancha_url = "http://jb.9939.com" + jiancha_url_raw
        yield Request(jiancha_url, callback=self.parse_jiancha, meta={"item": deepcopy(item)}, dont_filter=True)
#检查
    def parse_jiancha(self,response):
        item = response.meta["item"]
        jiancha_raw = response.xpath("//div[@class='tost nickn bshare spread graco']/p[1]//text()").extract()
        jiancha = str(jiancha_raw).replace("['\\r\\n                ', '","").replace(" ","").replace("','",
        "、").replace("', '            ']","").replace("、']","").replace("[","").replace("]","").replace("\\n",
        "").replace("\\r","").replace("'","")
        if len(jiancha) >1:
            item["jiancha"] = jiancha

        else:
            item["jiancha"] = "暂无"

        jianbie_url_raw = response.xpath("//div[@class='absbar']/ul/li/a[text()='鉴 别']/@href").extract_first()
        jianbie_url = "http://jb.9939.com" + jianbie_url_raw
        yield Request(jianbie_url, callback=self.parse_jianbie, meta={"item": deepcopy(item)}, dont_filter=True)


#鉴别
    def parse_jianbie(self,response):
        item = response.meta["item"]
        jianbie_f = ""
        jianbie_list = response.xpath("//div[@class='tost nickn bshare spread graco']/p")
        for p in jianbie_list:
            jianbie_raw = p.xpath(".//text()").extract()

            jianbie = str(jianbie_raw).replace("[","").replace("]","").replace("'","").replace("\\r","").replace(" ",
            "").replace("&rdquo","").replace("&ldquo","").replace("','",
            "").replace("（温馨提示：以上资料仅供参考，具体情况请向医生详细咨询）","")
            if len(jianbie)>1:
                jianbie_f = jianbie_f + jianbie +"\n"


        item["jianbie"] = jianbie_f

        huli_url_raw = response.xpath("//div[@class='absbar']/ul/li/a[text()='护 理']/@href").extract_first()
        huli_url = "http://jb.9939.com" + huli_url_raw
        yield Request(huli_url, callback=self.parse_huli, meta={"item": deepcopy(item)}, dont_filter=True)


#护理
    def parse_huli(self,response):
        item = response.meta["item"]
        huli__list = response.xpath("//div[@class='tost nickn bshare prevp spread graco']/p")
        huli_f = ""
        for p in huli__list:
            huli_raw = p.xpath(".//text()").extract()
            huli = str(huli_raw).replace("[","").replace("]","").replace(" ","").replace("'","").replace("\\u3000",
            "").replace("\\r","").replace("（温馨提示：以上资料仅供参考，具体情况请向医生详细咨询）","")
            if len(huli)>1:
                huli_f = huli_f + huli +"\n"

        item["huli"] = huli_f

        zhiliao_url_raw = response.xpath("//div[@class='absbar']/ul/li/a[text()='治 疗']/@href").extract_first()
        zhiliao_url = "http://jb.9939.com" + zhiliao_url_raw
        yield Request(zhiliao_url, callback=self.parse_zhiliao, meta={"item": deepcopy(item)}, dont_filter=True)


    def parse_zhiliao(self,response):
        item = response.meta["item"]

        zhiliao_list = response.xpath("//div[@class='tost nickn bshare prevp spread graco']/p")
        zhiliao_f = ""
        for p in zhiliao_list:
            zhiliao_raw = p.xpath(".//text()").extract()
            zhiliao = str(zhiliao_raw).replace("[", "").replace("]", "").replace(" ", "").replace("'", "").replace(
            "\\u3000", "").replace("\\r","").replace("\\n","\n").replace("（温馨提示：以上资料仅供参考，具体情况请向医生详细咨询）", "")
            if len(zhiliao) > 1:
                zhiliao_f = zhiliao_f + zhiliao + "\n"
        print(item["title"])
        # print(zhiliao_f)

        item["zhiliao_disease"] = zhiliao_f


        # print(item)

        # print(item)

        yield item




