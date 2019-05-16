import csv

file = open("./jian.txt","r")
file2 = open("./fan.txt","r")

read = csv.reader(file)
read2 = csv.reader(file2)

a = ""
b= ""
for line in read:
    a = line[0]

for line2 in read2:
    b = line2[0]

print(a)
print(b)
with open("./all.txt","a+",encoding="utf-8") as f:
    f.write("{")
if len(a) == len(b):
    for i in range(len(a)):

        with open("./all.txt","a+",encoding="utf-8") as f:
            f.write("'")
            f.write(b[i])
            f.write("'")
            f.write(":")
            f.write("'")
            f.write(a[i])
            f.write("'")
            f.write(",")

with open("./all.txt","a+",encoding="utf-8") as f:
    f.write("}")