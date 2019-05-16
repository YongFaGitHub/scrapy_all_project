# -*- coding: utf-8 -*-
import scrapy
import re

class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['weibo.com/']
    start_urls = []

    def start_requests(self):
        url = 'http://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_all=1&pagebar=0&id=1005056094607440&page=1'
        # header = {
        #     "User-Agent":
        #         "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
        #     "Cookie":
        #         "SINAGLOBAL=2062930205846.9246.1541471887986; UOR=,,www.sogou.com; SCF=And8B39Te5KxeDr9Pud1IA5-fOK2tDqhP1Lx0EmploZ6F39iour3e7QrTHR8kty-vab67d4ybCQM7v8tVzfbCVs.; SUHB=0jB4aLduCHlfsB; TC-Page-G0=6fdca7ba258605061f331acb73120318; SUB=_2AkMrTUcZf8NxqwJRmP0WyW_kaY92yAzEieKdEbbCJRMxHRl-yT9jqn0StRB6AM1p6DSl9DqVLxP4tolEr61jPj4Az5y6; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhL4ex4CugZ26hm3AqpdRMH; _s_tentry=passport.weibo.com; Apache=2536565412440.73.1544669230595; ULV=1544669230601:4:2:2:2536565412440.73.1544669230595:1544411904199; TC-V5-G0=914ba011d20e5b7f25fe12574c186eda; YF-V5-G0=1312426fba7c62175794755e73312c7d"
        # }
        cookies = {"Cookie":
                "SINAGLOBAL=2062930205846.9246.1541471887986; UOR=,,www.sogou.com; SCF=And8B39Te5KxeDr9Pud1IA5-fOK2tDqhP1Lx0EmploZ6F39iour3e7QrTHR8kty-vab67d4ybCQM7v8tVzfbCVs.; SUHB=0jB4aLduCHlfsB; TC-Page-G0=6fdca7ba258605061f331acb73120318; SUB=_2AkMrTUcZf8NxqwJRmP0WyW_kaY92yAzEieKdEbbCJRMxHRl-yT9jqn0StRB6AM1p6DSl9DqVLxP4tolEr61jPj4Az5y6; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhL4ex4CugZ26hm3AqpdRMH; _s_tentry=passport.weibo.com; Apache=2536565412440.73.1544669230595; ULV=1544669230601:4:2:2:2536565412440.73.1544669230595:1544411904199; TC-V5-G0=914ba011d20e5b7f25fe12574c186eda; YF-V5-G0=1312426fba7c62175794755e73312c7d"
}

        yield scrapy.Request(url, callback=self.parse, dont_filter=True, cookies=cookies)

    def parse(self, response):
        print(response.body)
        # list = re.findall("video-sources=(.*?)action-data=", response.body.decode("gb2312"), re.S)

