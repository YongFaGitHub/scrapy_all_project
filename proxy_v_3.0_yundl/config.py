#!/usr/bin/env python
# -*- coding: utf-8 -*-
HEADER = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2693.2 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'close',
    # 'Accept-Encoding': 'gzip, deflate',
}

PROXYPOOL_CONFIG = {
    'MIN_IP_NUM': 1000,  # 代理池中最小可用ip数量，若检测到小于此数量，启动爬虫
    'DELETE_TIME': 24 * 60,  # minutes, 删除24小时之前的ip
    'UPDATE_TIME': 10, # minutes, 验证10分钟之前ip的代理状态
    'CRAWL_TIME': 30 }  #每30分钟一次，所以查询30分钟之前的sql数据量

API_CONFIG = {
    # 'HOST': '10.44.163.19',
    # 'PORT': 8080
}
# out_redis_host = '101.200.174.92' #test_host
# in_redis_host = '10.44.163.19'
#
# out_redis_host = '112.124.17.26'
# in_redis_host = '10.160.15.209'
REDIS_CONFIG={    #
    "OUT_HOST":'localhost',
    "IN_HOST":'localhost',
    "PORT":6379,
    "PASSWD":"donews1234",
    "DB_NUM":4
}
MYSQL_CONFIG={
    "OUT_HOST":'localhost',
    "IN_HOST":'localhost',
    "PORT":3306,
    "USER":'root',
    'DB':'yuwande',
    "PASSWD":"mysql",
}

# REDIS_CONFIG = {  #test
#     "OUT_HOST": '101.200.174.92',
#     "IN_HOST": '10.44.163.19',
#     "PORT": 6379,
#     "PASSWD": "donews_1234",
#     "DB_NUM": 3
# }

CRAWLER_CONFIG = {
    'THREAD_NUM': 20,
    'TIMEOUT': 60,
    'RETRY_TIMES': 5
}

VALIDATE_CONFIG = {
    'THREAD_NUM': 1,
    'TIMEOUT': 20,
    # 'TIMEOUT': 10,
    'PROXY_TYPE': [0, 1, 2, 3],
    'HTTP_TARGET': 'http://fetch.bestzsj.com/v1/validate_ip_https',
    'HTTPS_TARGET': 'https://fetch.bestzsj.com/v1/validate_ip_https',
}



LOG_CONFIG = {
    'LOG_TO_FILE': True, #修改日志输出到文件
    'LOG_TO_PRINT': False,
    'FILE_PATH': './logs/proxyPool.log',
    'IP_FILE_PATH':'./logs/proxyIP.log',
    'MONITOR_FILE_PATH':'./logs/monitor.log'
}
