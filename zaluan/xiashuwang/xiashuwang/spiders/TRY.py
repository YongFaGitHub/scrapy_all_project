# -*- coding: utf-8 -*-
import re
a = "wwＷ．ｘｉａｂｏｏｋ.com下书网,Www.dfsf.com,wwＷ．ｘｉａｂｏｏｋ.coM"
#
b = re.findall("([wW].*?[Mm])",a,re.S)
# for c in b:
#     a = a.replace(c,"")
#     print(a)
#
# print(b)
print(b,"@@@@@@@2")
t = "WWW.xiAbook.com下~书- 网"
result = re.findall("([Ｗw].*?[ＭMm])", t,re.S)
# print(result)