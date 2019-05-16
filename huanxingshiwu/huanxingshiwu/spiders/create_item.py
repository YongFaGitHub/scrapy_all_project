# from pymysql import *
#
# a = {'kcal': 71,
# 	'protein': 1.88,
# 	'fat': 0.86,
# 	'carbo': 15.9,
# 	'fibre': 6.5,
# 	'mufas': 0.154,
# 	'pufas': 0.171,
# 	'pufas_percent': 40,
# 	'tfa': 'null',
# 	'tfa_percent': 'null',
# 	'cholesterol': 'null',
# 	'phytosterol': 'null',
# 	'carotene': 155,
# 	'l_z_c': 322,
# 	'lycopene': 'null',
# 	'ca': 62,
# 	'mg': 20,
# 	'na': 10,
# 	'k': 186,
# 	'p': 19,
# 	's': 0.003959,
# 	'cl': 15.42,
# 	'fe': 0.86,
# 	'i': 'null',
# 	'zu': 0.17,
# 	'se': 'null',
# 	'cu': 0.095,
# 	'mn': 0.135,
# 	'f': 'null',
# 	'va': 87,
# 	'vc': 43.9,
# 	'vd': 'null',
# 	've': 0.15,
# 	'vk': 'null',
# 	'vp': 79.3,
# 	'b1': 0.037,
# 	'b2': 0.09,
# 	'b3': 0.429,
# 	'b4': 8.4,
# 	'b5': 0.208,
# 	'b6': 0.036,
# 	'b7': 'null',
# 	'b9': 17,
# 	'b12': 'null',
# 	'b14': 'null',
# 	'leu': 'null',
# 	'met': 'null',
# 	'thr': 'null',
# 	'lys': 'null',
# 	'trp': 'null',
# 	'val': 'null',
# 	'his': 'null',
# 	'ile': 'null',
# 	'phe': 'null'}

#
# conn = connect(host='127.0.0.1',
#                port=3306,
#                database='huanxingshiwu',
#                user='root',
#                password='jing1995',
#                charset='utf8')
# cs1 = conn.cursor()

# for key in a.keys():
#     print("item['{}'],item['{}']".format(key,key+"_fen")+",")
#




#     sql = 'alter table shiwuyuansu add {} float(10);'.format(key)
#     sql2 = 'alter table shiwuyuansu add {} float(10);'.format(key+"_fen")
#     print(key)
#
#     coone = cs1.execute(sql)
#     coone2 = cs1.execute(sql2)
#
# conn.commit()
# cs1.close()
# conn.close()
