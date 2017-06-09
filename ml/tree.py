from math import log

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] +=1
    shannoEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannoEnt -= prob*log(prob,2)
    return shannoEnt

def createDataSet():
    dataSet = [[1,1,'yes'],[1,0,'yes'],[0,1,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels

def splitDataSet(dataSet,axis,value):
    retDataSet = []
    for featVec in dataSet:
        reducedFeatVec =  featVec[:axis]
        reducedFeatVec.extends(feacVect[axis+1:])
        retDataSet.append(reducedFeatVec)
    return retDataSet