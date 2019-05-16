# import csv
#
# file = open("./http.txt","r")
#
# read = csv.reader(file)
#
# for line in read:
#     print(len(line))
#     for i in line:
#         print(i)
#
# import pymysql
#
# conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="jing1995",  charset='utf8', database="daili",)
# cs1 = conn.cursor()
#
# connt = cs1.execute("select ip from daili_pool")
# res = cs1.fetchall()
# print(res)


