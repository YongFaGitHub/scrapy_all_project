# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi
class JtysPipeline(object):
    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],  # 读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd='jing1995',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,

            use_unicode=False,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        return cls(dbpool)

    def __init__(self, dbpool):
        self.dbpool = dbpool

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
        return item


    def _conditional_insert(self, tx, item):

        tx.execute("insert into jtysdata (big_class,title,question_title,question,answer) values(%s,%s,%s,%s,%s)",
                   (item["big_class"],item["small_class2"],item["question_title"],item["question"],item["answer"]))

