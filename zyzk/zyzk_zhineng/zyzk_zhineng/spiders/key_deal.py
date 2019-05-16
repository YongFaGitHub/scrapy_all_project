# import requests
#
# url = "https://www.zk120.com/zhen/diagnose"
# headers = {
#     "accept":"application/json, text/javascript, */*; q=0.01",
#     "accept-encoding":"gzip, deflate, br",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "content-length": "40",
#     "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "origin": "https://www.zk120.com",
#     "referer": "https://www.zk120.com/zhen/?nav=ys",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
#     "x-csrftoken": "rsYOTF0E0OpMd4wtbzkfjCABSXCu4I70",
#     "x-requested-with": "XMLHttpRequest",
#     "cookie":"pgv_pvi=9169763328; NTKF_T2D_CLIENTID=guestA3BCCF13-EDE6-B0E0-75C7-9AC334579E0C; sessionid=p225vz3dtemmiz9glfg55sifa8oiht92; csrftoken=rsYOTF0E0OpMd4wtbzkfjCABSXCu4I70; shfskey=20181022T075258.788267672481; pgv_si=s6861075456; nTalk_CACHE_DATA={uid:kf_9050_ISME9754_guestA3BCCF13-EDE6-B0,tid:1541067033603292}; checkCookieTime=1541067033670; svrid=5aff15db8fb99d9bd967d5b9eeccc5d1"
# }
#
# formdata = {
#     "trace":"316283.99,261521.4894,242657.7653,789008.6154,240019.4849",
#     "choice":"yes"
# }
#
# r = requests.post(url=url,headers=headers,data=formdata)
# print(r.text)
#
#
#
#
# # import time
# # timestamp = str((time.time()*1000)).split('.')[0]
# # print(timestamp)
#
a = {'symptoms': ['身体、眼睛、小便发黄', '腰膝酸软', '发病时间短，黄色鲜明，舌苔黄腻', '头身困重、胃胀腹满'], 'answer': {'goods': ['[YZ][278xa26memkc3:356069590]清补凉:清热解毒 养生保健:民间养生保健必备养生汤料。'], 'diagnosis': '黄疸:湿热发黄', 'fang': {'medicines': [{'name': '茵陈', 'unit': 'g', 'quantity': '4'}, {'name': '白术', 'unit': 'g', 'quantity': '9'}, {'name': '赤茯苓', 'unit': 'g', 'quantity': '9'}, {'name': '猪苓', 'unit': 'g', 'quantity': '9'}, {'name': '桂枝', 'unit': 'g', 'quantity': '6'}, {'name': '泽泻', 'unit': 'g', 'quantity': '15'}], 'name': '茵陈五苓散', 'composition': '茵陈4g\xa0 白术9g\xa0 赤茯苓9g\xa0 猪苓9g\xa0 桂枝6g\xa0 泽泻15g'}, 'doctor': '{"head":"咨询医生","doc_name":"郑宇红","img":"/media/widgets/banners/2018/05/180425084705084.20180525014056101.jpg","section":"中医内科","zhi":"主治医师","title":"医学硕士","description":"擅治：黄疸、便秘、腹泻、腹痛等消化系统疾病，师从名师，经验丰富。","path":"/fw/expert/83?shprefix=linzheng-huangdan-wenzhen"}', 'default': 'default', 'nature': '{"head":"自然疗法","name":"艾灸疗法","text":["1. 主灸穴：风池穴、 肝俞穴、 脾俞穴、 肾俞穴、 肺俞穴。","2. 配灸穴：热重加灸大椎穴；腹胀纳呆加灸中脘穴 ；脘腹痞闷加灸足三里穴 ；呕吐加灸内关穴 ；神疲畏寒加灸命门穴、关元穴 ；大便溏泄加灸天枢穴。","3. 每次施灸时，每穴灸3～5壮，每日灸1次或2次，10次为1个疗程。"],"path":"/baike/w/%E9%BB%84%E7%96%B8?shprefix=linzheng-huangdan-baike#.E4.B8.AD.E5.8C.BB.E8.AF.8A.E6.96.AD.E9.89.B4.E5.88.AB"}', 'anli': '{"head":"参考病例","anname":"黄疸：阳黄 湿热 内蕴证","doc_name":"李振华","section":"国医大师","zhi":"主任医师","title":"教授","path":"/an/7711.html?shprefix=linzheng-huangdan-zkan","text":["主诉：周身肌肤、小便黄已三月余，伴随腹胀、纳差、厌食油腻，周身困乏。","辨证分析：因过服寒凉药物致脾阳受损，湿着留滞，胆液被阻，外溢肌肤而发黄。","治则治法：健脾和胃，化湿清热，理气退黄。","治疗方法：32剂，茵陈、白术、茯苓、泽泻、桂枝、香附、郁金、川朴、砂仁、广木香、焦三仙各、青皮、甘草。","病情变化：面色黄、小便黄减轻，肝功检查明显好转。"]}', 'tiao': '47256', 'cheng': '甘露消毒丹\xa0 茵陈五苓散', 'cases': '黄疸', 'cause': '湿热发黄是指湿热互结，壅遏气机，影响了肝胆的疏泄，使胆汁不能按照常规的道路来排泄，逆流入血，泛溢肌肤，而发为身黄。或者说湿热中阻，迫使脾色外露，黄发肌肤。'}, 'solution': '/zhen/solution/92291,224445,166870,147690', 'success': True, 'tree_id': 769}