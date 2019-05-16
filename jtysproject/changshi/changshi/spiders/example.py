# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['ask.familydoctor.com']
    start_urls = []

    def start_requests(self):

        list = ["http://nanke.familydoctor.com.cn/nkjb/",
                "http://fuke.familydoctor.com.cn/jb/",
                "http://buyunbuyu.familydoctor.com.cn/by/",
                "http://buyunbuyu.familydoctor.com.cn/nxbyu/",
                "http://xnxg.familydoctor.com.cn/jb/",
                "http://cancer.familydoctor.com.cn/zljb/",
                "http://ganbing.familydoctor.com.cn/gbzl/",
                "http://shen.familydoctor.com.cn/jb/",
                "http://guke.familydoctor.com.cn/gkjb/",
                "http://pf.familydoctor.com.cn/jb/",
                "http://eye.familydoctor.com.cn/jb/",
                "http://erbihou.familydoctor.com.cn/ebhjb/",
                "http://www.familydoctor.com.cn/Mouth/jb/",
                "http://ya.familydoctor.com.cn/ykxm/",
                "http://www.familydoctor.com.cn/intestine/gcjb/",
                "http://www.familydoctor.com.cn/encyclopedia/hx/",
                "http://www.familydoctor.com.cn/encyclopedia/aged/",
                "http://www.familydoctor.com.cn/encyclopedia/sj/jb/",
                "http://www.familydoctor.com.cn/Encyclopedia/sj/jb/js/",
                "http://shimian.familydoctor.com.cn/smjb/",
                "http://www.familydoctor.com.cn/dianxian/dxzs/",
                "http://nanke.familydoctor.com.cn/nkjb/qlx/",
                "http://baidianfeng.familydoctor.com.cn/jibingchangshi/"
                ,"http://changdao.familydoctor.com.cn/cdys/",
                "http://changdao.familydoctor.com.cn/wy/",
                "http://changdao.familydoctor.com.cn/wky/",
                "http://changdao.familydoctor.com.cn/yxy/",
                "http://changdao.familydoctor.com.cn/sgy/",
                "http://changdao.familydoctor.com.cn/fx/",
                "http://changdao.familydoctor.com.cn/xhbl/",
                "http://changdao.familydoctor.com.cn/cyjzhz/",
                "http://teng.familydoctor.com.cn/lb/"
                ]

        for i in list:
                yield Request(i,callback=self.parse)

    def parse(self, response):
        div_list = response.xpath("//div[@class='module mNyList']/div[@class='text']")
        for div in div_list:
                url = div.xpath(".//h4/a/@href").extract_first()

                yield Request(url,callback=self.parse_one,dont_filter=True)

        next_url = response.xpath("//a[text()='下页']/@href").extract_first()
        yield Request(next_url,callback=self.parse,dont_filter=True)


    def parse_one(self,response):
        item = {}
        title_raw = response.xpath("//div[@class='article-titile']/h1/text()").extract_first()
        # print(title_raw)
        item["title"] = title_raw

        p_raw = response.xpath("//div[@class='viewContent']/p")
        disease1 = ""
        for p in p_raw:
            disease_raw = p.xpath(".//text()").extract()
            disease = str(disease_raw).replace("['","").replace("']","").replace(" ","").replace("','",
            "").replace("\\u3000","").replace("\t","").replace("\\t","").replace("\\xa0","").replace("\xa0","")

            if len(disease) > 1:
                disease1 = disease1 + disease + "\n"

        item["disease"] = disease1
        # print(disease1)
        # print(item)
        yield item