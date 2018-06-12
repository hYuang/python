# -*- coding: utf-8 -*-
import re


#注释符号
commentSymbol="#"
#表头
tableHeadList = []
#表头标识符
tableHeadSymbol = "CHROM"
#数据的统计
dataMap = {}
#数据的输出列表
dataList = []

with open("./test.txt") as infile:
    for line in infile:
        line = line.strip()
        lines = line 
        #去除注释行
        if ( line.startswith(commentSymbol)):
            continue 
        
        if ( line.startswith(tableHeadSymbol)):
            continue
        #数据行
        line = re.split("\s+",line)
        dataLine = line[20:26]
        for element in  dataLine:
            if (element != '.'):
                if (float(element) < 1  and float(element) > 0) :
                    dataList.append(line)
                    break
            
                

f=open('newtest.vcf', 'w') 

with open("./test.vcf") as infile:
    for line in infile:
        line = line.strip()
        #去除注释行
        if ( line.startswith(commentSymbol)):
            f.write(line)
            f.write('\n')
            continue 
        
        if ( line.startswith(tableHeadSymbol)):
            f.write(line)
            f.write('\n')
            continue
        #数据行
        lineList = re.split("\s+",line)
        flag = False
        for i  in range(len(dataList)):
            data = dataList[i]
            for j in range(1,5):
                if ( j < 5 ) :
                    if ( j != 2) :
                        if (data[j] != lineList[j]):
                            flag = True
                            break
                    else :
                        pass
            break
        if not flag :
            f.write(line)
            f.write('\n')

f.close()


