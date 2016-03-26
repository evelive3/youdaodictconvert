# 有道生词本导出转换工具
#  author Jing @ SYSU
#

import xml.etree.ElementTree

youdaoxml = "word.xml"  # youdaodict 导出的xml格式生词本
fileoutput = "word.txt" # 导出的文件名

e = xml.etree.ElementTree.parse(youdaoxml).getroot()
f=open(fileoutput,"w")
for item in e.findall("item"):
    print(item.find("word").text)
    f.write(item.find("word").text + "\n")
f.flush()
f.close()