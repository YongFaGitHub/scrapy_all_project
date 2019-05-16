# import csv
# from pymysql import *
#
# conn = connect(
#     host="127.0.0.1",
#     database="baidubaiku",
#     user="root",
#     password="jing1995",
#     port=3306,
#     charset='utf8'
# )
# cs1 = conn.cursor()
#
#
#
# file = open("./name1.csv", "rt", encoding="utf-8")
# list_1 = []
# read = csv.reader(file)
# # with open("./name1.csv", "a+", encoding="utf-8") as f:
#
# for line in read:
#     if line[1] not in list_1:
#         list_1.append(line[1])
#
# #     if len(line[2]) > 0:
# #
# #         f.write(line[1] + "," + line[2] + "\n")
# #     else:
# #         f.write(line[1] + "," + "暂不存储" + "\n")
# print(list_1)
# print(len(list_1))
# for lis_one in list_1:
#     sql = "alter table baidu_zhenghou add {} text".format(lis_one)
#
#     cs1.execute(sql)
#
# conn.commit()
# conn.close()
a = ['病因病机', '证候特征', '临床表现', '治法', '常用方剂', '常用中药', '常见病证',
     '预防调护', '常见证型', '转归预后', '概述', '证候关系', '治法方药', '常用腧穴',
     '病因', '治疗', '鉴别诊断', '检查', '其他疗法', '常用方药', '饮食调护', '历代论述',
     '注意事项', '家庭治疗措施', '病理机制', '常见证候']

# b = str(a).replace("[", "").replace("]", "").replace("'", "")
for b in a:
    print("item['" + b + "']" + ",")


