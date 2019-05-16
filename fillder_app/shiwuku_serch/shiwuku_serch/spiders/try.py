# import csv
# file = open("./food_list.csv", "rt",
#             encoding="utf-8")
#
# file2 = open("./name.txt", "rt",
#             encoding="utf-8")
# read2 = csv.reader(file2)
# read = csv.reader(file)
# list = []
# for line in read:
#     list.append(line[0])
#
#
# for line2 in read2:
#     if line2[0] not in list:
#         with open("./no.txt","a+",encoding="utf-8") as f:
#             f.write(line2[0] + "\n")