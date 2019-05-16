import re
a = "（实习编辑：叶洁斯）"


b = re.findall("(（.*?：.*?）)",a)
if len(b) !=0:
    print(b[0])
else:
    print("wu")