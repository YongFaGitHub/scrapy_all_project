# -*- coding: utf-8 -*-

import time
import os
from DumpClient import get_mysql_db
from logger import logger_monitor


def insert_mysql(db_name, file_name):
    contents = open("logs/" + file_name).readlines()

    mysql_conn = get_mysql_db()
    cursor = mysql_conn.cursor()

    # insert_sql = "insert into {0} (ip_port, datetime) VALUES (%s, %s)".format(db_name)
    # update_sql = "update {0} set datetime=%s where ip_port=%s".format(db_name)

    sql = """
            INSERT INTO {0} (ip_port, datetime)
            VALUES (%s, %s) ON DUPLICATE KEY UPDATE datetime=VALUES(datetime)
          """.format(db_name)

    logger_monitor.info("begin insert into mysql....")
    start_time = time.time()

    param_list = list()
    for item in contents:
        item_list = item.split()
        ip_port = item_list[0]
        get_time = item_list[1] + ' ' + item_list[-1]

        param = (ip_port, get_time)
        param_list.append(param)
    try:
        cursor.executemany(sql, param_list)
        mysql_conn.commit()
    except Exception as e:
        logger_monitor.error("insert error msg:%s", e)

    finally:
        cursor.close()
        mysql_conn.close()

    if os.path.exists("logs/" + file_name):
        os.remove("logs/" + file_name)
        logger_monitor.info("delete file:%s", file_name)
    logger_monitor.info("insert mysql consume_time: %s", time.time()-start_time)

if __name__ == '__main__':
    db_name = "yundl_history_ip"
    file_list = os.listdir("logs/")
    for i in file_list:
        if len(i) > 30:
            insert_mysql(db_name=db_name, file_name=i)
