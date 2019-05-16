# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DyPipeline(object):
    def process_item(self, item, spider):
        s = str(dict(item)) + "\n"
        with open("./dy.txt", "a", encoding="utf8")as f:
            f.write(s)
        return item



