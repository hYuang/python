# coding=utf-8
import re

dataMap = {}
columIndex = 2

with open("sample_stock") as infile1:
    for line in infile1:
        line = line.strip()
        dataList = re.split("\s+", line)
        dataMap[dataList[columIndex]] = line

f = open('output.txt', 'w')

with open("sample_stock.txt") as infile2:
    for line1 in infile2:
        patientCode = line1.strip()
        print patientCode
        '''if dataMap.has_key(patientCode):
            patientInfo = dataMap.get(patientCode)
            print "---"+patientCode
            f.write(patientCode + ' \t' + patientInfo + '\n')
        else :
            f.write(patientCode + ' \t  no information \n')
            print "+++"+patientCode'''

f.close()

