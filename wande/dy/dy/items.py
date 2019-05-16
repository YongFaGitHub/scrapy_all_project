# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    play_count = scrapy.Field()
    comment_count = scrapy.Field()
    share_count = scrapy.Field()
    digg_count = scrapy.Field()
    music_name = scrapy.Field()
    author = scrapy.Field()
    author_id = scrapy.Field()
    desc = scrapy.Field()
    video_addr = scrapy.Field()
