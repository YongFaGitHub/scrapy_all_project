# import csv
# import  re
# file = open("H:/pycharmproject/project/zaluan/dedao/dedao/spiders/FIDDLER2.txt","rt",encoding="utf-8")
# read = csv.reader(file)
# for line2 in read:
#     if len(line2)>1:
#         # line = str(line2)
#         # re.findall("")
#         for i in line2:
#             print(i)
#             if  "mp3_play_url" in i :
#
#                 print(i)
#

test = "\u674e\u7fd4\u77e5\u8bc6\u5185\u53c2"
test.encode('utf-8').decode('unicode_escape')
print(test)