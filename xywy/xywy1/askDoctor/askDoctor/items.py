# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class AskdoctorItem(scrapy.Item):
    # define the fields for your item here like:
     #siteURL = scrapy.Field()#首页中各个问题的URL
     question = scrapy.Field() #患者提问的问题
     titleClass=scrapy.Field()
     answer= scrapy.Field()
     gender=scrapy.Field ()


     age = scrapy.Field()


     #answer_structor = scrapy.Field()#医生的回答
     #answer_analyse = scrapy.Field()
     #pageURL = scrapy.Field()#每一个问题的入口地址
     #age_sex = scrapy.Field()
