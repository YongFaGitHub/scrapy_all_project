# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from copy import deepcopy
import re
import csv

'''
n级标题 前面就加了n个# 后面是空格
'''

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['zk120.com/baike']
    start_urls = ["https://www.zk120.com/baike/w/止血药"]
    def __init__(self):
        self.list = []
        self.list_e = []


    def start_requests(self):
        url_list_start = ["https://www.zk120.com/baike/w/疾病",
                          "https://www.zk120.com/baike/w/中药",
                          "https://www.zk120.com/baike/w/%E9%AB%98%E8%A1%80%E5%8E%8B"
                          "https://www.zk120.com/baike/w/%E6%85%A2%E6%80%A7%E5%92%BD%E7%82%8E"
                          ]

        for start_url in url_list_start:
            yield Request(start_url,callback=self.parse,dont_filter=True)


    def parse(self, response):
        item = {}

        title = response.xpath("//div[@class='mw-body']/h1/text()").extract_first()
        item["title"] = title


        table_list = re.findall('(<table class="wikitable".*?</table>)', str(response.body.decode()), re.S)
        # print(len(table_list))
        item["table_list"] = str(table_list)

        all = response.xpath("//div[@id='mw-content-text']/h2 | //div[@id='mw-content-text']/h3 | //div[@id='mw-content-text']/p | //div[@id='mw-content-text']/ol ")
        content = ""
        for a in all:
            # print(str(a))
            #判断二级标题
            if "data='<h2>" in str(a):
                h2_text = a.xpath(".//text()").extract()
                if h2_text[0] != "参看":
                    # print(h2_text)
                    content += "## " + h2_text[0] + "\n"
            #判断三级标题
            if "data='<h3>" in str(a):
                h3_text = a.xpath(".//text()").extract()
                content += "### " + h3_text[0] + "\n"
            #判断p标签
            if "data='<p>" in str(a):
                p_text_raw = a.xpath(".//text()").extract()

                p_text = str(p_text_raw).replace("['","").replace("']","").replace(" ","").replace("','","").replace("\\u3000","").replace("\\xa0","")
                content += p_text

            #判断table
            if "data='<ol" in str(a):
                ol_text_raw = a.xpath(".//text()").extract()
                ol_text = str(ol_text_raw).replace("['", "").replace("']", "").replace(" ", "").replace("','", "").replace("\\u3000","").replace("\\xa0","")
                content += ol_text

        item["content"] = content
        yield item



        a_list_url = response.xpath("//div[@id='mw-content-text']/h2//a | //div[@id='mw-content-text']/h3//a | //div[@id='mw-content-text']/p//a | //div[@id='mw-content-text']/ol//a | //div[@id='mw-content-text']/table//a ")
        for a_url in a_list_url:

            a_title = a_url.xpath("./@title").extract_first()
            a_url_text = a_url.xpath("./@href").extract_first()
            if "index.php?" in a_url_text:
                if a_title not in self.list_e:
                    self.list_e.append(a_title)
                    print("无链接")
                    with open("H:/zyzk/zyzk_title_empy.txt","a+",encoding="utf-8") as f:
                        f.write(a_title + "\n")

            else:
                if a_title not in self.list:
                    self.list.append(a_title)
                    with open("H:/zyzk_title.txt","a+",encoding="utf-8") as f:
                        f.write(a_title + "\n")
                    yield Request("https://www.zk120.com"+a_url_text,callback=self.parse,dont_filter=True)



        # item = {}
        # title  = response.xpath("//div[@class='mw-body']/h1/text()").extract_first()
        # item["title"] = title
        # content = str(response.body.decode())
        # text = re.findall('(<div id="mw-content-text" lang="zh-CN".*?)<h2><span class="mw-headline hede" id=".E5.8F.82.E7.9C.8B">参看</span></h2>',content,re.S)
        # try:
        #     content_raw = str(text[0])
        #     raw = re.findall('(<div id="toc" class="toc".*?</ul>\n</div>)',content_raw,re.S)
        #     content = content_raw.replace(raw[0],"")
        #     item["content"] = content
        #     # yield item
        #     # print(item)
        # except:
        #     #直接就是定义的网页的爬取
        #     p_list = response.xpath("//div[@class='mw-content-ltr']/p | //div[@class='mw-content-ltr']/h2 |//div[@class='mw-content-ltr']/ol |//div[@class='mw-content-ltr']/h3 ")
        #     p_s = ""
        #     for p in p_list:
        #         p_text_raw = p.xpath(".//text()").extract()
        #         p_text = str(p_text_raw).replace("['","").replace("']","").replace(" ","").replace("','","").replace("\\u3000",
        #         "").replace("\\xa0","")
        #         p_s += p_text
        #     print(p_s)
        #     print("@@"*50)


    # item = {}
    # h2 = response.xpath("//h2/span[text()='参看']")
    # if len(h2) >= 1:
    #
    #     title  = response.xpath("//div[@class='mw-body']/h1/text()").extract_first()
    #     item["title"] = title
    #     content = str(response.body.decode())
    #     text = re.findall('(<div id="mw-content-text" lang="zh-CN".*?)<h2><span class="mw-headline hede" id=".E5.8F.82.E7.9C.8B">参看</span></h2>',content,re.S)
    #     try:
    #         content_raw = str(text[0])
    #         raw = re.findall('(<div id="toc" class="toc".*?</ul>\n</div>)',content_raw,re.S)
    #         content = content_raw.replace(raw[0],"")
    #         item["content"] = content
    #         # yield item
    #         # print(item)






    #构造初始的地址
    # def start_requests(self):
    #
    #     fdir = open("H:/zhy.txt", "rt", encoding="utf-8")
    #     read = csv.reader(fdir)
    #     for line in read:
    #         url ="https://www.zk120.com/baike/w/" + line[0]
    #         print(url)
    #         yield Request(url,callback=self.parse,dont_filter=True)
    #
    #
    # #解析每个关键词的页面
    # def parse(self, response):
    #     #现已发现分三种网站结构
    #     response.xpath()
    #
    #



    # def parse(self, response):
    #     a_list = response.xpath("//div[@id='mw-content-text']/p//a")
    #     for a in a_list:
    #         url_raw = a.xpath("./@href").extract_first()
    #         url = "https://www.zk120.com" + url_raw
    #         name = a.xpath("./text()").extract_first()
    #
    #         #查看有没有此项
    #         fdir = open("H:/zyzk.txt", "rt", encoding="utf-8")
    #         read = csv.reader(fdir)
    #         list = []
    #         for line in read:
    #             list.append(line[0])
    #
    #         if name not in list:
    #             #如果没有则写入
    #             with open("H:/zyzk.txt", "a+", encoding="utf-8") as f:
    #                 f.write(name)
    #                 f.write("\n")
    #
    #             #并且请求
    #             yield scrapy.Request(url, callback=self.parse, dont_filter=True)
























    # def parse(self, response):
    #     content = str(response.body.decode())
    #     text = re.findall('(<div id="mw-content-text" lang="zh-CN".*?)<h2><span class="mw-headline hede" id=".E5.8F.82.E7.9C.8B">参看</span></h2>',content,re.S)
    #     yield text
    #
    #     a_list = response.xpath("//div[@id='mw-content-text']/p//a")
    #     for a in a_list:
    #         url_raw = a.xpath("./@href").extract_first()
    #         url = "https://www.zk120.com" + url_raw















