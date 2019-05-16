# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi
class JtysscPipeline(object):
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

        tx.execute("insert into jtysscall (big_class,small_class,title,title2,title_img_url,disease_info,gongxiao_disease,gongxiaozuoyong,yingyangjiazhi,shiyirenqun,bushiyirenqun,shiwuxiangke,shiwuxiangyigaikuo,shiwuxiangyi_disease,bianbie,cunchu) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   (item["big_class"],item["small_class"],item["title"],item["title2"],item["title_img_url"],item["disease_info"],item["gongxiao_disease"],item["gongxiaozuoyong"],item["yingyangjiazhi"],
                    item["shiyirenqun"],item["bushiyirenqun"],item["shiwuxiangke"],item["fun_info_show"],item["fun_info_show2"],item["bianbie"],item["cunchu"]
                        ))

