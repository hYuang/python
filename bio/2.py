import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm 
def draw_heatmap(data,xlabels,ylabels):
    cmap = cm.Blues    
    figure=plt.figure(facecolor='w')
    ax=figure.add_subplot(2,1,1)
    ax.set_yticks(range(len(ylabels)))
    ax.set_yticklabels(ylabels)
    ax.set_xticks(range(len(xlabels)))
    ax.set_xticklabels(xlabels)
    vmax=data[0][0]
    vmin=data[0][0]
    for i in data:
        for j in i:
            if j>vmax:
                vmax=j
            if j<vmin:
                vmin=j
    map=ax.imshow(data,interpolation='nearest',cmap=cmap,aspect='auto',vmin=vmin,vmax=vmax)
    cb=plt.colorbar(mappable=map,cax=None,ax=None,shrink=0.5)
    plt.show()

mu = 6
sigma = 10
sampleNo = 40
dim = 4
samples = sigma*np.random.randn(dim,sampleNo)+mu

a=np.random.rand(10,10)
xlabels=['-13','-12','-11','-10','-9','-8','-7','-6','-5','-4','-3','-2','-1','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
ylabels=['a','b','c','d']
draw_heatmap(samples,xlabels,ylabels)
print samples
