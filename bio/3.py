#coding=utf-8 
import re
import matplotlib.pyplot as plt
import numpy as np
import copy

length = 10
total = 0
genC='C'
genG='G'
countGC=0
x=[]# 单个样本数量
y=[]# 总的样本数量
z=[]# 概率
count = 0

'''文件读安行读取防止文件过大'''
with open("test.data") as infile:
    '''读取每行按照规定的窗口的大小去读取对于存在有不足窗口的字段留到下次处理'''
    temp=''
    for line in infile:
        line = line.strip()
        if line.startswith('>'):
            '''存在不足的窗口'''
            count = count+1
            if count == 25 :
                break
            tempcountGC=temp.count(genC)+temp.count(genG)
            x.append(tempcountGC)
            countGC= tempcountGC +countGC
            total = total + len(temp)
            if total :
                z.append(float(countGC)/total)#概率
                countGC = 0
                total = 0
                if x :
                    y.append(copy.deepcopy(x))
                    x=[]
                    temp =''
            continue
        line = temp.strip()+line
        readSize = len(line)
        nTime = readSize / length
        '''按照指定窗口分割'''
        b=re.findall(r'.{'+str(length)+'}',line[0:nTime*length]) 
        for element in b:
             tempcountGC=element.count(genGC)
             countGC = tempcountGC +countGC
             total = total + length
             x.append(tempcountGC)
        temp=line[nTime*length:readSize]

#概率直方图
#个人的观点
#样本的数应该是GC的数量
print z
plt.hist(z,bins=length,color='green',normed=True)# bins显示有几个直方,normed是否对数据进行标准化
plt.show()