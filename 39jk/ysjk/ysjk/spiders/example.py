# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['jbk.39.net/']
    start_urls = ['http://jbk.39.net/']


    def parse(self, response):
        dl_list = response.xpath("//div[@class='mapList']/dl")
        for dl in dl_list:
            position_list =dl.xpath("./dd/div[1]/ul/li")
            for position in position_list:
                title_list = position.xpath("./span[@class='right']/a") #病症列表
                for title in title_list:
                    # items["title"] =title.xpath("./text()").extract_first()# 拿到标题
                    url_raw = title.xpath("./@href").extract()[0]#拿到标题的url
                    # print(url)
                    url  = url_raw+ "ysbj/"

                    yield Request(url,callback=self.parse_one,dont_filter=True)

    def parse_one(self,response):
        item={}
        title_raw = response.xpath("//div[@class='tit clearfix']/a/h1/text()").extract_first()
        title = str(title_raw)
        item["title"] = title

        title2_raw = response.xpath("//div[@class='tit clearfix']/h2/text()").extract_first()
        title2 = str(title2_raw).replace("）","").replace("（","")
        item["title2"] = title2

        yinshi_raw = response.xpath("//div[@class='yinshi_table']//text()").extract()
        yinshi = str(yinshi_raw).replace("\\r\\n","").replace(" ","").replace("'',","").replace("'",
        "").replace(",,","").replace("。,","。")
        item["yinshi"] = yinshi

        all_raw = response.xpath("//div[@class='art-box']//text()").extract()
        all = str(all_raw).replace("\\r\\n","").replace(" ","").replace("'',","").replace("'",
        "").replace(",,","").replace("。,","。").replace("\\xa0","").replace("\\u3000","").replace("（以上资料仅供参考，详细情况询问医生),",
        "").replace("：,","：").replace("(以上资料仅供参考，详细请咨询医生),","")
        item["all"] = all

        yield item
        # print(item)






