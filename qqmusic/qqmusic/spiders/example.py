# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['y.qq.com']
    start_urls = ['http://y.qq.com/portal/playlist.html']

    def parse(self, response):
        div_list = response.xpath("//div[@class='js_1024']/div")
        for div in div_list:
            text = div.xpath(".//text()").extract_first()
            print(text)


           '''
           
           https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg
           ?picmid=1&rnd=0.7832730818944968&g_tk=5381&jsonpCallback=
           getPlaylist&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8
           &outCharset=utf-8&notice=0
           &platform=yqq&needNewCode=0&categoryId=10000000&sortId=5
           &sin=0&ein=29
           
           
           
           https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg?picmid=1&rnd=0.6088431554527229&g_tk=5381&jsonpCallback=getPlaylist&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&categoryId=136&sortId=5&sin=0&ein=29
           https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg?picmid=1&rnd=0.41516030941225535&g_tk=5381&jsonpCallback=getPlaylist&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&categoryId=194&sortId=5&sin=0&ein=29
           '''