# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi


class XiachufangPipeline(object):
    @classmethod
    def from_settings(cls, settings):
        '''1、@classmethod声明一个类方法，而对于平常我们见到的则叫做实例方法。
           2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
           3、可以通过类来调用，就像C.f()，相当于java中的静态方法'''
        dbparams = dict(
            host=settings['MYSQL_HOST'],  # 读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd='jing1995',
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)  # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        return cls(dbpool)  # 相当于dbpool付给了这个类，self中可以得到

    def __init__(self, dbpool):
        self.dbpool = dbpool

    # pipeline默认调用
    def process_item(self, item, spider):
        # print(item)
        query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
        # query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item

    # 写入数据库中
    def _conditional_insert(self, tx, item):
        # print item['name']

        # sql = "insert into xywy20171108 (titleClass,answer,question) values( %s,%s,%s)"
        # params = (item["titleClass"], item["answer"],item["question"])
        # tx.execute(sql,params)
        # tx.commit()
        tx.execute(
            "insert into xcfsc (big_class,small_class,title,gongxiao,tiaoxuan,cunchu,yingyangzhishi,shiyongrenqun,yinshijinji,zhizuozhishi,bieming,shiling,cunchushijian,disease_info) values( %s,%s, %s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s, %s)",
            ( item["big_class"],
              item["small_class"],
              item["title"],
            item["gongxiao"],
        item["tiaoxuan"],
        item["cunchu"],
        item["yingyangzhishi"],
        item["shiyongrenqun"] ,
        item["yinshijinji"] ,
        item["zhizuozhishi"] ,
        item["bieming"],
        item["shiling"],
        item["cunchushijian"],
        item["disease_info"]))

