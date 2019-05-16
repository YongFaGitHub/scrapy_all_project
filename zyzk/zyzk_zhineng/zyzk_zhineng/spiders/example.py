# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import FormRequest
from copy import deepcopy
import time


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['zk120.com/']
    start_urls = []
    def start_requests(self):
        url = 'https://www.zk120.com/zhen/diagnose'

        while True:
            yield scrapy.Request(url,callback=self.parse,dont_filter=True)
            time.sleep(2)



    # 处理初始化的性别对应的疾病的trace
    def parse(self, response):
        '''
        sex_list: 得到的是包含男女儿童的整个大的列表，遍历之后可以得到三个对象
        body_list：获得单个性别中的除了常见之外的所有部位的列表，遍历之后可以得到所有的部位
        body_list_content ： 某个部位中的所有包含疾病的列表，遍历之后得到单个疾病的字典
        body_list_content_name：单个疾病的字典
        :param response:
        :return:
        '''
        item = {}
        # print(response.body.decode())
        content = json.loads(response.body)
        sex_list = content["classifier"]["root"]["children"][0]["children"]
        for sex in sex_list:
            # print(sex,"************************************") #三大类
            item["sex"] = sex["text"]
            body_list = sex["children"][1:]  # 男女儿童的 三个分类的所有的疾病，单项
            for body_buwei in body_list:
                # print(body_list)
                item["body"] = body_buwei["text"]
                body_list_content = body_buwei["children"]
                for body_list_content_name in body_list_content:
                    # print(item["sex"], item["body"], body_list_content_name)
                    # print("*"*100)
                    trace = body_list_content_name["trace"]
                    item["title"] = body_list_content_name["text"]
                    item["question"] = ""

                    url = "https://www.zk120.com/zhen/diagnose"

                    headers = {
                        "referer": "https://www.zk120.com/zhen/?nav=ys",
                        "x-csrftoken": "rsYOTF0E0OpMd4wtbzkfjCABSXCu4I70",
                        "x-requested-with": "XMLHttpRequest",
                        "cookie": "pgv_pvi=9169763328; NTKF_T2D_CLIENTID=guestA3BCCF13-EDE6-B0E0-75C7-9AC334579E0C; sessionid=p225vz3dtemmiz9glfg55sifa8oiht92; csrftoken=rsYOTF0E0OpMd4wtbzkfjCABSXCu4I70; shfskey=20181022T075258.788267672481; pgv_si=s6861075456; nTalk_CACHE_DATA={uid:kf_9050_ISME9754_guestA3BCCF13-EDE6-B0,tid:1541124010239005}; checkCookieTime=1541124010335; svrid=5fd27ea780c4a754f52d79b63edaaf3b"
                    }

                    formdata = {
                        "trace": trace,
                        "choice": "yes"
                    }
                    yield FormRequest(
                        url=url,
                        headers=headers,
                        formdata=formdata,
                        callback=self.parse_question,
                        dont_filter=True,
                        meta={"item": deepcopy(item),"ask":deepcopy("")}
                    )
                    # time.sleep(3)

    # 解析初始化的第一个问题，第一个问题以及以后的问题都是随机生成的，所以之后要反复的请求一个问题
    def parse_question(self, response):
        item = response.meta["item"]

        # print(response.body)
        try :
            content = json.loads(response.body)

            # print(content)
            # 判断此次响应是问题还是结论，如果是问题 则请求下一个问题，分两个，是与否
            try:
                item["question"] += content["question"] + "**"
                url = "https://www.zk120.com/zhen/diagnose"

                headers = {
                    "referer": "https://www.zk120.com/zhen/?nav=ys",
                    "x-csrftoken": "rsYOTF0E0OpMd4wtbzkfjCABSXCu4I70",
                    "x-requested-with": "XMLHttpRequest",
                    "cookie": "pgv_pvi=9169763328; NTKF_T2D_CLIENTID=guestA3BCCF13-EDE6-B0E0-75C7-9AC334579E0C; sessionid=p225vz3dtemmiz9glfg55sifa8oiht92; csrftoken=rsYOTF0E0OpMd4wtbzkfjCABSXCu4I70; shfskey=20181022T075258.788267672481; pgv_si=s6861075456; nTalk_CACHE_DATA={uid:kf_9050_ISME9754_guestA3BCCF13-EDE6-B0,tid:1541124010239005}; checkCookieTime=1541124010335; svrid=5fd27ea780c4a754f52d79b63edaaf3b"
                }
                formdata1 = {
                    "trace": content["trace"],
                    "choice": "yes"
                }
                formdata2 ={
                    "trace": content["trace"],
                    "choice": ""
                }
                # time.sleep(5)
                question = item["question"]

                item["question"] = question +"是***"
                yield FormRequest(
                    url=url,
                    headers=headers,
                    formdata=formdata1,
                    callback=self.parse_question,
                    dont_filter=True,
                    meta={"item": deepcopy(item)}
                )
                # time.sleep(4)

                item["question"] = question + "否***"
                yield FormRequest(
                    url=url,
                    headers=headers,
                    formdata=formdata2,
                    callback=self.parse_question,
                    dont_filter=True,
                    meta={"item": deepcopy(item)}
                )
            #判断是否是结论
            except:
                # 过滤部分未知问题
                item["answer"] = str(content)
                if "'question': None" in item["answer"]:
                    pass
                else:
                    yield item
        except:
            img_url = "http://www.zk120.com" + response.xpath("//div[@class='vcode-absolute vcode_content']/img/@src").extract_first()
            yield scrapy.Request(img_url,callback=self.parse_img,dont_filter=True)
            # time.sleep(200)

    def parse_img(self,response):
        with open("F:\pycharmproject\project\zaluan\zyzk_zhineng\zyzk_zhineng\spiders\img.jpg","wb") as f:
            f.write(response.body)

        yan = input("请输入验证码:")
        url = "https://www.zk120.com/zhen/?nav=ys"

        headers = {
            "referer": "https://www.zk120.com/zhen/?nav=ys",
            "x-csrftoken": "rsYOTF0E0OpMd4wtbzkfjCABSXCu4I70",
            "x-requested-with": "XMLHttpRequest",
            "cookie": "pgv_pvi=9169763328; NTKF_T2D_CLIENTID=guestA3BCCF13-EDE6-B0E0-75C7-9AC334579E0C; sessionid=p225vz3dtemmiz9glfg55sifa8oiht92; csrftoken=rsYOTF0E0OpMd4wtbzkfjCABSXCu4I70; shfskey=20181022T075258.788267672481; pgv_si=s6861075456; nTalk_CACHE_DATA={uid:kf_9050_ISME9754_guestA3BCCF13-EDE6-B0,tid:1541124010239005}; checkCookieTime=1541124010335; svrid=5fd27ea780c4a754f52d79b63edaaf3b"
        }

        formdata = {
            "vcode":yan,
            "_form4antispider": "true"
        }
        yield FormRequest(
            url=url,
            headers=headers,
            formdata=formdata,
            callback=self.parse,
            dont_filter=True,

        )
        # time.sleep(200)

