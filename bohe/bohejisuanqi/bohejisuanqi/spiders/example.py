# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, FormRequest
import re


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.boohee.com/']
    start_urls = []

    def start_requests(self):
        for i in range(1, 11):
            url = "http://www.boohee.com/can/hot_activities?date=2019-03-25&page={}&authenticity_token=tBvcNMZ7UfZBo1yCpWaLkV4PtiiS%2BbGpluZoEwGXQLI%3D".format(i)
            yield Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        div_list = response.xpath("//div[@class='can-menu']/div/div")
        for div in div_list:
            text = div.xpath("./div[@class='oper']/a/@onclick").extract_first()
            url_raw = re.findall("url:'(.*?)'}", text)[0]
            url = "http://www.boohee.com" + url_raw
            ass_token = "tBvcNMZ7UfZBo1yCpWaLkV4PtiiS+bGpluZoEwGXQLI="

            formdata = {"authenticity_token": ass_token}

            yield FormRequest(url, callback=self.parse_one_dateils,
                              dont_filter=True, formdata=formdata)

    def parse_one_dateils(self, response):
        item = {}
        tr_list = response.xpath("//div[@class='record-body']//tr")
        for tr in tr_list:
            text_name = tr.xpath("./td[@class='name']/div[@class='limit']/@title").extract_first()
            item["title"] = text_name
            unit = tr.xpath("./td[@class='unit']//span[@class='limit']/text()").extract()
            item["unit"] = str(unit).replace("['", "").replace("']", "").replace(" ",
                                        "").replace("\\n", "").replace("\\t", "")

            cal = tr.xpath("./td[@class='cal']/div[@class='limit right']/@title").extract_first()

            item["cal"] = cal
            yield item





