#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import platform
from config import REDIS_CONFIG
from config import MYSQL_CONFIG
from logger import logger
import traceback
import MySQLdb


def get_host(CONFIG):
    real_host = ''
    if 'Window' in platform.system():
        real_host = CONFIG['OUT_HOST']
    else:
        real_host = CONFIG['IN_HOST']
    return real_host


def get_redis_client(client=None):
    real_redis_host=get_host(REDIS_CONFIG)
    try:
        if not client:
            client = redis.StrictRedis(host=real_redis_host, port=REDIS_CONFIG['PORT'], password=REDIS_CONFIG['PASSWD'], db=REDIS_CONFIG['DB_NUM'])
        return client
    except Exception as e:
        logger.error("Redis connection error %s", traceback.format_exc())


def get_mysql_db(conn=None):
    try:
        real_mysql_host=get_host(MYSQL_CONFIG)
        if not conn:
            conn=MySQLdb.connect(host=real_mysql_host, user=MYSQL_CONFIG['USER'], passwd=MYSQL_CONFIG['PASSWD'], db=MYSQL_CONFIG['DB'], port=MYSQL_CONFIG['PORT'])
        return conn
    except Exception as e:
        logger.error("Mysql connection error %s", traceback.format_exc())

redis_client=get_redis_client()
# mysql_conn=get_mysql_db()
