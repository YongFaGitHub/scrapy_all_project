# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['store.steampowered.com/']
    start_urls = ['http://store.steampowered.com/bundle/7399/Whale_Rock_Games_bundle/']

    def parse(self, response):
        #图片地址
        img_url = response.xpath("//img[@class='package_header']/@src").extract_first()

        #五种字段
        div_box = response.xpath("//div[@class='block_content block_content_inner']/div[1]/p/*/text()").extract()


        #单人什么玩意。。还有后面的字
        danren_raw = response.xpath("//div[@class='details_block']//text()").extract()
        danren = str(danren_raw)

        #价格标签
        jiage_raw = response.xpath("//div[@class='game_purchase_action_bg']")

        #捆绑的文字
        kunbang_raw = response.xpath("//div[@class='game_area_description bundle_description']/p//text()").extract()
        kunbang = str(kunbang_raw)

        #捆绑的游戏地址
        kunbangurl_raw = response.xpath("//div[@class='bundle_package_item complete_the_set']/div/a/@href").extract()
        kunbangurl = str(kunbangurl_raw)

        print(img_url,"@@@@@@@")
        print(div_box,"###")
        print(danren,"$$$$")
        print(kunbang,"%5%%%%")
        print(kunbangurl,"^^…………")
