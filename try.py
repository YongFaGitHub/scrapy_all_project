# -*- coding: utf-8 -*-
# import csv
# import sys
#
# # file = open("./all.txt","rt",encoding="UTF-8")
# #
# # read =   csv.reader(file)
# #
# # for line in read:
# #     print(line)
# #
#
# # print(sys.path)
#
#
# #
# # for n in filer(lambda n:n%5,[n for n in range(100) if n%5 ==0]):
# #     print(n)
# #     print("12345")
#
# # a = 1
# # b = 256
# # c = 258
# #
# # a = a is b
# # b = b is c
# # b = -1
# # c = c is b
# # print(a,b,c)
# #
# # a = zip("a","b","c"),(1,2,3,4)
# # print(a)
# # print(dict(a))
#
#
# import requests
#
# # formdata = {"account: 13022434516","password: iNdP4M+8dOZxq2hfWEqxihce/cfu/mfwQEnVNYBClVAUZ9IgpGO30qNfMMnjj71x5DoGdc3s71MwJF8voUfGhWtXzupYNctu3WvlzHYEziETUSEdIcDvwP+0rNDANBAVFWERD+Itsw7LG7vb9aVV9UDXZDuKHxYWAF8O2kdG09I="}
# # YmqIiPJOjLEXfMwjvmVM3983n2+wUlvFOemV1IVjcRfVlZz9r8kBnnq08FtkIgtYQ77cvojkTCx84k6z1UfukxwKAGhBdz8GjAKdxDLTgv4f4hs1doOGiYl/qjQGI1S5VqDlGF9lqv1NwU1FvayW7JQRMs1xNt6i6sF3jKpL5ek=
# # iNdP4M+8dOZxq2hfWEqxihce/cfu/mfwQEnVNYBClVAUZ9IgpGO30qNfMMnjj71x5DoGdc3s71MwJF8voUfGhWtXzupYNctu3WvlzHYEziETUSEdIcDvwP+0rNDANBAVFWERD+Itsw7LG7vb9aVV9UDXZDuKHxYWAF8O2kdG09I=
# # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
# # url = "https://www.ximalaya.com/passport/v3/security/popupLogin"
# # r = requests.post(url=url,headers = headers,data=formdata)
# # print(r.content.decode())
#
# #
# #
# # mail:18513606786
# # icode:
# # origURL:http://www.renren.com/home
# # domain:renren.com
# # key_id:1
# # captcha_type:web_login
# # password:0c5f0e108f637a6ba0b25727797973b29464c510b891b67f2159ae1ccbf89b98
# # rkey:630b54f9b76184834971d1b2f2e633c8
# # f:http%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DJHiQ5D1PsUSA8SyTpLXtkd8g64_z3R75ikIeAAfeY8u%26wd%3D%26eqid%3D9a69fc8c0000be00000000025b48128a
#
# formdata = {"email":"18513606786","password":"jing1995",
#             }
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"}
#
# url = "http://www.renren.com/PLogin.do"
# r = requests.post(url = url,data=formdata,headers=headers)
# # b = requests.get("http://zhibo.renren.com/top")
# # 新用户06786
#
# print(r.content.decode())

#
# import re
#
# a = "dfsggfsg"
# # b = re.findall(r"gs",a)
# # print(b)
# b = re.sub(r"gs","",a)
# print(b)

# import re
# a = "sdfsgfwerf"
#
# b = re.findall(r"(.*[\┘\┐])", a, re.S)
#
# c = re.sub()

# import random
# print(random.uniform(0, 5))
# lsi = ['督脉之气在此吸湿化风。', '', '']
# a = ""
# b = a.join(lsi)
# print(b)

# from pypinyin import *
# a = "我是"
# print(pinyin(a))
# print(round(2.112142, 4))




# 测试图谱可视化
# from django.http import JsonResponse
# from owlready2 import *
# import json
# # from owl_query_two.settings import STATICFILES_DIRS
# from django.http import HttpResponse
# import Levenshtein
# from functools import partial
# import time
#
# onto = get_ontology("F:\Django_project\知识图谱可视化\owl_query_2.0\static\enn20190131.owl").load()  # 本体 需要修改加载路径
# obo = onto.get_namespace("http://enn.cn/onto")
#
# jiazai = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX owl: <http://www.w3.org/2002/07/owl#>
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# PREFIX enn: <http://enn.cn/onto#>
# """
# graph = default_world.as_rdflib_graph()
#
# # 初始化部分数据，从文件中加载
# ObjectProperty_list = list(onto.object_properties())  # 获得所有的object的关系
# DataProperty_list = list(onto.data_properties())  # 获得所有的dataproperties的关系
# list_classes_raw = list(onto.classes())
# list_classes_raw.remove(onto.Classify)  # 获得实体的类名列表 并且已经去除classify
# list_class_comment = list(map(lambda x: x.comment[0], list_classes_raw))  # 获得类的备注名称
#
# # 判断是不是大类别的列表
# is_big_class_list = [onto.Disease, onto.Food, onto.Cookbook]
#
#
# @profile
# def query():
#
#     # if request.method == "POST":
#         # 接收表单
#         # name = request.POST.get('name')
#         # 接收json
#         # data = json.loads(request.body)
#         # print(data, "@@"*100)
#         # name_raw = data["name"]
#         # name = name_raw.title()
#         name = "丝瓜"
#         data_list = []
#
#         code = HttpResponse.status_code
#         head = getattr(onto, name)
#         b_p_id = False
#         ann_pro = ""
#         if head is not None:  # 如果不是空值，则有可能是英文类名、实体名称
#             if head in list_classes_raw:  # 如果传过来的是类名
#                 type_property = "objectproperty"
#                 name_all_list = list(map(lambda x: x.name, head.instances()))
#                 for name_one_class in name_all_list:
#                     comment_class_name = {"type_pro": type_property, "source": name, "target": name_one_class,
#                                           'rela_en': "", "rela_zh": "", "p_b_id": False}
#                     data_list.append(comment_class_name)
#
#             else:  # 如果是实体名称
#                 s1 = time.time()
#                 for rel in head.get_properties():  # head,rel,tail  遍历每一个关系
#                     if rel == onto.pinyin:
#                         b_p_id = True
#                     else:
#                         b_p_id = False
#
#                     if rel in ObjectProperty_list:  # 判断关系是否是object ann_pro 为注释含量
#                         comment = (list(getattr(rel, "comment")))[0]  # 关系的第一个注释
#                         type_property = "objectproperty"
#                         if rel == onto.contain_elements:
#                             type_property = "ann_property"
#                             elements_list = """select  ?y ?s (concat(str(?num),?n) as ?val) where
#                             {{enn:{0} enn:contain_elements ?y.
#                             ?temp owl:annotatedSource enn:{0};
#                             owl:annotatedTarget ?y;
#                             enn:nuit ?n;
#                             enn:numerical ?num;
#                             enn:score ?s}}
#                             """.format(head.name)
#                             for x, y, z in graph.query(jiazai + elements_list):
#                                 pass
#                                 # objectpro_dict_one = {"type_pro": type_property, "source": head.name,
#                                 #                       "target": x.split("#")[-1],
#                                 #                       'rela_en': rel.name, "rela_zh": comment, "ann_pro": z,
#                                 #                       "b_p_id": b_p_id}
#                                 # data_list.append(objectpro_dict_one)
#                         else:
#                             tail_list = list(getattr(head, rel.name))
#                             for tail in tail_list:  # rel.name 得到的是关系名称
#                                 tail_name = getattr(tail, "name")  # 得到object关系指向的name
#
#                                 objectpro_dict_one = {"type_pro": type_property, "source": head.name, "target": tail_name,
#                                                       'rela_en': rel.name, "rela_zh": comment, "ann_pro": "",
#                                                       "b_p_id": b_p_id}
#                                 data_list.append(objectpro_dict_one)
#
#                     if rel in DataProperty_list:  # 如果是datapro类型的数据 则:
#                         type_object = "dataproperty"
#                         for tail2 in getattr(head, rel.name):  # rel.name 得到的是关系名称
#
#                             comment = (list(getattr(rel, "comment")))[0]
#                             tail_name = tail2
#                             datapro_dict_one = {"is_object": type_object, "source": head.name, "target": tail_name,
#                                                 'rela_en': rel.name, "rela_zh": comment, "b_p_id" : b_p_id}
#                             data_list.append(datapro_dict_one)
#                 s2 = time.time()
#                 print(s2 - s1)
#         else:  # 如果是空的
#             # 判断是不是输入的类的中文注释名称
#             if name in list_class_comment:
#                 for i in onto.classes():
#                     if i.comment[0] == name:
#                         type_property = "objectproperty"
#                         name_all_list = list(map(lambda x: x.name, i.instances()))
#                         for name_one_class in name_all_list:
#                             comment_class_name = {"type_pro": type_property, "source": name, "target": name_one_class,
#                                                   'rela_en': "instances", "rela_zh": "", "b_p_id": b_p_id,
#                                                   "ann_pro": ann_pro}
#                             data_list.append(comment_class_name)
#             else:
#                 # response_data = {"code": code, "version": 1.0, "status": "success", "data": "查询无内容"}
#                 data_list = "查询无内容"
#
#         response_data = {"code": code, "version": 2.0, "data": data_list}
#
#         # return JsonResponse(response_data)
#
# if __name__ == '__main__':
#     query()





