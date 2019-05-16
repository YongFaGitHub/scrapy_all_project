# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['s.weibo.com']
    start_urls = []

    def start_requests(self):

        for i in range(1,13):
            url = 'https://s.weibo.com/weibo/%23%E8%8F%8A%E5%AD%90%E7%BE%8E%E9%A3%9F%E8%AE%B0%23&page={}'.format(i)
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)
    def parse(self, response):
        # print(response.body.decode())

        url_lsit = response.xpath("//div[@class='media media-article-a']//div[@class='thumbnail']/a")
        for url in url_lsit:
            url_text = url.xpath("./@href").extract_first()

            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36" ,
                "Upgrade-Insecure-Requests": "1",
                "Connection": "keep-alive",
                "host": "weibo.com",
                "cookie": "TC-V5-G0=ffc89a27ffa5c92ffdaf08972449df02; _s_tentry=-; Apache=2062930205846.9246.1541471887986; SINAGLOBAL=2062930205846.9246.1541471887986; ULV=1541471888122:1:1:1:2062930205846.9246.1541471887986:; TC-Page-G0=2b304d86df6cbca200a4b69b18c732c4; SUB=_2AkMsvHHCf8NxqwJRmP0WyW_kaY92yAzEieKa4IAZJRMxHRl-yT9jqk4dtRB6BzxfLUvVTpzYEJfuB5S93TYVDyHKRc2K; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhL4ex4CugZ26hm3AqpdRMH; YF-Page-G0=091b90e49b7b3ab2860004fba404a078; WBStorage=e8781eb7dee3fd7f|undefined"}

            yield scrapy.Request(url_text,callback=self.parse_disease,dont_filter=True,headers=header)

    def parse_disease(self,response):
        item = {}

        # print(response.body.decode())
        title = response.xpath("//div[@class='main_editor ']/div[@class='title']/text()").extract_first()

        item["title"] = title
        p_list = response.xpath("//div[@class='main_editor ']/div[@class='WB_editor_iframe']/p")
        p_s = ""
        for p in p_list:
            p_text_raw_raw = p.xpath("./text()").extract()
            if len(p_text_raw_raw) >= 1:
                p_text_raw = str(p_text_raw_raw).replace(" ", "").replace("['", "").replace("']",
                "").replace("\\u200b", "").replace("\\n", "").replace("\\xa0", "").replace("','",
                "").replace("★","").replace("▼","").replace("1、","").replace("2、","").replace("3、",
                "").replace("4、","").replace("5、","").replace("6、","").replace("7、","").replace("8、",
                "").replace("9、","").replace("10、","").replace("11、","")
                if len(p_text_raw) > 2:
                    p_s += p_text_raw + "\n"
        item["content"] = p_s

        with open("H:/meishi.csv","a+",encoding="utf-8") as f:
            if title is not None:
                f.write(title)
            f.write("\n")
            f.write(p_s)
        # if title is not None:
        #     yield item






