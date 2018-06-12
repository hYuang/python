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
        #去除注释行
        if ( line.startswith(commentSymbol)):
            continue 
        
        if ( line.startswith(tableHeadSymbol)):
            tableHead = re.split("\s+", line)
            tableHeadList = tableHead[:4]
            continue
        #数据行
        elementList = []
        elementList = re.split("\s+", line)
        #DP4数据列获取
        freqList = re.split(";", elementList[31])
        #DP4数据获取
        DP4String  = freqList[-2]
        #DP4数据集
        DP4_list= re.split("=",DP4String)[-1].split(",")
        #DP4精度换算
        DP4_list=[ float(x) for x in DP4_list]
        #DP4频率计算
        freq=(DP4_list[2]+DP4_list[3])/sum(DP4_list)
        #CHROM	POS		REF	ALT
        gene_position = elementList[:5]
        del gene_position[2]

        #频率列
        freStr = str(round(freq,3))
        gene_position.append(freStr)
        #存在相同的基因则取出并且count加1 同时添加最大值 最小值
        genKeyId = gene_position[:4]
        genKey = ",".join(genKeyId)
        if ( dataMap.has_key(genKey)) :
            for element in dataList :
                listId = element[:4]
                listKey = ",".join(listId)
                if (listKey == genKey) :

                   fre = element[-1]+","+freStr
                   element[-1] = fre
                   continue
        else:
            dataMap[genKey] = gene_position[-1]
            dataList.append(gene_position)
     



 
tableHeadList.append("count")
tableHeadList.append("min")
tableHeadList.append("max")
f=open('newfile', 'w')

for headElement in tableHeadList :
    f.write(headElement)
    f.write("\t")
f.write("\n")

for element in dataList :
    for data in element :
        f.write(str(data))
        f.write("\t")
    freInfo = str(element[-1])
    freInfoList = freInfo.split(",")
    f.write(str(len(freInfoList)))
    f.write("\t")
    f.write(min(freInfoList))
    f.write("\t")
    f.write(max(freInfoList))
    f.write("\n")

f.close()


