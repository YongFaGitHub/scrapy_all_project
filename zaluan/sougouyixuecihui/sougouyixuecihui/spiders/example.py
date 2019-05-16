# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['pinyin.sogou.com']
    start_urls = ['https://pinyin.sogou.com/dict/cate/index/132/default/']

    def parse(self, response):
        item = {}

        div_list = response.xpath("//div[@id='dict_detail_list']/div[1]/following-sibling::*")
        ""
        for div in div_list:
            name = div.xpath(".//div[@class='detail_title']/a/text()").extract_first()
            item["name"] = name

            url_raw = div.xpath("./div[@class='dict_detail_show']/div[@class='dict_dl_btn']/a/@href").extract_first()
            yield scrapy.Request(url_raw,callback=self.parse_w,dont_filter=True,meta={"item":deepcopy(item)})

        next_url_raw = response.xpath("//div[@id='dict_page']/div//a[text()='下一页']/@href").extract_first()
        if next_url_raw is not None:
            next_url = "http://pinyin.sogou.com" + next_url_raw
            yield scrapy.Request(next_url,callback=self.parse,dont_filter=True)

    def parse_w(self, response):
        item = response.meta["item"]
        with open("F:/pycharmproject/project/zaluan/sougouyixuecihui/sougouyixuecihui/spiders/sougou/{}.scel".format(item["name"]),"wb") as f:
            f.write(response.body)