#
#
# # 测试菜品识别
#
# from django.http import JsonResponse
# from owlready2 import *
# import json
# # from owl_query_two.settings import STATICFILES_DIRS
# from django.http import HttpResponse
# import Levenshtein
# from functools import partial
# import time
# import requests
# import base64
#
# onto = get_ontology("F:\Django_project\知识图谱可视化\owl_query_2.0\static\enn20190131.owl").load()  # 本体 需要修改加载路径
# obo = onto.get_namespace("http://enn.cn/onto")
#
# jiazai = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX owl: <http://www.w3.org/2002/07/owl#>
# PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# PREFIX enn: <http://enn.cn/onto#>
# """
# graph = default_world.as_rdflib_graph()
# # 先初始化一个菜谱的列表  , 用于计算最近的逻辑距离
# Cookbook_list = []
# for a in list(onto.Cookbook.instances()):
#     Cookbook_list.append(a.name)
#
# Food_obj_list = list(onto.Food.instances())  # 食材个体
# Cookbook_obj_list = list(onto.Cookbook.instances())  # 菜谱个体
#
# # 获得jaro距离的函数
# def pro_match_func(sent1):
#     return partial(lambda s1, s2: round(Levenshtein.jaro(s1, s2), 2), s2=sent1)
#
#
# # 将用户图片传给百度接口，返回一个相似列表 len=5
# def input_img(img):
#     # 获取acc_t
#     r = requests.get("https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=pGnjqSH88cUKLLZnG8vPISW5&client_secret=bhQYCjG4W6VFjGycCAfWWmAWykeMYLkx")
#
#     scc_t = eval(r.text)
#     access_token = scc_t["access_token"]
#
#     # 构建携带图片数据的请求
#     params = {"image": img, "top_num": 5}
#     # header = {'Content-Type': 'application/x-www-form-urlencoded'}
#
#     request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish?access_token=" + access_token
#     response = requests.post(url=request_url, data=params, )
#     response_dict = eval(response.text.replace("true", '\"true\"'))
#     # print("##########")
#     # print(response_dict)
#
#     return response_dict
#
# @profile
# def caipin(img):
#     # if request.method == "POST":
#     #     code = request.POST.get("img").encode()
#         response_dict = input_img(img)
#         ##########################################################
#         # code_yi = request.FILES.get("fafafa").chunks()  # 获取图片的内容
#         # 测试页面上传图片 获得二进制码的规则
#         # for code_two in code_yi:  # 生成图片内容
#         #     code = base64.b64encode(code_two)  # 对图片进行编码
#         #     response_dict = input_img(code)  # 调用百度接口，将图片数据传入，接收返回的最大的
#         ##########################################################
#         try:  # 判断百度是否返回
#             respon_raw = response_dict["result"][0]
#             baidu_name = respon_raw["name"]
#
#             # 初始化数据
#             is_owl_rela = 0
#             name_material = ""  # 初始化相似度的名字
#
#             data_list = []
#
#             material_raw = (getattr(onto, baidu_name))
#             # print(material_raw)  #存在
#             if material_raw is None:  # 如果百度接口返回的菜名在知识图谱中没有
#                 # 加入相似度判断,与现有的知识图谱相匹配
#                 pro_match_func_one = pro_match_func(baidu_name)
#                 pro_match_func_list = list(map(pro_match_func_one, Cookbook_list))
#                 if max(pro_match_func_list) > 0.7:
#                     name_material = Cookbook_list[pro_match_func_list.index(max(pro_match_func_list))]  # 最大匹配名字
#
#                     material_raw = getattr(onto, name_material)
#
#             # 在加入相似度匹配之后 判断是否存在，如果存在则进行获取食材，如果还没有则直接返回百度返回的数据
#             # print(material_raw)
#             if material_raw is not None:
#                 name_caipin = material_raw.name
#                 is_owl_rela = 1
#                 # 菜品名称在知识图谱中之后的操作
#                 if material_raw in Food_obj_list:  # 如果是食材
#                     elements_list_shi = """select  ?y ?s (concat(str(?num),?n) as ?val) where
#                                                 {{enn:{0} enn:contain_elements ?y.
#                                                 ?temp owl:annotatedSource enn:{0};
#                                                 owl:annotatedTarget ?y;
#                                                 enn:nuit ?n;
#                                                 enn:numerical ?num;
#                                                 enn:score ?s}}
#                                                 """.format(name_caipin)
#                     r1 = graph.query(jiazai + elements_list_shi)
#                     for x, y, z in r1:
#                         data_dict = {"element": x.split("#")[-1],
#                                      "number": z}
#
#                         data_list.append(data_dict)
#
#                 if material_raw in Cookbook_obj_list:  # 如果是菜谱
#
#                     contain_elements = """
#                     select ?yuansu (concat(str((sum(?numerical))/(sample(?count))),(sample(?nuit))) as ?e) where{{
#                     {{select (count(*) as ?count) where {{enn:{0} enn:material ?food1.}}}}
#                     enn:{0} enn:material ?food.
#                     ?temp owl:annotatedSource ?food ;
#                           owl:annotatedTarget ?yuansu ;
#                           enn:nuit ?nuit;
#                           enn:numerical ?numerical;
#                           filter(!regex(str(?yuansu),"能量"))
#                           }}group by ?yuansu
#                             """.format(name_caipin)
#                     r = graph.query(jiazai + contain_elements)
#                     for x,y in r:
#                         data_dict = {"element":x.split("#")[-1],
#                                      "number": y}
#
#                         data_list.append(data_dict)
#
#             else: respon_raw["data"] = "暂无数据"
#
#             respon_raw["data"] = data_list
#             response = {
#                 "code": HttpResponse.status_code,
#                 "version": 1.0,
#                 "result": respon_raw
#             }
#
#             # 返回之前存入数据库,包括图片的二进制存入数据库
#
#         except:
#             response = {
#                 "code": HttpResponse.status_code,
#                 "version": 1.0,
#                 "result": "无法识别"
#             }
# if __name__ == '__main__':
#     f = open('F:/pycharmproject/caipu_api/bbb.jpg', 'rb')
#     img = base64.b64encode(f.read())
#     caipin(img)
#
# import datetime
# date1=datetime.datetime.strptime("2019-02-14",  '%Y-%m-%d')
# date2=datetime.datetime.strptime("2019-02-17", '%Y-%m-%d')
# print((date2 - date1).days)

