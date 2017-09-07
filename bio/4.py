#coding=utf-8 
import re

genC='C'
genG='G'
countGC=0
x=[]#
with open("test1.txt") as infile:
    for line in infile:
        line = line.strip()
        #匹配多个空格
        if line == '':
            continue
        dataList = re.split("\s+", line)
        column6 = dataList[5]
        matchLen = 0
        if column6.count('M'):
            #匹配数字
            mFlag = len(re.split("[M]\d+", column6))
            matchLen = re.split("M", column6)[0]
            if mFlag > 1 or  not matchLen.isdigit() :
                continue
            #处理第十列的数据
            countGC = dataList[9].count(genC)+dataList[9].count(genG)
            x.append(float(countGC)/float(matchLen))

output= open('output','w')
output.write("".join("%f\n" % n for n in x))
output.close()       

