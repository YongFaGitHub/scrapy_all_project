import requests
from lxml import etree
url = 'http://www.a-hospital.com/w/%E5%AD%90%E5%AE%AB%E9%A2%88%E5%B9%B3%E6%BB%91%E8%82%8C%E7%98%A4'
r = requests.get(url)
body = etree.HTML(r.content)
div_list = body.xpath("//div[@id='bodyContent']")[0]
p = etree.tostring(div_list).decode()
qq = ['<h2>'+i for i in p.split('<h2>')if i]
for i in qq:
    c_list = etree.HTML(i.strip())
    h2 = c_list.xpath('//h2/span/text()')
    h3 = c_list.xpath('//h3//text()')
    print(h3)
    p = c_list.xpath('//p//text()')
    print(h2)
    print(p)
    print('-'*20)