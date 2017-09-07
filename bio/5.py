#coding=utf-8 
import re
import copy

genC='C'
genG='G'
countGC=0
count = 0
x=[]#
standardGen =[]
sampleGen = ''
count = 0
output = []
y=[]

#样本筛选外显子
with open("text2.txt") as infile:
    for line in infile:
        line = line.strip()
        #匹配多个空格
        dataList = re.split("\s+", line)
        #个数
        column9 = dataList[8]
        #开始长度
        column10 = (dataList[9].strip(',')).split(',')
        #终止位置
        column11 = (dataList[10].strip(',')).split(',')
        #染色体
        column2 = dataList[2]
        
        exonList = list(map(lambda x: int(x[0]) - int(x[1]),zip(column11,column10)))
        maxExonIndex = exonList.index(max(exonList))
        #[染色体，起始位置，结束位置,个数,长度]
        result = [column2,column10[maxExonIndex],column11[maxExonIndex],column9,exonList[maxExonIndex]]
        y.append(max(exonList))
        x.append(result)

#行间比较
maxLineIndex = y.index(max(y))
x= x[maxLineIndex]
genInt = int(chr[3:])

with open("test.data") as infile:
    for line in infile:
        line = line.strip()
        if line == '':
            continue
        if line.startswith('>'):
            line = '>'
            count = count +1
            if  count > 24 or count > genInt :
                break
        if count == genInt :
            sampleGen= line +sampleGen

standardGen = sampleGen.strip('>').split('>')

for element in  x:
    chr = element[0]
    chrInt = int(chr[3:])
    begin = int(element[1])
    end = int(element[2])
    genLen = int(element[3])
    gen = standardGen[chrInt-1][begin:(end+1)]
    countGC = gen.count(genC)+gen.count(genG)
    output.append(float(countGC)/genLen)

output= str(output).replace('[','').replace(']','')
outputData= open('outputdata','w')
outputData.write(output)
outputData.close()   

    





