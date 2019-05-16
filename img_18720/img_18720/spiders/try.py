import csv
file = open("./img.txt","rt")
read = csv.reader(file)
list = []

for line in read:
    list.append(line[0])

list2 = set(list)
for i in list2:
    with open("./img_all.txt","a+",encoding="utf-8") as f:
        f.write(i)
        f.write("\n")

# print(len(list2))


