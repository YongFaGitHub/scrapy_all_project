# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymysql import *
from twisted.enterprise import adbapi


class XianghaPipeline(object):

    def process_item(self, item, spider):
        conn = connect(
            host="127.0.0.1",
            database="xiangha",
            user="root",
            password="jing1995",
            port=3306,
            charset='utf8'
        )
        cs1 = conn.cursor()
        if item["biaoshi"] == 0:

            cs1.execute("insert into yi_ke(title, query,ke_yi) values( %s,%s,%s)",
                   (item['title'], item['query'], item['ke_yi']))
        else:
            cs1.execute("insert into yuansu(title, reliang, danbaizhi, zhifang, tanshui, qianwei, va, huluobosu, vb1, vb2, danguchun, yansuan, vc, ve, vb6, ca, p, ka, na, mei, tie,zn, xi, tong, mn, shui) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (
                            item["title"],
                            item["reliang"],
                            item["danbaizhi"],
                            item["zhifang"],
                            item["tanshui"],
                            item["qianwei"],
                            item["va"],
                            item["huluobosu"],
                            item["vb1"],
                            item["vb2"],
                            item["danguchun"],
                            item["yansuan"],
                            item["vc"],
                            item["ve"],
                            item["vb6"],
                            item["ca"],
                            item["p"],
                            item["ka"],
                            item["na"],
                            item["mei"],
                            item["tie"],
                            item["zn"],
                            item["xi"],
                            item["tong"],
                            item["mn"],
                            item["shui"],
                        ))

        conn.commit()

        return item







