#encoding=utf-8
import re
#
# a = "律表\n┌────┬──────┬──────┐在\n │年支│司天│在泉│\n├────┼──────┼──────┤\n│子午│少阴君火│阳明燥金│\n│丑未│太阴湿土│太阳寒水│\n│寅申│少阳相火│厥阴风木│\n│卯酉│阳明燥金│少阴君火│\n│辰 戌│太阳寒水│太阴湿土│\n│巳亥│厥阴风木│少阳相火│\n└────┴──────┴──────┘\n司天丑未│太阴湿土│太阳寒水│\n│寅申│少阳相火│厥阴风木│\n│卯酉│阳明燥金│少阴君火│\n│辰 戌│太阳寒水│太阴湿土│\n│巳亥│厥阴风木│少阳相火│\n└────┴──────┴──────┘\n司"
#
# b = re.f
#
# indall(r"\n(.*[\┘\┐])\n",a,re.S)
# print(b)


# pattern="(\d+)(.*?)(\d+)"
pattern="\d+(?P<Tag>，)\d+"
a = "17，14个鸡，鸡78，90"

# b = re.findall("\d+(.*?)\d+",a,re.S)
# re.split("\d+(.*?)\d+",a,re.S)

# b = re.findall("\d(，)\d",a,re.S)
# re.

# print(b)
def d(m):
    v=m.group("Tag")
    v=","
    return v

newUrl=re.sub(pattern,d,a)
print(newUrl)