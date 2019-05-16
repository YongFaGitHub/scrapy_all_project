import requests
import csv
import re
import os


#读取的 含有title的文件 并且获取到 类别id title 和 key
code_num_file =  open("H:/url_xima.txt","r")
reader_num = csv.reader(code_num_file)

for num_one in reader_num:
    #初始化
    a = 0
    b = 0
    url = ""
    num = ""
    class_id = ""
    title = ""
    class_name = ""
    # print(num_one)
    for i in num_one:
        if "Response body" in i:
            #类别编号
            class_id_raw = re.findall('uid":(.*)',i)
            class_id = class_id_raw[0]
            # print(class_id)
        if "duration" in i:
            #小视频编号
            num = i.replace("duration:","")
            # print(num)
        if "title" in i:
            #小节名称
            title = i.replace("title:","").replace('"',"")
            # print(title)

    #类名 读取含有类别的文件
    title_name_file = open("H:/title.txt", "r")
    title_name = csv.reader(title_name_file)
    for title_ons in title_name:
        # print("111")
        if a == 0:
            # print("222")
            # print(title_ons)
            char_raw = "anchorId:" + class_id
            if char_raw in str(title_ons):
                a = 1
                title_raw = re.findall("albumName:(.*?)anchorId:", str(title_ons))
                title_tt = re.findall("(.*?)'", (title_raw[0]).replace('"', ""))
                class_name = title_tt[0]
                # print(class_name)


    #读取含有视频地址的文件
    m4a_url_file = open("H:/get.txt", "r")
    m4a_url_read = csv.reader(m4a_url_file)
    for url_m4a in m4a_url_read:
        if b == 0:
            # print(url_m4a)
            if len(url_m4a) >0:
                if "Request url" in url_m4a[0]:
                    url_num_raw = re.findall("duration=(.*)",(url_m4a[0]))
                    if int(url_num_raw[0]) == int(num):
                        b = 1
                        url = "http://" + (url_m4a[0]).replace("Request url: ","")
                        # print(url)
                        # print(url_m4a[0])

    if len(class_name) < 1:
        r = requests.get(url)
        print("未得到大类名称 ----- 音频文件名:",title)
        with open("H:/FM/{}.m4a".format(title), "wb") as  f:
            f.write(r.content)
    else:
        try:os.mkdir("H:/FM/{}".format(class_name))
        except:pass

        print("章节大类：",class_name)
        print("音频文件名：",title)
        list_file = os.listdir("H:/FM/{}".format(class_name))

        if title in str(list_file):
            print(title,"--------重复")

        else:
            r = requests.get(url)
            with open("H:/FM/{}/{}.m4a".format(class_name,title),"wb") as  f:
                f.write(r.content)


    print("%%%"*100)







                    #https://www.ximalaya.com/revision/album?albumId=6715874
# r = requests.get("http://audio.pay.xmcdn.com/download/1.0.0/group1/M05/07/85/wKgJMlkwyjfSj1gYAHlTJrRnU_0746.m4a?sign=f5d634f503b37d1a3f08c340d178270a&buy_key=332E3734353633363331303138323636392D302E3434373630383739353236373736303135&token=2825&timestamp=1536732154970721&duration=982")
# with open("./tt.m4a","wb") as f:
#     f.write(r.content)



