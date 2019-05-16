# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re


class ExampleSpider(scrapy.Spider):
    name = 'jieba_try'
    allowed_domains = ['zk120.com/']
    start_urls = ['https://www.zk120.com/baike/w/%E7%89%B9%E6%AE%8A:%E6%89%80%E6%9C%89%E9%A1%B5%E9%9D%A2']

    def parse(self, response):
        li_list = response.xpath("//ul[@class='mw-allpages-chunk']/li")
        for li in li_list:
            url_raw = li.xpath("./a/@href").extract_first()
            url = "https://www.zk120.com" + url_raw

            yield Request(url,callback=self.parse_disease,dont_filter=True)
        next_url_raw = response.xpath("//div[@class='mw-allpages-nav']/a[contains(text(),'下一页')]/@href").extract_first()
        if next_url_raw is not None:
            next_url = "https://www.zk120.com" + next_url_raw

            yield Request(next_url, callback=self.parse, dont_filter=True)

    def parse_disease(self,response):
        item = {}
        title = response.xpath("//div[@class='mw-body']/h1/text()").extract_first()
        item["title"] = title

        table_list = re.findall('(<table class="wikitable".*?</table>)', str(response.body.decode()), re.S)
        # print(len(table_list))
        item["table_list"] = str(table_list)

        all = response.xpath(
            "//div[@id='mw-content-text']/h2 | //div[@id='mw-content-text']/h3 | //div[@id='mw-content-text']/p | //div[@id='mw-content-text']/ol | //div[@id='mw-content-text']/ul ")
        content = ""
        for a in all:
            # print(str(a))
            # 判断二级标题
            if "data='<h2>" in str(a):
                h2_text = a.xpath(".//text()").extract()
                if h2_text[0] != "参看":
                    # print(h2_text)
                    content += "\n## " + h2_text[0] + "\n"
            # 判断三级标题
            if "data='<h3>" in str(a):
                h3_text = a.xpath(".//text()").extract()
                content += "### " + h3_text[0] + "\n"
            # 判断p标签
            if "data='<p>" in str(a):
                p_text_raw = a.xpath(".//text()").extract()

                p_text = str(p_text_raw).replace("['", "").replace("']", "").replace(" ", "").replace("','",
                                                                                                      "").replace(
                    "\\u3000", "").replace("\\xa0", "").replace("\\n","\n")
                content += p_text

            # 判断table
            if "data='<ol" in str(a):
                ol_text_raw = a.xpath(".//text()").extract()
                ol_text = str(ol_text_raw).replace("['", "").replace("']", "").replace(" ", "").replace("','",
                "").replace("\\u3000", "").replace("\\xa0", "").replace("\\n","\n")
                content += ol_text

        content_ = content.replace("\\n", "\n")
        # print(content_)

        item["content"] = content_
        # print(item)
        yield item