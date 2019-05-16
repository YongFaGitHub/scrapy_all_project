# -*- coding: utf-8 -*-

# 将 39健康网上的 并发疾病和 相关症状加入到数据库中！！！！！！！！！！！！！！！！！！！！！！！！1
#
#
# import scrapy
# from scrapy.http import Request
#
#
#
#
# # 1，部位，2，大类名 3，详情，详情页的数据
#
#
#
# #  注意点进url链接时的 地址可能为空!!!!!!!!!!!!
#
# class ExampleSpider(scrapy.Spider):
#     name = 'buchong'
#     allowed_domains = ['jbk.39.net/']
#     start_urls = ['http://jbk.39.net/']
#
#     def parse(self, response):
#
#         dl_list = response.xpath("//div[@class='mapList']/dl")
#         # print(url_list)
#         # print("*"*100)
#         #拿到部位
#         for dl in dl_list:
#             position_list =dl.xpath("./dd/div[1]/ul/li")
#             for position in position_list:
#                 # positions_raw = position.xpath("./span[@class='left']/a/text()").extract_first()  #部位
#                 # positions = str(positions_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '').replace("[", "").replace("]", "")
#                 # # print(type(positions))
#                 # # print(positions_raw,"######")
#                 # items['position'] = positions
#                 title_list = position.xpath("./span[@class='right']/a") #病症列表
#                 for title in title_list:
#                     # items["title"] =title.xpath("./text()").extract_first()# 拿到标题
#                     url = title.xpath("./@href").extract()[0]#拿到标题的url
#                     # print(url) 网址没问题
#                     if url is not None:
#                         yield Request(url,callback=self.parse_one,dont_filter=True)
#
#     def parse_one(self,response):
#
#         #找到详情（details）的url,    可能没有详情！！！！！！！！！！！！！！！！！！！
#         details_url = response.xpath("//dl[@class='intro']/dd/a/@href").extract()[0]  #详情的url地址,里面包括想要获得的数据
#         if details_url is not None:
#             yield Request(details_url,callback=self.parse_two,dont_filter=True)
#
#     def parse_two(self,response):
#
#
#         bingfajibing = response.xpath("//i[text()='并发疾病：']/../a[@class='more']/@href").extract_first() # 选择并发疾病的url
#         # print(bingfajibing)
#         if bingfajibing is not None:
#             yield Request(bingfajibing, callback=self.parse_tree,dont_filter=True)
#     def parse_tree(self,response):
#         item = {}
#         title_raw= response.xpath("//div[@class='tit clearfix']/a/h1/text()").extract_first()
#         title = str(title_raw)
#
#         item["title"] = title
#         urlra_raw = response.xpath("//dl[@class='links']/dd/..//text()").extract()
#         urlra = str(urlra_raw).replace("\\r\\n","").replace(" ","").replace("'","").replace("[","").replace("]","")
#         item["urlra"] = urlra
#         ddd = response.xpath("//div[@class='art-box']//text()").extract()
#         dd = str(ddd).replace("\\r\\n","").replace(" ","").replace("'","").replace("[","").replace("]","")
#         item["dd"] = dd
#         yield item
        # print(item)






import scrapy
from scrapy.http import Request




# 1，部位，2，大类名 3，详情，详情页的数据



#  注意点进url链接时的 地址可能为空!!!!!!!!!!!!

class ExampleSpider(scrapy.Spider):
    name = 'buchong'
    allowed_domains = ['jbk.39.net/']
    start_urls = ['http://jbk.39.net/']

    def parse(self, response):

        dl_list = response.xpath("//div[@class='mapList']/dl")
        # print(url_list)
        # print("*"*100)
        #拿到部位
        for dl in dl_list:
            position_list =dl.xpath("./dd/div[1]/ul/li")
            for position in position_list:
                # positions_raw = position.xpath("./span[@class='left']/a/text()").extract_first()  #部位
                # positions = str(positions_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '').replace("[", "").replace("]", "")
                # # print(type(positions))
                # # print(positions_raw,"######")
                # items['position'] = positions
                title_list = position.xpath("./span[@class='right']/a") #病症列表
                for title in title_list:
                    # items["title"] =title.xpath("./text()").extract_first()# 拿到标题
                    url = title.xpath("./@href").extract()[0]#拿到标题的url
                    # print(url) 网址没问题
                    if url is not None:
                        yield Request(url,callback=self.parse_one,dont_filter=True)

    def parse_one(self,response):

        #找到详情（details）的url,    可能没有详情！！！！！！！！！！！！！！！！！！！
        details_url = response.xpath("//dl[@class='intro']/dd/a/@href").extract()[0]  #详情的url地址,里面包括想要获得的数据
        if details_url is not None:
            yield Request(details_url,callback=self.parse_two,dont_filter=True)

    def parse_two(self,response):

        zhengzhuang = response.xpath("//i[text()='相关症状：']/../a[@class='more']/@href").extract_first() # 选择并发疾病的url
        # print(bingfajibing)
        if zhengzhuang is not None:
            yield Request(zhengzhuang, callback=self.parse_tree,dont_filter=True)
    def parse_tree(self,response):
        item = {}
        title_raw= response.xpath("//div[@class='tit clearfix']/a/h1/text()").extract_first()
        title = str(title_raw)

        item["title"] = title
        info_raw = response.xpath("//dl[@class='links']//text()").extract()
        info = str(info_raw).replace("\\xa0","").replace("[","").replace("]","").replace("\\r\\n","").replace(" ","").replace("'","").replace(",,","").replace("。,","").replace("\\u3000","")
        item["info"] = str(info)
        info2_raw = response.xpath("//div[@class='art-box']//text()").extract()
        info2 = str(info2_raw).replace("\\xa0","").replace("[","").replace("]","").replace("\\r\\n","").replace(" ","").replace("'","").replace(",,","").replace("。,","").replace("\\u3000","")
        item["info2"] = str(info2)
        # yield item
        print(item)
        # urlra_raw = response.xpath("//dl[@class='links']/dd/..//text()").extract()
        # urlra = str(urlra_raw).replace("\\r\\n","").replace(" ","").replace("'","").replace("[","").replace("]","").replace("\\n","")
        # item["urlra"] = urlra
        # ddd = response.xpath("//div[@class='art-box']//text()").extract()
        # dd = str(ddd).replace("\\r\\n","").replace(" ","").replace("'","").replace("[","").replace("]","").replace("\\n","")
        # item["dd"] = dd
        # yield item
        # print(item)