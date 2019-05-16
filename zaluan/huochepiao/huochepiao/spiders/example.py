# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['12306.com']
    start_urls = []

    def start_requests(self):
        url = 'https://kyfw.12306.cn/otn/index/initMy12306Api'

        cookies = {"Cookie":"JSESSIONID=2F07C68339865E890C654B1BB4AB7003; tk=zgfBrZ3XotNuF4-u8Z9jdmHwl28eKIOnLPEPpQAEPkEcOyf4mk9290; BIGipServerotn=1039139338.24610.0000; RAIL_EXPIRATION=1546822235736; RAIL_DEVICEID=IwSnBkt7sXTeBRkuReiHQtIyYzrqCh89SbqsbeQWtlKAlL_EixYN8gayqtkdUAIF91PpxxHUVuPmw7v-on6EOG5oBaR9FeR3twnWbWr9SgDPfYMiio4Dbh5QVWVBhjIIvKft_iUoA9KSQ7_xnOOR22I3lVlarX6H; BIGipServerpool_passport=300745226.50215.0000; route=6f50b51faa11b987e576cdb301e545c4"}

        yield scrapy.FormRequest(url, callback=self.parse, cookies=cookies)

    def parse(self, response):
        print("####")
        print(response)
        print("####")
        # text = response.xpath("//li[@id='J-header-logout']//text()").extract()
        # print(text)