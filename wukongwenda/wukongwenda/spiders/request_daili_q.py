import requests
import json
import random
import pymysql


# 获取可以使用的代理ip
def daili_tiqu():

    daili_url = "http://gea.ip3366.net/api/?key=20181105112519230&getnum=30&area=1&order=2&proxytype=0"
    while 1:
        r = requests.get(daili_url)
        ip_txt = (r.content.decode())
        ip_list = ip_txt.split("\r\n")
        for ip_one in ip_list:
            # ip = "https://" + ip_one
            proxies = {'http': "http://" + ip_one}
            print("正在测试%s" % ip_one)
            try:
                r = requests.get("http://fetch.bestzsj.com/v1/validate_ip_https", proxies=proxies, timeout=3)
                # print(r.content)
                wukong(proxies)
            except:
                print("代理不可用%s" % ip_one)


# 获取悟空问答的数据
def wukong(proxies):
    print("已经使用%s" % proxies )
    id_list = ["6215497895248923137", "6215497899774577154"]
    id = random.choice(id_list)
    if id == "6215497895248923137":
        class_name = "健康"
    else:
        class_name = "美食"
    url = "https://www.wukong.com/wenda/web/nativefeed/brow/?concern_id={}".format(id)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        "cookie": "tt_webid=6626204913008412164; wendacsrftoken=3369c7ab7c433a99e0f5c29f46b27774; tt_webid=6626204913008412164; answer_finalFrom=; cookie_tt_page=97332cc2ca86d7f3c5e77624c96aca0f; _ga=GA1.2.1229206126.1542783557; _gid=GA1.2.1477376751.1542783557; answer_enterFrom=; wenda_last_concern_id=6215497899774577154"
        }


    q_content = requests.get(url, headers=headers, proxies=proxies, timeout=6)
    q_list = json.loads(q_content.content)
    data_list = q_list["data"]
    for data in data_list:
        question = data["question"]["title"]
        insert_mysql(class_name,question)



def insert_mysql(class_name,question):
    conn = pymysql.connect(
    host="127.0.0.1",
    database="wukong",
    user="root",
    password="jing1995",
    port=3306,
    charset='utf8'
    )
    cs1 = conn.cursor()
    sql = "insert into wukongwenda_q(class_name,question) values(%s,%s)"
    cs1.execute(sql, (class_name, question))
    conn.commit()
    print("%s:%s" % (class_name,question))

if __name__ == '__main__':
    daili_tiqu()




