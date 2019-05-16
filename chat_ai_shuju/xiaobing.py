#-*-encoding:utf-8 -*-
# 微软小冰链接：http://kan.msxiaobing.com/V3/Portal?task=yanzhi
import requests
import json
import time
import base64
from bs4 import BeautifulSoup

session = requests.Session()

# 获取参数tid
def getTid():
	url = 'http://kan.msxiaobing.com/V3/Portal?task=yanzhi'
	req = session.get(url)
	soup = BeautifulSoup(req.text,'html.parser')
	return soup.select('#xb_log_info input')[0]['value']


