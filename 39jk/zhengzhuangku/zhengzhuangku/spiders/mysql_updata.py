import pymysql
import csv

conn = pymysql.connect(
    host="127.0.0.1",
    database="39jk",
    user="root",
    password="jing1995",
    port=3306,
    charset='utf8'
)
cs1 = conn.cursor()
file = open("./title.txt","rt",encoding="utf-8")
read = csv.reader(file)

for line in read:
    try:
    # print(line[0])
        b = (line[0]).split("、")

        cs1.execute(
            'update 39jkzhengzhuangku set img_url="{}" where 名称="{}"'.format(b[1],b[0]))
        conn.commit()
        print(b[0])
    except:pass

cs1.close()
conn.close()
