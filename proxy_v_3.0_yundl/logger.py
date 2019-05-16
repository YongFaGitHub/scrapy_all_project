#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from config import LOG_CONFIG
from logging.handlers import RotatingFileHandler


def set_fh(fmt,file_name):
    fh = RotatingFileHandler(file_name, maxBytes=1024 * 1024 * 100, backupCount=10 * 72)
    fh.setFormatter(fmt)
    fh.setLevel(logging.DEBUG)
    return fh

def set_proxy_logs(fmt):
    file_name=LOG_CONFIG['FILE_PATH']
    return set_fh(fmt,file_name)

def set_monitor_logs(fmt):
    file_name=LOG_CONFIG['MONITOR_FILE_PATH']
    return set_fh(fmt,file_name)

def set_proxy_Ip(fmt):
    file_name=LOG_CONFIG['IP_FILE_PATH']
    return set_fh(fmt,file_name)
def get_logger(log_name,set_log,fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')):

    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        # logging format
        # filehandler
        if LOG_CONFIG['LOG_TO_FILE']:
            #fh = logging.FileHandler(LOG_CONFIG['PATH'])
            # 使用更高级的handler处理日志,日志大小100M，保留历史个数10*72
            fh=set_log(fmt)
            logger.addHandler(fh)
        # streamhandler
        if LOG_CONFIG['LOG_TO_PRINT']:
            ch = logging.StreamHandler()
            ch.setFormatter(fmt)
            ch.setLevel(logging.INFO)
            logger.addHandler(ch)
    return logger

logger_monitor=get_logger('monitor_ip',set_monitor_logs)
# logger_ip = get_logger('proxyIp',set_proxy_Ip,fmt = logging.Formatter('%(message)s %(asctime)s '))
logger=get_logger('proxyLogs',set_proxy_logs)
