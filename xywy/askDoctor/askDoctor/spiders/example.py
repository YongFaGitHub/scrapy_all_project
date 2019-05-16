import scrapy
import requests
from scrapy.http import Request
import selectors


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['club.xywy.com']
    start_urls = []

    def start_requests(self):
        a = "2017-{}-{}"

        for month in range(1, 3):
            if len(str(month)) < 2:
                month = "0" + str(month)
            for day in range(1, 30):  # 日
                if len(str(day)) < 2:
                    day = "0" + str(day)
                month_day = a.format(month, day)

                for i in range(1, 7000):
                    url = 'http://club.xywy.com/keshi/{}/'.format(month_day) + str(i) + '.html'  # 2017-10-02

                    yield Request(url, callback=self.parse_one)

    def parse_one(self, response):
        url_list = []  # 创建一个大的list存储所有的url
        urls = response.xpath("//em//a[@target=\'_blank\']/@href").extract()
        n = len(urls)
        print(n)
        for i in range(0, n):
            all_urls = urls[i]
            print(all_urls)
            yield Request(all_urls, callback=self.parse_second)

    def parse_second(self, response):
        items = {}
        titleClass = response.xpath('//div//p//a[@target=\'_blank\']/text()').extract()
        title = titleClass[3]
        # if title == "肾内科":
        items['titleClass'] = title
        question_raw = response.xpath('//div[@id=\'qdetailc\']/text()').extract()
        question = str(question_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '')
        # print(question)
        items['question'] = question

        answer_raw = response.xpath('//div[@class=\'pt15 f14 graydeep  pl20 pr20\']/text()').extract()
        answer = str(answer_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '')
        items['answer'] = answer
        # print(answer)

        gender_raw = response.xpath('//div[@class =\'User_askcon clearfix pr\'] / div[3] / span[3]').extract()
        gender = str(gender_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '').replace('<span>',
                                                                                                  '').replace(
            '</span>', '')

        items['gender'] = gender

        age_raw = response.xpath('//div[@class=\'User_askcon clearfix pr\']/div[3]/span[5]').extract()
        age = str(age_raw).replace('\\t', '').replace('\\r', '').replace('\\n', '').replace('<span>', '').replace(
            '</span>', '')

        items['age'] = age

        yield items