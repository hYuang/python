#coding=utf-8 

#存在编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

mu = 6
sigma = 10
sampleNo = 40
dim = 4
samples = sigma*np.random.randn(dim,sampleNo)+mu
temp=open('txt','w')
temp.write(str(samples))
temp.close()

plt.style.use("ggplot")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif']=['SimHei']

df=pd.DataFrame()

for i in range(len(samples)):
    df["sample"+str(i)] = samples[i]

pp = PdfPages('test.pdf')
f=plt.boxplot(x=df.values,labels=df.columns)
plt.xlabel("标准差")
plt.ylabel("样本")
plt.title("箱图")
color = ['r','g','y','b']
for box in f['boxes']:
    colors = color.pop()
    box.set(color=colors)
pp.savefig()
pp.close()

