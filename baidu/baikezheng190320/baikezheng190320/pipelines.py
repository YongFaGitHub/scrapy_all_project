# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi


class Baikezheng190320Pipeline(object):

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

        sql = """insert into baidu_zhenghou(title,病因病机, 证候特征, 临床表现, 治法, 常用方剂, 常用中药,
              常见病证, 预防调护,常见证型, 转归预后, 概述, 证候关系, 治法方药, 常用腧穴, 病因, 治疗, 鉴别诊断,
               检查, 其他疗法, 常用方药, 饮食调护,历代论述, 注意事项, 家庭治疗措施, 病理机制, 常见证候)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        tx.execute(sql, (item["title"],
                    item['病因病机'],
                    item['证候特征'],
                    item['临床表现'],
                    item['治法'],
                    item['常用方剂'],
                    item['常用中药'],
                    item['常见病证'],
                    item['预防调护'],
                    item['常见证型'],
                    item['转归预后'],
                    item['概述'],
                    item['证候关系'],
                    item['治法方药'],
                    item['常用腧穴'],
                    item['病因'],
                    item['治疗'],
                    item['鉴别诊断'],
                    item['检查'],
                    item['其他疗法'],
                    item['常用方药'],
                    item['饮食调护'],
                    item['历代论述'],
                    item['注意事项'],
                    item['家庭治疗措施'],
                    item['病理机制'],
                    item['常见证候'],))