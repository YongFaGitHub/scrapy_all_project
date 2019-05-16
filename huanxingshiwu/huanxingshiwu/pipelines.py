# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi



class HuanxingshiwuPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

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

    # pipeline默认调用
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
        # query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item

    # 写入数据库中
    def _conditional_insert(self, tx, item):
        tx.execute("""insert into shiwuyuansu(title, aa_switch, 1_value, 1_level, 0_value, 0_level,
                      kcal, kcal_fen, protein, protein_fen, fat,fat_fen, carbo, carbo_fen,
                      fibre, fibre_fen,mufas, mufas_fen, pufas,pufas_fen, pufas_percent,
                      pufas_percent_fen, tfa, tfa_fen, tfa_percent, tfa_percent_fen, cholesterol,
                      cholesterol_fen, phytosterol, phytosterol_fen, carotene, carotene_fen,
                      l_z_c,l_z_c_fen, lycopene, lycopene_fen, ca, ca_fen, mg, mg_fen, na, na_fen,
                      k, k_fen, p, p_fen, s, s_fen, cl, cl_fen, fe, fe_fen, i, i_fen, zu,zu_fen, se,
                      se_fen, cu, cu_fen, mn, mn_fen, f, f_fen, va, va_fen, vc, vc_fen, vd,vd_fen,
                      ve, ve_fen, vk, vk_fen,vp,vp_fen, b1, b1_fen, b2, b2_fen, b3, b3_fen, b4, b4_fen,
                      b5, b5_fen, b6, b6_fen,b7,b7_fen, b9, b9_fen, b12, b12_fen, b14, b14_fen, leu, leu_fen,
                      met, met_fen, thr, thr_fen, lys, lys_fen, trp, trp_fen, val, val_fen, his, his_fen, ile,
                      ile_fen, phe, phe_fen) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                      %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                      %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                      ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                      %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                   (item["query"], item["aa_switch"], item["1_value"], item["1_level"], item["0_value"], item["0_level"],
                    item['kcal'], item['kcal_fen'],
                    item['protein'], item['protein_fen'],
                    item['fat'], item['fat_fen'],
                    item['carbo'], item['carbo_fen'],
                    item['fibre'], item['fibre_fen'],
                    item['mufas'], item['mufas_fen'],
                    item['pufas'], item['pufas_fen'],
                    item['pufas_percent'], item['pufas_percent_fen'],
                    item['tfa'], item['tfa_fen'],
                    item['tfa_percent'], item['tfa_percent_fen'],
                    item['cholesterol'], item['cholesterol_fen'],
                    item['phytosterol'], item['phytosterol_fen'],
                    item['carotene'], item['carotene_fen'],
                    item['l_z_c'], item['l_z_c_fen'],
                    item['lycopene'], item['lycopene_fen'],
                    item['ca'], item['ca_fen'],
                    item['mg'], item['mg_fen'],
                    item['na'], item['na_fen'],
                    item['k'], item['k_fen'],
                    item['p'], item['p_fen'],
                    item['s'], item['s_fen'],
                    item['cl'], item['cl_fen'],
                    item['fe'], item['fe_fen'],
                    item['i'], item['i_fen'],
                    item['zu'], item['zu_fen'],
                    item['se'], item['se_fen'],
                    item['cu'], item['cu_fen'],
                    item['mn'], item['mn_fen'],
                    item['f'], item['f_fen'],
                    item['va'], item['va_fen'],
                    item['vc'], item['vc_fen'],
                    item['vd'], item['vd_fen'],
                    item['ve'], item['ve_fen'],
                    item['vk'], item['vk_fen'],
                    item['vp'], item['vp_fen'],
                    item['b1'], item['b1_fen'],
                    item['b2'], item['b2_fen'],
                    item['b3'], item['b3_fen'],
                    item['b4'], item['b4_fen'],
                    item['b5'], item['b5_fen'],
                    item['b6'], item['b6_fen'],
                    item['b7'], item['b7_fen'],
                    item['b9'], item['b9_fen'],
                    item['b12'], item['b12_fen'],
                    item['b14'], item['b14_fen'],
                    item['leu'], item['leu_fen'],
                    item['met'], item['met_fen'],
                    item['thr'], item['thr_fen'],
                    item['lys'], item['lys_fen'],
                    item['trp'], item['trp_fen'],
                    item['val'], item['val_fen'],
                    item['his'], item['his_fen'],
                    item['ile'], item['ile_fen'],
                    item['phe'], item['phe_fen'],))

