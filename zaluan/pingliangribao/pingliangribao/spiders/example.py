# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,FormRequest
import re
import time

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['plxww.com']
    start_urls = []

    def start_requests(self):
        url = "http://www.plxww.com/sitefiles/services/cms/search/output.aspx?publishmentSystemID=1"

        for i in range(19):
            data = {
                "channelID": "1",
                "word": "%E5%90%95%E5%A8%85%E8%8E%89",
                "pageIndex": "{}".format(i),
                "ajaxDivID": "ajaxElement_2_262",
                "charset": "utf-8",
                "dateAttribute": "AddDate",
                "isDefaultDisplay": "False",
                "isRedirectSingle": "False",
                "isHighlight": "True",
                "pageNum": "0",
                "successTemplateString": "bvITd7yMIxcIOm8ZUD4UFWff95Z7hY9WBo20add0IpFwbgobijxL2Ea2Gy0add0AQKhAJcpc7eF1GFy00add0rAIx1hrZMbX9893FIalmsJ95RHuX5NjsOv2kVYSSVxQOtY77OAJVaEbmuglfUq5QE4uGhP177p0slash0Hpg16ZZWMvDhKQyI0wKZUEpesI0yDCC2fkZnDKQcWEZ0slash0OdDYoabmOVNzWAexU27lyAszzglFhjT1cJrMIN5No9bgXMZPkUVXVaSTHD2s7iMrwdpNUqivV0slash0axEXOTnjemZhHTZBBkL978zMsHlpPHYaQYNr4JL8o0add0xL4PeunRpQqZsy5CA4ann42lZeAhTzVJ5rcHVe0add0Xf0KYQA7XlUYRn5RY6ij5dRqAVgl5e5FEPymI7box0slash0pWLnXG0OhdLoiZy30slash0OYfw0slash0h9BotN0swNJXzkHAw7JvUjcK6fAXIeM9qZeC2HW0add0bWlDDGh2SZ0add0OZV89wJFerEXHrQ6fk37Ljs1VhOhhc0EYiE1zAy2roI1bkeE0slash0Bjv4ddyweUkBN3rpUdvHdIWdOrOuaIGXwLb4P1e0slash0V8HQo0tbp37GTmXLMKCvBQcccJVf4LmTt0slash0zUo0add0fccJevXUqcro0add0DouhWTJ9gpE3pKEdmMwHkLSBQFu4NV6AwmnIDBxCYHh04CAwaNhgYqbS0add0O9jzujTsOW1FP0euHS6FKWlXymDBI9VRrP0add0dfIuWC10add0G444Z0slash0P9OFHVtQo0slash0hYbwicEJCiRKayFbchvgf4Fw7kk1KO0zWVNRfws9NbgECVTKnapW8hSmq18XlK0slash08kFysY3sEzEP0slash0nKBhAZjEzS6TdUcTrjEwXEFdrNlYRpO5Fzs2SIZApokmq44MS6skbm6KrLg2kGjl2yNyrbYFZ0RhU0slash0UpbFuPVm3B3TAMt5eSjLpSDVGiH0WfngiVmzO2btzzzm3Y45DEBObq30QqqiloiwFoUcXX4d0slash0Q0add0y4ls2Eh4pIlLh4bqtYItBC0add0dbUG5YsNn8z0add0WfXi44HB1EwQVuC0add05ngXPIu0slash0Td9Q3qQ6oqRA1aFt7kUNNc0F4zZ2sOZ9hPd85OS7mZQWLJ1n7EdFfSMhjeZ0slash0WlY62VR3tySbYaN0add0d8BURIeQv4IdJ7cg7W8WRQyM0ipAcBSY1q8tzDCNAv1rh9XL10slash07k1wY6DomydOMrixDwAXUmsgHQps20slash0YtbbdpRETqijgw70k9b0slash02DiVrdm2mD0slash0tw5vh6Y64nuzqdpLqL5XvcotpMVHtu6KKmNZBd3mfXLnmp5e6Qagmli0slash00add0MmyWOe3kRpBNzoXaHjIUl0slash0dUOUwdvW7c24GXfpJBrRkdeOJw5nBr335tDYgcayd2t7SfChC0slash0sC94lwNhSgVvYL0XqNznrapyX0add0UNJmGa16qK0slash0xWU9VysBnTyS5lqI4cos6GQeO1qWaq9bg7X5tZJtr1iC7ELuRoH1FLg0slash0XD8ot6z0slash06O23sAv7MDnOy5D2ELsTatPTcRby6rIFPjrzuymO0QCT30slash0he7fGGub3NwbfkX2vWOBE1MTFQf1SWtcPcpYrqRqRBSg31dTWvwmXZJqegXBwBLm8TllbWBBqDcIHb1B7uHS1xbW0kHwpV64xLIpxRliZgX2deoQmoHt2Dw5J0add0wGghfrYztOuvrGrIOubPCRpuWDgAADYsZ2gQgcrkad0add0qc5j9FvYiEPi0add0dQo0M1bMCBEo6X0slash0vCcTEDBiYt0slash0yUlMMQ7sdliDg0equals00equals0",
                "failureTemplateString": "dRnRj1IC07Ha0slash0ZFwL0slash0PpV0slash0oIJa7l1ntowYmueDRnpJPBtDtr469WQ1uYVDFHo3NNkWZsJPOomw6nK6FG4G0slash0IKXGSwAtfzDrZEItIpBhmRAiX4qx5WgEzV4dy5dXBwUiN16jeS9EUQelU8TI30slash001xR3gILDBj0add0yQeNmtvhzlMnz86z6nMUYrxinkXvvgAQsb57x5ABTDNjroD6EDThHRfbYF0add0pAfMC9LwNwLZcVmBJm1Kj8Ty1MLmPSffIGDobas0add02uVln6zTxdOIHTx8qMUO6CHXJxcFwKWCZJ6VYyKDcHWIf2CkIeaVhCNoLjsH2PWJXi6pqbDnGzfGQphCi8z5oFcLcCU2eEFR9ZoEbo7SD1Rqa1Ye7KPTfiC8Ri4YQNGbkzZWGoS1Vdgu4ZDL5o4Jlc1DWpa1GLo0add0ht4gTKplFHYh464L27o80add0HdXF0add0aKZ1572KSUnv5Z0add0SzpLb10rIWZCgVxxIGCcur30sbUruOaT6pYdVX0mgyXCl7BCiMA7l70Exm6cROQiwEZLbTkZvkSqndirLip6hGQYrJBExlbkNGXaf0RPdkJT0slash090slash00slash0WxYu0add0E9XMiegsKeCRdLJDF61n7rFltQq6ZiW18gr33tvjjWWTXLJHE2AhE0add0lEWUr8GwFmQMSbeD2h8pvUDTh3N2cncW5KcvLuCN0slash0tX5essBN4EHijAXOJ0scTdqwczmw7h0slash0WyW0cI33XTZwkra3YPnVGC7VgOMjtebuMmOy5DJgBOncmaaizrXw4Vw2NZnhPy27c5L3j2LQof3UtpY2Yf7tBpcL8vaN0O0slash0eMuq0add01jLpGKt4XtcMAIxpComFMa1fVn2B5X5BtBk5IX5qm0VCcOSEPK4IlFJvuk7NI8C2IplQ5yd8Gy00equals0"
            }

            time.sleep(2)
            yield FormRequest(url, callback=self.parse, dont_filter=True, formdata=data)

    def parse(self, response):
        href_list = re.findall('<p class=\"search_title\"><a href=\"(.*?)\"', response.body.decode())

        for href_raw in href_list:
            href_url = "http://www.plxww.com" + href_raw
            time.sleep(2)
            yield Request(href_url, callback=self.parse_dis, dont_filter=True)

        # href_url = "http://www.plxww.com/contents/pl/pl20190108493254.html"
        # yield Request(href_url, callback=self.parse_dis, dont_filter=True)


    def parse_dis(self, response):

        title_s = response.xpath("//div[@class='contentbox']/h2/text()").extract()
        title = str(title_s).replace("['", "").replace("']", "").replace("\\u3000",
                "").replace(' ', "").replace("\\", "").replace("/", "").replace(":", "").replace("*",
                "").replace("?", "").replace("<", "").replace('>', "").replace("→", "").replace("|", "")

        tim_raw = response.xpath("//div[@class='tim']/text()").extract()
        time_a_raw = re.findall("时间：(.*?)来源", str(tim_raw))
        time_a = str(time_a_raw).replace("['", "").replace("']", "").replace("\\\\u3000", "")

        title_time = time_a + "_" + title



        p_list = response.xpath("//div[@class='content']/p")
        for p in p_list:
            text_raw = p.xpath('.//text()').extract()
            text = str(text_raw).replace("['", "").replace("']", "").replace("\\u3000",
                                 "").replace("\\xa0", " ").replace(" ", "").replace("[", "").replace(']', "")
            if len(text) > 0:
                with open("H:/新闻new/{}.txt".format(title_time), "a+", encoding="utf-8") as f:
                    f.write(text)
                    f.write("\n")