# a = set(["a", "b"])
# b = set(["cdd", "d"])
# a.update(b)
# c = a
# print(c)
# print(a)
# print(b)




c = [{
		'type_pro': 'dataproperty',
		'source': '黄瓜',
		'target': '1、不宜生食不洁黄瓜;<br/>2、不宜加碱或高热煮后食用;<br/>3、不宜弃汁制馅食用;<br/>4、不宜多食偏食;<br/>5、不宜和辣椒、菠菜同食;<br/>6、不宜与花菜、小白菜、西红柿、柑桔同食。',
		'rela_en': 'food_taboos',
		'rela_zh': '食物禁忌',
		'is_show': True,
		'ann_pro': '',
		'level': 1
	}, {
		'type_pro': 'dataproperty',
		'source': '黄瓜',
		'target': '黄瓜葫芦科一年生蔓生或攀援草本植物。茎、枝伸长，有棱沟，被白色的糙硬毛。卷须细。叶柄稍粗糙，有糙硬毛；<br/>黄瓜为中国各地夏季主要菜蔬之一。茎藤药用，能消炎、祛痰、镇痉。',
		'rela_en': 'food_summarize',
		'rela_zh': '概述',
		'is_show': True,
		'ann_pro': '',
		'level': 1
	}, {
		'type_pro': 'dataproperty',
		'source': '黄瓜',
		'target': '黄瓜味甘，甜、性凉、苦、无毒，入脾、胃、大肠；具有除热，利水利尿，清热解毒的功效；主治烦渴，咽喉肿痛，火眼，火烫伤。还有减肥功效。',
		'rela_en': 'traditional',
		'rela_zh': '功效',
		'is_show': True,
		'ann_pro': '',
		'level': 1
	}, {
		'type_pro': 'dataproperty',
		'source': '黄瓜',
		'target': 'knowledge-pro/a69a12ea-c8e2-4f4c-afbf-ed1857607ff6.jpg?e=15580501397&token=2:H0SXGV9F964NB1956N60:311ce8f62276820c534659b16fa2308793af0c1fd74e842017f4cfff5ba20c2b',
		'rela_en': 'picture',
		'rela_zh': '图片',
		'is_show': True,
		'ann_pro': '',
		'level': 1
	}, {
		'type_pro': 'dataproperty',
		'source': '黄瓜',
		'target': '黄瓜富含蛋白质、糖类、维生素B2、维生素C、维生素E、胡萝卜素、尼克酸、钙、磷、铁等营养成分。<br/>黄瓜中的一种激素有利于胰腺分泌胰岛素，可辅助治疗糖尿病。黄瓜中的固醇类成分能降低胆固醇。黄瓜富含的膳食纤维、钾和镁有益调节血压水平，预防高血压。',
		'rela_en': 'nutrition',
		'rela_zh': '营养功效',
		'is_show': True,
		'ann_pro': '',
		'level': 1
	}, {
		'type_pro': 'dataproperty',
		'source': '黄瓜',
		'target': 'huanggua',
		'rela_en': 'pinyin',
		'rela_zh': '拼音',
		'is_show': False,
		'ann_pro': '',
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '蔬菜类',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '膀胱炎',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '湿热质',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '湿热内蕴证',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '血瘀质',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '上呼吸道感染',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '可疑失眠',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '痰湿质',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '泌尿道感染',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '高血压',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '气郁质',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '食积证',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '阴虚质',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '特禀质',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '肾功能不全',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '糖尿病性酮症酸中毒',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '气滞证',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '食积化热证',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '糖尿病性肾病',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '平和质',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '睡眠障碍',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '阴虚证',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '疲劳综合征',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '热证',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '失眠',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '心动过速',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '肥胖',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '糖尿病',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '健康人',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '无失眠',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '低热症',
		'rela_en': 'suitable_to',
		'rela_zh': '适宜人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '阳虚质',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '血瘀证',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '寒证',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '脾虚证',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '肾病综合征',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '阳虚证',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '气虚质',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '痰湿内蕴证',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '气虚证',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '肾炎',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '肾盂肾炎',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '肾病',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '心动过缓',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '肾气虚证',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '血虚证',
		'rela_en': 'unsuitable_to',
		'rela_zh': '禁忌人群',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '中餐',
		'rela_en': 'suitmeal',
		'rela_zh': '适宜食用时间段',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '晚餐',
		'rela_en': 'suitmeal',
		'rela_zh': '适宜食用时间段',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '早餐',
		'rela_en': 'suitmeal',
		'rela_zh': '适宜食用时间段',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '凉',
		'rela_en': 'food_property',
		'rela_zh': '食物性状',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '甘',
		'rela_en': 'food_taste',
		'rela_zh': '食物味道',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '夏至',
		'rela_en': 'eat_more',
		'rela_zh': '适宜多吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '白露',
		'rela_en': 'eat_more',
		'rela_zh': '适宜多吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '霜降',
		'rela_en': 'eat_more',
		'rela_zh': '适宜多吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '立夏',
		'rela_en': 'eat_more',
		'rela_zh': '适宜多吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '立秋',
		'rela_en': 'eat_more',
		'rela_zh': '适宜多吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '处暑',
		'rela_en': 'eat_more',
		'rela_zh': '适宜多吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '小满',
		'rela_en': 'eat_more',
		'rela_zh': '适宜多吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '寒露',
		'rela_en': 'eat_more',
		'rela_zh': '适宜多吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '小暑',
		'rela_en': 'eat_more',
		'rela_zh': '适宜多吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '大暑',
		'rela_en': 'eat_more',
		'rela_zh': '适宜多吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '芒种',
		'rela_en': 'eat_more',
		'rela_zh': '适宜多吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '秋分',
		'rela_en': 'eat_more',
		'rela_zh': '适宜多吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '小寒',
		'rela_en': 'eat_less',
		'rela_zh': '适宜少吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '大雪',
		'rela_en': 'eat_less',
		'rela_zh': '适宜少吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '立冬',
		'rela_en': 'eat_less',
		'rela_zh': '适宜少吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '冬至',
		'rela_en': 'eat_less',
		'rela_zh': '适宜少吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '小雪',
		'rela_en': 'eat_less',
		'rela_zh': '适宜少吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '大寒',
		'rela_en': 'eat_less',
		'rela_zh': '适宜少吃',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '肺经',
		'rela_en': 'channeltropism',
		'rela_zh': '归经',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '胃经',
		'rela_en': 'channeltropism',
		'rela_zh': '归经',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '大肠经',
		'rela_en': 'channeltropism',
		'rela_zh': '归经',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '清热解毒',
		'rela_en': 'food_health_efficacy',
		'rela_zh': '食材保健功效',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '抗衰老',
		'rela_en': 'food_health_efficacy',
		'rela_zh': '食材保健功效',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '利尿',
		'rela_en': 'food_health_efficacy',
		'rela_zh': '食材保健功效',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '术后',
		'rela_en': 'food_health_efficacy',
		'rela_zh': '食材保健功效',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '减肥',
		'rela_en': 'food_health_efficacy',
		'rela_zh': '食材保健功效',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '祛痘',
		'rela_en': 'food_health_efficacy',
		'rela_zh': '食材保健功效',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '晕车',
		'rela_en': 'food_health_efficacy',
		'rela_zh': '食材保健功效',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '瘦身',
		'rela_en': 'food_health_efficacy',
		'rela_zh': '食材保健功效',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '消暑解渴',
		'rela_en': 'food_health_efficacy',
		'rela_zh': '食材保健功效',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'objectproperty',
		'source': '黄瓜',
		'target': '美白',
		'rela_en': 'food_health_efficacy',
		'rela_zh': '食材保健功效',
		'ann_pro': '',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '多不饱和脂肪酸',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.032克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '多不饱和脂肪酸',
		'target': '0.032克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '植物固醇',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '14.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '植物固醇',
		'target': '14.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '胡萝卜素',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '56.0微克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '胡萝卜素',
		'target': '56.0微克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '叶黄素',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '49.0微克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '叶黄素',
		'target': '49.0微克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '钙',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '16.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '钙',
		'target': '16.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '镁',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '13.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '镁',
		'target': '13.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '钠',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '2.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '钠',
		'target': '2.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '钾',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '147.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '钾',
		'target': '147.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '磷',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '24.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '磷',
		'target': '24.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '硫',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '2.36089毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '硫',
		'target': '2.36089毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '氯',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '3.084毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '氯',
		'target': '3.084毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '铁',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.28毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '铁',
		'target': '0.28毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '锌',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.2毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '锌',
		'target': '0.2毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '硒',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.3微克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '硒',
		'target': '0.3微克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '铜',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.041毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '铜',
		'target': '0.041毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '锰',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.079毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '锰',
		'target': '0.079毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '氟',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '1.3微克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '氟',
		'target': '1.3微克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '维生素A',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '31.5微克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '维生素A',
		'target': '31.5微克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '维生素C',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '2.8毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '维生素C',
		'target': '2.8毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '维生素E',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.03毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '维生素E',
		'target': '0.03毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '维生素K',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '16.4微克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '维生素K',
		'target': '16.4微克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '维生素P',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.1毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '维生素P',
		'target': '0.1毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '维生素B1',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.027毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '维生素B1',
		'target': '0.027毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '维生素B2',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.033毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '维生素B2',
		'target': '0.033毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '维生素B3',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.098毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '维生素B3',
		'target': '0.098毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '维生素B4',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '6.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '维生素B4',
		'target': '6.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '能量',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '15.0千卡',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '能量',
		'target': '15.0千卡',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '蛋白质',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.65克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '蛋白质',
		'target': '0.65克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '脂肪',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.11克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '脂肪',
		'target': '0.11克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '碳水化合物',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '3.63克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '碳水化合物',
		'target': '3.63克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '粗纤维',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.5克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '粗纤维',
		'target': '0.5克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '单不饱和脂肪酸',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.005克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '单不饱和脂肪酸',
		'target': '0.005克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '维生素B5',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.259毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '维生素B5',
		'target': '0.259毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '维生素B6',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.04毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '维生素B6',
		'target': '0.04毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '维生素B9',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '7.0微克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '维生素B9',
		'target': '7.0微克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '维生素B14',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '0.1毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '维生素B14',
		'target': '0.1毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '亮氨酸',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '29.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '亮氨酸',
		'target': '29.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '蛋氨酸',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '6.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '蛋氨酸',
		'target': '6.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '苏氨酸',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '19.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '苏氨酸',
		'target': '19.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '赖氨酸',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '29.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '赖氨酸',
		'target': '29.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '色氨酸',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '5.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '色氨酸',
		'target': '5.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '缬氨酸',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '22.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '缬氨酸',
		'target': '22.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '组氨酸',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '10.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '组氨酸',
		'target': '10.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '异亮氨酸',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '21.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '异亮氨酸',
		'target': '21.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'ann_property',
		'source': '黄瓜',
		'target': '苯丙氨酸',
		'rela_en': 'contain_elements',
		'rela_zh': '元素关系网',
		'ann_pro': '19.0毫克',
		'is_show': True,
		'level': 1
	}, {
		'type_pro': 'ann_property',
		'source': '苯丙氨酸',
		'target': '19.0毫克',
		'rela_en': '',
		'rela_zh': '',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '膀胱炎',
		'target': 'N30.901',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '膀胱炎',
		'target': '膀胱炎是一种常见的尿路感染性疾病，约占尿路感染的60%以上，分为急性单纯性膀胱炎和反复发作性膀胱炎。其致病菌多数为大肠杆菌，约占75%以上，通常多发生于女性，因为女性的尿道比男性的尿道短，又接近肛门，大肠杆菌易侵入。膀胱炎主要的临床表现为尿频、尿急、尿痛、排尿不适、下腹部疼痛，终末血尿常见，部分患者出现迅速排尿困难。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '膀胱炎',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '湿热质',
		'target': 'TZBZSHIREZ',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '湿热质',
		'target': '以湿热内蕴为主要特征的体质状态。其中“湿”分为内湿和外湿，外湿指空气或环境潮湿；内湿是指体内的津液聚停。\n主要表现：面垢油光，易生痤疮，口苦口干，身重困倦，大便粘滞或燥结，小便短黄，舌质偏红，苔黄腻，形体中等或偏瘦。男子易阴囊潮湿，女子易带下增多，脉滑数。\n容易烦躁。\n性格特征：多急躁易怒。\n发病倾向:易患脂肪肝、糖尿病、高脂血症、痤疮、湿疹、泌尿系感染等疾病。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '湿热质',
		'target': '中医-体质',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '湿热内蕴证',
		'target': 'ZBMR20',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '湿热内蕴证',
		'target': 9.0,
		'rela_en': 'weight',
		'rela_zh': '权重',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '湿热内蕴证',
		'target': '中医病证名，指湿热蕴与体内。“湿”分为内湿和外湿，外湿指空气或环境潮湿；内湿是指体内的津液聚停。湿热证就如同人体内处于夏日的“桑拿天”的状态，又热、又湿、又粘。\n常表现脸上容易生粉刺，皮肤容易瘙痒，口苦、口臭或嘴里有异味，头重如裹，昏蒙眩晕，胸脘痞闷，胃纳不香，大便黏滞不爽，小便有发热感，小便浑浊，妇女带下稠浊，舌质偏红、苔黄腻等。\n常见人群：\n1、长期情绪压抑，或经常熬夜，或偏嗜生冷、油腻饮食，或长期吸烟、饮酒的人群；\n2、滋补过度，如吃很多银耳、燕窝、冬虫夏草；\n3、长期生活在湿热环境中，比如广东、海南；\n4、一部分消化系统慢性病，例如慢性肝炎、溃疡性结肠炎等。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '湿热内蕴证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '血瘀质',
		'target': 'TZBSXUEYUZ',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '血瘀质',
		'target': '女性多见痛经、闭经、或经色紫黑有块、崩漏，口唇黯淡或紫',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '血瘀质',
		'target': '脉象细涩或结代。\n性格特征：多内郁',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '血瘀质',
		'target': '以血瘀表现为主要特征的体质状态\n主要表现：平素面色晦黯',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '血瘀质',
		'target': '心情不快',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '上呼吸道感染',
		'target': 'J06.903',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '上呼吸道感染',
		'target': '上呼吸道感染简称上感，又称普通感冒。是包括鼻腔、咽或喉部急性炎症的总称。广义的上感不是一个疾病诊断，而是一组疾病，包括普通感冒、病毒性咽炎、喉炎、疱疹性咽峡炎、咽结膜热、细菌性咽-扁桃体炎。狭义的上感又称普通感冒，是最常见的急性呼吸道感染性疾病，多呈自限性，但发生率较高。成人每年发生2～4次，儿童发生率更高，每年6～8次。全年皆可发病，冬春季较多。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '上呼吸道感染',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '可疑失眠',
		'target': 'XYKYSM',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '可疑失眠',
		'target': '轻度的入睡困难或者早醒，睡眠时间欠充足和（或）睡眠质量不很满意。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '可疑失眠',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '痰湿质',
		'target': 'TZBSTANSHIZ',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '痰湿质',
		'target': '口黏腻或甜，喜食肥甘，大便正常或不实',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '痰湿质',
		'target': '以黏滞重浊为主要特征的体质状态。\n主要表现：体型肥胖，腹部肥满，口黏苔腻，面部皮肤油脂多，多汗且粘，胸闷，痰多，易困倦',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '痰湿质',
		'target': '脉滑。\n性格特征：多性格温和，稳重恭谦，善于忍耐。\n发病倾向:易患肥胖、糖尿病、代谢综合征、月经不调、带下病、不孕不育、眩晕、痤疮等疾病。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '痰湿质',
		'target': '小便不多或微混，舌体胖大',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '泌尿道感染',
		'target': 'N39.001',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '泌尿道感染',
		'target': '尿路感染又称泌尿系统感染，是尿路上皮对细菌侵入导致的炎症反应，通常伴随有菌尿和脓尿。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '泌尿道感染',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '高血压',
		'target': 'I10.X02',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '高血压',
		'target': '高血压（hypertension）是指以体循环动脉血压（收缩压和/或舒张压）增高为主要特征（收缩压≥140毫米汞柱，舒张压≥90毫米汞柱），可伴有心、脑、肾等器官的功能或器质性损害的临床综合征。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '高血压',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气郁质',
		'target': 'TZBSQIYUZ',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气郁质',
		'target': '敏感多疑为主要表现的体质状态。\n主要表现：平素神情抑郁，烦闷不乐，善太息，睡眠较差，舌淡红，苔薄白，脉弦。\n性格特征：多性格内向不稳定',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气郁质',
		'target': '由于长期情志不畅、气机郁滞而形成的以性格内向不稳定',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气郁质',
		'target': '敏感多疑。\n发病倾向：易患抑郁症、失眠等情志病，胃炎、十二指肠溃疡、胆囊炎等消化系统疾病，心律失常、冠心病、中风等心脑血管疾病，甲状腺机能紊乱，乳腺增生，肿瘤等。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气郁质',
		'target': '忧郁脆弱',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '食积证',
		'target': 'ZBY011',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '食积证',
		'target': 3.0,
		'rela_en': 'weight',
		'rela_zh': '权重',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '食积证',
		'target': '食积是指食物停积于胃肠，损害脾胃功能所引起的病症。多见于小儿，脾运失司所引起的一种小儿常见的脾胃病证。临床表现为不思饮食，腹胀嗳腐，大便酸臭或便秘等症状。\n常见人群：\n1、\t喂养不当的婴幼儿；\n2、饱食无度，生冷不节，或过食肥甘厚腻的成年人。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '食积证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阴虚质',
		'target': 'TZBSYINXUZ',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阴虚质',
		'target': '口燥咽干',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阴虚质',
		'target': '喜冷饮',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阴虚质',
		'target': '以阴虚内热等表现为主要特征的体质状态。\n主要表现：平素易手足心热',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阴虚质',
		'target': '盗汗，大便干燥',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '特禀质',
		'target': 'TZBSTEBINGZ',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '特禀质',
		'target': '或有先天生理缺陷。\n性格特征：因禀质特异情况而不同。\n发病倾向：易患感冒、过敏性鼻炎、哮喘、湿疹、荨麻疹等疾病，平素抵抗力弱，特别对季节和环境适应能力差，易引发宿疾；或遗传病如血友病等；胎传性疾病如胎痫等。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '特禀质',
		'target': '由于先天禀赋不足和禀赋遗传等因素造成的一种特殊体质。包括先天性、遗传性的生理缺陷与疾病',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '特禀质',
		'target': '过敏反应等。\n主要表现：易过敏者，常见哮喘、风团、咽痒、喷嚏等；或患某些遗传性疾病、胎传性疾病。形体无特殊',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '特禀质',
		'target': '或有畸形',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肾功能不全',
		'target': 'N19.X02',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肾功能不全',
		'target': '是由多种原因引起的，肾小球严重破坏，使身体在排泄代谢废物和调节水电解质、酸碱平衡等方面出现紊乱的临床综合症后群。分为急性肾功能不全和慢性肾功能不全。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '肾功能不全',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '糖尿病性酮症酸中毒',
		'target': 'E14.103',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '糖尿病性酮症酸中毒',
		'target': '糖尿病酮症酸中毒是糖尿病常见的急性并发症，易发生于Ⅰ型糖尿病或Ⅱ型糖尿病患者在胰岛素治疗突然中断或减量，以及遇有急性应激情况时（例如各种感染、急性心脑血管意外、手术、妊娠等），体内糖代谢紊乱加重，酮体产生过多，导致血中HCO3-浓度减少，失代偿时，则血液pH下降，引起酸中毒症。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '糖尿病性酮症酸中毒',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气滞证',
		'target': 'ZYV150',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气滞证',
		'target': '人体气机以通顺为贵，一有郁滞，轻则胀闷，重则疼痛，气滞即因病邪内阻、情志不舒等，引起的人体某一脏腑或部分气机阻滞，运行不畅的病理状态。\n常表现为面色苍暗或萎黄；胸闷不舒，时欲太息，胸肋胀痛或窜痛；胃脘部容易胀痛，泛吐酸水，呃逆嗳气；女性经前乳房胀痛、月经不调等。\n常见人群：\n1.更年期女性或产后妇女；\n2.过度要求完美，不仅对自己，而且也别人有很多要求的人群；\n3.工作压力大，经常熬夜的人群。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '气滞证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '食积化热证',
		'target': 'ZBY011/1',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '食积化热证',
		'target': 2.0,
		'rela_en': 'weight',
		'rela_zh': '权重',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '食积化热证',
		'target': '食积化热是指食物内停不化，郁积化热，损伤脾胃功能所引起的病症。多见于小儿，临床表现为不思饮食，腹胀嗳腐，大便酸臭或便秘，兼有口渴唇红、皮肤灼热、手足心热、小便黄少等症状。\n常见人群：\n1、\t喂养不当、多食膏粱厚味的婴幼儿；\n2、暴饮饱食、多食膏粱厚味、煎炸炙烤之物的成年人。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '食积化热证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '糖尿病性肾病',
		'target': 'E14.203+',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '糖尿病性肾病',
		'target': '糖尿病肾病是糖尿病微血管并发症之一。广义的糖尿病肾脏病变包括感染性病变和血管性病变。血管性病变分微血管和大血管病变，大血管病变包括肾动脉硬化（累及主干及分支）和肾小动脉硬化（累及入球和出球小动脉）。微血管病变是指肾小球硬化，分结节性、渗出性和弥漫性三种。我们通常说的糖尿病肾病是肾小球硬化。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '糖尿病性肾病',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '平和质',
		'target': 'TZBZPINGHEZ',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '平和质',
		'target': '舌色淡红',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '平和质',
		'target': '睡眠安和',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '平和质',
		'target': '精力充沛',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '平和质',
		'target': '苔薄白；脉和有神。\n性格特征：多随和开朗。\n发病倾向：平素患病较少，对自然环境和社会环境适应力很强。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '睡眠障碍',
		'target': 'G47.901',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '睡眠障碍',
		'target': '睡眠量不正常以及睡眠中出现异常行为的表现﹐也是睡眠和觉醒正常节律性交替紊乱的表现。可由多种因素引起，常与躯体疾病有关，包括睡眠失调和异态睡眠。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '睡眠障碍',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阴虚证',
		'target': 'ZYJ030',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阴虚证',
		'target': 7.0,
		'rela_en': 'weight',
		'rela_zh': '权重',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阴虚证',
		'target': '阴虚是指体内精、血、津液的不足，本处重点是指阴津不足。阴虚证可见于西医多种临床疾病，与心脑血管系统、内分泌代谢等疾病关系密切，还涉及神经系统、呼吸系统、消化系统等。\n主要表现为面部烘热，手心、足心、胸中发热，失眠，睡中汗出、醒后汗止，急躁易怒，口眼发干，舌红或淡红、少苔或无苔等。\n阴虚常见人群：\n1、常见于女性更年期综合征人群，也可见于男性；\n2、一部分糖尿病人群；\n3、脑力劳动者并经常熬夜的人群；\n4、内分泌失调或植物神经紊乱的人群。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '阴虚证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '疲劳综合征',
		'target': 'F48.001',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '疲劳综合征',
		'target': '又称雅痞症、慢性伯基特淋巴瘤病毒（EBV）、慢性类单核白血球增多症等等。是一种身体出现慢性疲劳征状的病症，具体定义是长期（连续6个月以上）原因不明的疲劳感觉或身体不适。其症状包括发烧、喉咙痛、淋巴结肿大、极度疲劳、失去食欲、复发性上呼吸道感染、小肠不适、黄疽、焦虑、抑郁、烦躁及情绪不稳、睡眠障碍、对光及热敏感、暂时失去记忆力、无法集中注意力、头痛、痉挛、肌肉与关节痛。这些症状与感冒及其他病毒感染相似，因此容易误判。通常医师会误诊为臆想病、抑郁症、或精神引起的身体疾病。尚无对付此病毒的药或疫苗，辨识此病并不容易，而且其症状变化很大。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '疲劳综合征',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '热证',
		'target': 'ZBR000',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '热证',
		'target': 10.0,
		'rela_en': 'weight',
		'rela_zh': '权重',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '热证',
		'target': '中医病证名，此处特指实热证。主要指人体感受温邪、暑气或寒邪化热，或体内阳热偏亢，导致机体机能活动亢进，而引起的热性证候。\n可表现为怕热，身热汗多，面红烦躁，口渴喜冷饮，头痛、咽喉肿痛，口舌生疮，牙龈肿痛，心率不齐或心动过速，女性月经先期，便秘或泄泻热臭，小便少、色黄等。\n常见人群：\n1.\t嗜食辛辣刺激性食物的人群；\n2.\t情志不畅（如长期情绪压抑或急躁易怒等），或经常熬夜，压力大的一类人群；\n3.\t体型瘦，或先天因素致体内阴液不足，或饮水不足的一类人群；\n4.\t居处环境闷热、干燥。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '热证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '失眠',
		'target': 'G47.001',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '失眠',
		'target': '是指无法入睡或无法保持睡眠状态，导致睡眠不足。是对睡眠时间和（或）质量不满足并影响日间社会功能的一种主观体验。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '失眠',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '心动过速',
		'target': 'I47.102',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '心动过速',
		'target': '在成年人当由窦房结所控制的心律其频率超过每分钟100次时称为窦性心动过速。这是最常见的一种心动过速，其发生常与交感神经兴奋及迷走神经张力降低有关。它不是一种原发性心律失常，可由多种原因引起。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '心动过速',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肥胖',
		'target': 'E66.902',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肥胖',
		'target': '肥胖症是一组常见的代谢症群。当人体进食热量多于消耗热量时，多余热量以脂肪形式储存于体内，其量超过正常生理需要量，且达一定值时遂演变为肥胖症。正常男性成人脂肪组织重量占体重的15%～18%，女性占20%～25%。随年龄增长，体脂所占比例相应增加。关于肥胖的评估方法，包括人体测量学、双能X线吸收法、超声、CT、红外线感应法等多种。如无明显病因者称单纯性肥胖症，有明确病因者称为继发性肥胖症。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '肥胖',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '糖尿病',
		'target': 'E14.901',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '糖尿病',
		'target': '糖尿病是一组以高血糖为特征的代谢性疾病。高血糖则是由于胰岛素分泌缺陷或其生物作用受损，或两者兼有引起。糖尿病长期存在的高血糖，导致各种组织，特别是眼、肾、心脏、血管、神经的慢性损害、功能障碍。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '糖尿病',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '健康人',
		'target': 'XYZYJKR',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '健康人',
		'target': '是指身体、精神和社会适应等方面都处于良好状态的人。传统健康包括两个方面的内容：一是主要脏器无疾病，身体形态发育良好，体形均匀，人体各系统具有良好的生理功能，有较强的身体活动能力和劳动能力；二是对疾病的抵抗能力较强，能够适应环境变化，各种生理刺激以及致病因素对身体的作用。世界卫生组织提出“健康不仅是躯体没有疾病，还要具备心理健康、社会适应良好和有道德”。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '健康人',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '无失眠',
		'target': 'XYWSM',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '无失眠',
		'target': '无入睡困难，睡眠时间充足（成年人每天8小时左右），白天精力良好、无白天思睡。是对睡眠时间和（或）质量满足的一种主观体验。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '无失眠',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '低热症',
		'target': 'R50.951',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '低热症',
		'target': '低热是一种常见的症状，一般我们讲的低热是指体温超过正常，但在38℃以下者。引起低热的原因较多，要依据临床表现，查清病因，审因论治。特别是对功能性低热，要在排除器质性疾病的基础上作出诊断。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '低热症',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阳虚质',
		'target': 'TZBSYANGXUZ',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阳虚质',
		'target': '脉象沉迟。\n性格特征:多沉静、内向。\n发病倾向:易患肥胖、腹泻、骨质疏松、类风湿、关节炎、水肿、甲状腺功能低下、冠心病、哮喘、不孕不育等疾病',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阳虚质',
		'target': '苔润',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阳虚质',
		'target': '喜热饮食',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阳虚质',
		'target': '肌肉松弛不实，舌淡胖嫩边有齿痕',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '血瘀证',
		'target': 'ZYX120',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '血瘀证',
		'target': 6.0,
		'rela_en': 'weight',
		'rela_zh': '权重',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '血瘀证',
		'target': '血循行脉中，营养及滋润全身。血瘀是体内血液运行不畅的一种状态，包括微循环不畅、血液粘稠、或血管堵塞等病理状态，是多个身体指标的集体表现。\n血瘀的一般表现可概括为痛、麻、紫、淤、冷、肿、硬、乏等表现形式。具体表现为体内出现瘀滞则相应部位出现淤青（紫），面色晦暗，色素沉着，或有瘀斑；口唇暗淡或紫；舌质暗、有瘀点或片状瘀斑、舌下静脉曲张；女性多痛经、闭经、延期、经量少、崩漏，或经血暗黑，有血块等。\n血瘀常见人群：\n1、患有心脑血管疾病的人群；\n2、患有慢性疾病未及时纠正，3个月以上可以考虑；\n3、气虚，体内血液运行缓慢导致血瘀的一类人群；\n4、偏嗜生冷饮食、或久居寒湿之地，阳虚寒凉导致血瘀的一类人群；\n5、阴虚、湿热而热伤阴液，导致血瘀的一类人群；\n6、偏嗜肥甘厚味，内生痰湿导致血瘀的一类人群；\n7、不爱运动，或者生闷气抑郁寡欢导致气滞血瘀的一类人群。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '血瘀证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '寒证',
		'target': 'ZBH000',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '寒证',
		'target': 14.0,
		'rela_en': 'weight',
		'rela_zh': '权重',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '寒证',
		'target': '指感受寒邪，或体内寒气偏盛，导致身体内部阴气过剩，对营养物质消化和吸收功能减弱，以至身体对热量吸收减少所表现出的一类证候。\n寒证可分为外寒和内寒；外寒是导致人体发病的寒邪，伤于肌表为“伤寒”，直中脏腑为“中寒”，也可与他邪合并致病为风寒、寒湿等；内寒是脏腑阳气不足，主要是肾阳不足所致。\n常表现为怕冷，喜暖，手足不温，怕吹风，常觉得精神虚弱且容易疲劳，口淡不渴，小便颜色淡而量多，常腹泻，女性月经常迟来，血块多等。\n常见人群：\n1.\t嗜食生冷饮食、着装不适的人群；\n2.\t久坐、缺乏锻炼的人群；\n3.\t久居寒冷、潮湿环境的人群。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '寒证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '脾虚证',
		'target': 'ZZP010',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '脾虚证',
		'target': 5.0,
		'rela_en': 'weight',
		'rela_zh': '权重',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '脾虚证',
		'target': '泛指因脾气虚损引起的一系列中医“脾”脏生理功能失常的病理现象及病证。中医理论认为脾的功能是将胃中的饮食物转化为气、血、津、液，被称为“后天之本”，“气血生化之源”，现代医学研究表明其生理功能与物质能量代谢之间密切相连。\n常表现为食欲不振，食后困倦，胸腹部胀痛、痞满，口淡不渴，面白少华，倦怠乏力，便溏或便秘，舌淡，苔薄白等。\n常见人群：\n1、\t长期思虑（包括思考、思虑、忧思、相思）过度，或经常熬夜的人群；\n2、\t偏嗜生冷、油腻饮食的人群；\n3、\t缺乏锻炼、久坐的人群。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '脾虚证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肾病综合征',
		'target': 'N04.903',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肾病综合征',
		'target': '可由多种病因引起，以肾小球基膜通透性增加，表现为大量蛋白尿、低蛋白血症、高度水肿、高脂血症的一组临床症候群。分为原发性、继发性和遗传性三大类，原发性肾病综合征属于原发性肾小球疾病，有多种病理类型构成。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '肾病综合征',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阳虚证',
		'target': 'ZYA090',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阳虚证',
		'target': 11.0,
		'rela_en': 'weight',
		'rela_zh': '权重',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '阳虚证',
		'target': '阳虚是指体内阳气不足。阳气好比自然界中的太阳，给人以动力和温暖功能的能量，是人体物质代谢和生理功能的原动力和能量，亦是人体生殖、生长、发育、衰老和死亡的决定因素。\n阳虚人群主要表现为易疲劳，怕冷，遇冷容易出现腹泻、关节酸痛、胸闷，心律变慢，女性白带量多、清稀，伴腰部寒冷酸楚，男性可见阳痿早泄，面色苍白等。\n阳虚常见人群：\n1.\t慢性疾病未及时或妥善治疗的人群；\n2.\t偏嗜生冷饮食（如冰镇啤酒、冷饮、凉菜等）的人群；\n3.\t长期缺乏运动的人群。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '阳虚证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气虚质',
		'target': 'TZBSQIXUZ',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气虚质',
		'target': '一身之气不足',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气虚质',
		'target': '以气息低弱、脏腑功能状态低下为主要特征的体质状态。\n主要表现:平素气短懒言',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气虚质',
		'target': '或病后抗病能力弱',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气虚质',
		'target': '易迁延不愈，易患感冒、内脏下垂、过敏性鼻炎、哮喘、心率失常、冠心病、虚劳等病。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '痰湿内蕴证',
		'target': 'ZYTM30',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '痰湿内蕴证',
		'target': 13.0,
		'rela_en': 'weight',
		'rela_zh': '权重',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '痰湿内蕴证',
		'target': '痰湿是一种不健康状态，这里的“痰”并非只指一般概念中的口中咳出之痰，而是指人体津液的异常积留，是病理性的产物；“湿”分为内湿和外湿，外湿指空气或环境潮湿；内湿是指体内的津液聚停。现代医学认为其与体内代谢紊乱疾病相关，还与免疫系统、内分泌系统等全身多系统存在相关性。\n常表现为体形肥胖，腹部肥满松软，胸闷，痰多，身重不爽或麻木，口中常感甜、粘，面色淡黄而暗，眼胞微浮，容易困倦，平素舌体胖大，舌苔白腻等。\n常见人群：\n1.\t久食生冷、肥甘厚腻饮食的人群；\n2.\t长期暴饮暴食的人群；\n3.\t久坐、缺乏锻炼的人群；\n4.\t一部分具有高血压、高脂血症、糖尿病、肥胖症等代谢性疾病的人群；\n5.\t一部分患有心脑血管疾病的人群；\n6.\t一部分患有生殖功能障碍疾病的人群。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '痰湿内蕴证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气虚证',
		'target': 'ZYV090',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气虚证',
		'target': 12.0,
		'rela_en': 'weight',
		'rela_zh': '权重',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '气虚证',
		'target': '气虚是指由于一身之气不足，以气息低弱、脏腑功能状态低下为主要特征的病理状态。在中医中，气被认为是构成和维持人体生命活动的最基本物质，是不断运动的具有很强活力的极精微物质，为人体各脏腑器官的功能活动提供能量。人出生后，气主要来自于饮食物和呼吸的清气。\n常表现为语声低，气短懒言，精神不振，乏力，易出汗，经常头晕、健忘，冬天怕冷，酷夏怕热等。\n常见人群：\n1.\t一部分脾胃功能虚弱，营养不良的人群；\n2.\t因挑食、过度减肥等导致饮食失当的人群；\n3.\t过度劳累、过度安逸，或年老气衰的人群。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '气虚证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肾炎',
		'target': 'N05.902',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肾炎',
		'target': '肾炎是由免疫介导的、炎症介质（如补体、细胞因子、活性氧等）参与的，最后导致肾固有组织发生炎性改变，引起不同程度肾功能减退的一组肾脏疾病，可由多种病因引起。在慢性过程中也有非免疫、非炎症机制参与。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '肾炎',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肾盂肾炎',
		'target': 'N12.X03',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肾盂肾炎',
		'target': '是由致病微生物引起的肾盂和肾实质炎症，常伴有下尿路感染。大多为革兰阴性杆菌感染所致，分为急性和慢性两种类型。急性肾盂肾炎表现为与感染相关的急性间质炎症和肾小管坏死，患者有发热、尿频、尿急、尿痛及菌尿等症状，若无复杂因素存在，通过使用有效的抗菌药物，可迅速治愈。慢性肾盂肾炎多发生于尿路解剖或功能异常的基础之上，除了细菌性尿感外，还有肾盂肾盏瘢痕形成，肾脏外形不光滑或两肾大小不等，起病较为隐匿，容易反复发作，可导致慢性肾功能不全。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '肾盂肾炎',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肾病',
		'target': 'N28.901',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肾病',
		'target': '肾脏病的种类繁多，较常见的有免疫伤害引起的肾小球肾炎及细菌感染有关的肾盂肾炎等，另外糖尿病、高血压及全身性红斑性狼疮等病人也常并发肾脏病变。慢性肾脏病是各种原因引起的慢性肾脏结构和功能障碍（肾脏损害病史大于3个月），包括肾GFR正常和不正常的病理损伤、血液或尿液成分异常，及影像学检查异常，或不明原因GFR下降（<60ml/min·1.73m2）超过3个月。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '肾病',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '心动过缓',
		'target': 'R00.101',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '心动过缓',
		'target': '窦性心律慢于每分钟60次称为窦性心动过缓。可见于健康的成人，尤其是运动员、老年人和睡眠时。其他原因为颅内压增高、血钾过高、甲状腺机能减退、低温以及用洋地黄、β受体阻滞剂、利血平、胍乙啶、甲基多巴等药物。在器质性心脏病中，窦性心动过缓可见。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '心动过缓',
		'target': '西医疾病',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肾气虚证',
		'target': 'ZZS030',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肾气虚证',
		'target': 4.0,
		'rela_en': 'weight',
		'rela_zh': '权重',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '肾气虚证',
		'target': '肾气虚是指肾气亏虚，生长生殖功能下降，摄纳无权的病理状态。中医学的肾，不是解剖意义上的肾脏器官，它与人体的生长发育、生殖、消化、呼吸、水液代谢等功能相关，还与脑、骨、齿、腰、耳、头发、前后二阴（负责人体的排尿、生殖和排便的功能）相关，包含了人体的神经系统、运动系统、内分泌系统、免疫系统、生殖系统和泌尿系统，出现肾虚后，必然会影响到身体这几大主要系统的功能。\n常表现为骨骼与关节疼痛、腰膝酸软、不耐疲劳、尿频、脱发、耳鸣、视力及听力减退、失眠健忘，男子阳萎、遗精、早泄等，女子子宫发育不良、卵巢早衰闭经、月经不调、不孕等。\n常见人群：\n1、经常情绪无常、情志失调（如多愁善感、抑郁）的一类人群；\n2、房劳过度的一类人群；\n3、久病不愈而伤肾的一类人群；\n4、部分年老体衰的人群。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '肾气虚证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '血虚证',
		'target': 'ZYX030',
		'rela_en': 'code',
		'rela_zh': '疾病代码',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '血虚证',
		'target': 8.0,
		'rela_en': 'weight',
		'rela_zh': '权重',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'dataproperty',
		'source': '血虚证',
		'target': '血虚是血液失常的一种表现，是指血液生成不足或血的濡养功能减退的一种病理状态。\n常表现为经常疲劳，运动之后心慌、气短，头痛、头晕、目眩、耳鸣，注意力不集中，失眠多梦，没有食欲， 皮肤干燥发黄或苍白、头发干枯没有光泽，妇女经水愆期、量少色淡等。\n常见人群：\n1.\t一部分脾胃功能虚弱的人群；\n2.\t患有慢性消耗性疾病，或久病不愈的人群；\n3.\t患有导致失血的一类疾病的人群，例如女性功能性子宫出血、子宫肌瘤等；\n4.\t部分患有血液病相关疾病的人群。',
		'rela_en': 'remark',
		'rela_zh': '备注',
		'is_show': True,
		'ann_pro': '',
		'level': 2
	}, {
		'type_pro': 'objectproperty',
		'source': '血虚证',
		'target': '中医-证',
		'rela_en': 'classify_by',
		'rela_zh': '分类',
		'ann_pro': '',
		'is_show': True,
		'level': 2
	}]

all_list = []
for a in c:
    one = str(a["source"]) + str(a["target"])
    all_list.append(one)

print(all_list)
print(len(all_list))
print(len(set(all_list)))