# coding=utf-8
import requests
import re

session = requests.session()  #实例化一个session

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Cookie":"JSESSIONID=2F07C68339865E890C654B1BB4AB7003; tk=zgfBrZ3XotNuF4-u8Z9jdmHwl28eKIOnLPEPpQAEPkEcOyf4mk9290; BIGipServerotn=1039139338.24610.0000; RAIL_EXPIRATION=1546822235736; RAIL_DEVICEID=IwSnBkt7sXTeBRkuReiHQtIyYzrqCh89SbqsbeQWtlKAlL_EixYN8gayqtkdUAIF91PpxxHUVuPmw7v-on6EOG5oBaR9FeR3twnWbWr9SgDPfYMiio4Dbh5QVWVBhjIIvKft_iUoA9KSQ7_xnOOR22I3lVlarX6H; BIGipServerpool_passport=300745226.50215.0000; route=6f50b51faa11b987e576cdb301e545c4"
}

# 使用保存有cookies的session进行后续的操作
# 请求个人主页
r = session.get("http://www.12306.com/index.html", headers=headers)

# 判断是否登陆成功
print(r.content.decode())
