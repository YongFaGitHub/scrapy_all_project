# import re
# a = '大麦+红糖=辅助治疗腹泻大麦+羊肉=暖脾胃，祛腹胀大麦+南瓜=补虚养身大麦+豌豆=降低血糖大麦+红枣=促进营养吸收相克大麦+牛奶=不利于营养吸收'
# for i in range(len(a.split('相克'))):
#     c = re.sub(r'大麦', ' 大麦', a.split('相克')[i])
#
#     if i == 0:
#         print('相宜')
#     else:
#         print('相克')
#     for j in c.split(' '):
#         if j:
#             print(re.split(r'\+|=',j))