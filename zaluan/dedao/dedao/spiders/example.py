# -*- coding: utf-8 -*-
# import scrapy
# import csv
# from copy import deepcopy
# from scrapy import Request
# import os
# import re
#
# class ExampleSpider(scrapy.Spider):
#     name = 'jieba_try'
#     allowed_domains = ['cdn.steamstatic.com.8686c.com']
#     start_urls = ["https://cdn.steamstatic.com.8686c.com/steam/apps/500/0000006035.1920x1080.jpg?t=1517005754"]
#
#     def parse(self,response):
#         print(response.body)
#         print(type(response.body),"@#@#@#@#"*20)



    # # 直接构造首次请求
    # def start_requests(self):
    #     # 读取存储的数据文件路径（与fiddler设置存储的文件为同一地址）
    #     file = open("H:/pycharmproject/project/zaluan/dedao/dedao/spiders/FIDDLER2.txt","rt",encoding="utf-8")
    #     read = csv.reader(file)
    #
    #     for line2 in read:
    #         if len(line2) > 1: #判断不为空
    #             item = {}
    #
    #             #拿出地址和视频标题信息
    #
    #             for i in line2: #遍历出内容
    #                 if "mp3_play_url" in i:  #url地址
    #                     item["url"] = i.replace("\\","").replace("mp3_play_url:","").replace('"',"")
    #                     print(item["url"])
    #
    #                 if "source_name" in i:#栏目名称
    #                     class_name_1 = re.findall('source_name:"(.*?)"',i)
    #                     class_name2 = (class_name_1[0]).encode('utf-8').decode('unicode_escape')
    #                     class_name = class_name2.replace("|","、").replace(" ","")
    #                     item["class"]  = class_name
    #                     print(class_name,"@@@@@@@@@@@@@@@@")
    #                 if "title" in i and "share_title"  not in i:
    #                     i2  = re.findall('title:"(.*?)"',i)
    #                     title_name2 = (i2[0]).encode('utf-8').decode('unicode_escape')
    #                     title_name = title_name2.replace("|", "、").replace(" ", "")
    #                     print(title_name,"########################")
    #                     item["title"] = title_name
    #
    #
    #
    #
    #             yield Request(item["url"] ,callback=self.parse,meta={"item":deepcopy(item)})
    #     file.close()
    #     os.remove("H:/pycharmproject/project/zaluan/dedao/dedao/spiders/FIDDLER2.txt") #删除存储视频信息的文件（与fiddler设置存储的文件为同一地址）
    #
    # # 保存音频文件，设置路径
    # def parse(self, response):
    #     item = response.meta["item"]
    #     '''
    #     item["class"]，为栏目名称
    #     item["title] ,为视频标题名称
    #     测试文件的地址在I盘根目录下
    #     '''
    #
    #     try : os.mkdir("I:/{}".format(item["class"]))   #视频文件的保存到本地的路径，构建目录，（本次是I盘根目录下创建栏目文件夹）
    #     except:pass
    #
    #     #写入本地文件
    #     with open ("I:/{}/{}.m4a".format(item["class"],item["title"]),"wb") as f:
    #         f.write(response.body)
    #         print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")



import requests
url ='https://cdn.steamstatic.com.8686c.com/steam/apps/500/0000006035.1920x1080.jpg?t=1517005754'
r = requests.get(url)
print (type(r.content))
with open("./tu.txt","wb") as f:
    f.write(r.content)
