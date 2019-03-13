# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:58:35 2019

@author: vanna
"""

#%%Testing Function
import sys
import numpy as np
path = r'C:\Users\vanna\Desktop\MAT567'
sys.path.insert(0,path)
if path not in sys.path:
    sys.path.append(path) #add the path
path = r"C:\Users\jakeo\OneDrive\Documents\M467\Data\current.csv"
#convert all data strings to floating point numbers
def convertData(dataString):
    #INPUT: data line staring from 5th row in string form
    #OUTPUT: data in floating points
    for i in range(len(dataString)):
        dataString[i]=float(dataString[i])
    return dataString
years=[1,2,3,4,5,6,7,8,9]
def countyData(countyList):
    #INPUT: county
    #OUTPUT: year, rate, count
    countyDict={}
    for county in countyList: 
        countyDict.update({county:{'adjCounty':[]}})
        for year in years:
            countyDict[county].update({year:{'rate':[],'count':[]}})
    with open(path) as f:
        next(f)
        next(f)
        next(f)
        next(f)
        line=f.readline()  #Read the 4th line(row)
        lineString=line.split(",")  #split the 4th line(row)
        for record in f:   #goes through every row, starting at 5th row
            dataString = record.split(",") #split data
            data=convertData(dataString)   #convert all data rows to floating points
            for county in countyDict:
                for string in lineString:  #goes through the 4th line(row)
                    if string==county+' '+'rate':
                        position_rate=lineString.index(string)
                    if string==county+' '+'count':
                        position_count=lineString.index(string)
                        for year in years:
                            if data[3]==year:
                                rate=data[position_rate]       #position of county's rate
                                countyDict[county][year]['rate'].append(rate)
                                count=data[position_count]     #position of county's counts
                                countyDict[county][year]['count'].append(count)
    return countyDict
def adjcountyDict(countyList):
    countyDict['BE']['adjCounty']=['RA','SB','MA','CMHD']
    countyDict['BH']['adjCounty']=['YE','TR','CA','RS','PR']
    countyDict['BL']['adjCounty']=['HI','PH']
    countyDict['BR']['adjCounty']=['LC','JE','GA','ME']
    countyDict['CA']['adjCounty']=['PA','YE','BH']
    countyDict['CS']['adjCounty']=['TE','LC','ME','CMHD']
    countyDict['CMHD']['adjCounty']=['YE','RS','GF','PH','BL','CS','ME','SG']
    countyDict['FA']['adjCounty']=['WI','PR','CS']
    countyDict['FL']['adjCounty']=['LI','SA','LA','MS','PW','LC','TE','PO','GL']
    countyDict['GA']['adjCounty']=['MA','JE','BR','ME','PA']
    countyDict['GF']['adjCounty']=['RO','PH','VA','MC','CMHD']
    countyDict['GL']['adjCounty']=['FL','PO','TO']
    countyDict['HI']['adjCounty']=['LI','CMHD','BL']
    countyDict['JE']['adjCounty']=['MA','SB','CMHD','PW','LC','BR','GA']
    countyDict['LA']['adjCounty']=['MS','SA','FL','PW']
    countyDict['LC']['adjCounty']=['FL','TE','CS','ME','BR','JE','PW']
    countyDict['LI']['adjCounty']=['TO','PO','CMHD','HI']
    countyDict['LN']['adjCounty']=['FL','SA']
    countyDict['MA']['adjCounty']=['BE','SB','JE','GA']
    countyDict['MC']['adjCounty']=['GF','VA','RO','RI','CMHD',]
    countyDict['ME']['adjCounty']=['LC','CS','SG','PA','GA','BR']
    countyDict['MI']['adjCounty']=['SA','MS']
    countyDict['MS']['adjCounty']=['MI','SA','LA','FL','PW','RA']
    countyDict['PA']['adjCounty']=['GA','ME','SG','CA']
    countyDict['PH']['adjCounty']=['BL','GF','VA']
    countyDict['PO']['adjCounty']=['GL','FL','TE','CMHD','LI','TO']
    countyDict['PR']['adjCounty']=['BH','RS','CMHD',]
    countyDict['PW']['adjCounty']=['CMHD','MS','FL','LC','JE']
    countyDict['RA']['adjCounty']=['MS','CMHD','BE']
    countyDict['RI']['adjCounty']=['RO','MC','CMHD','WI']
    countyDict['RO']['adjCounty']=['SH','CMHD','VA','MC','RI']
    countyDict['RS']['adjCounty']=['GF','TR','BH','PR','CMHD']
    countyDict['SA']['adjCounty']=['LN','FL','LA','MS','MI']
    countyDict['SH']['adjCounty']=['CMHD','RO']
    countyDict['SB']['adjCounty']=['JE','CMHD','BE','MA']
    countyDict['SG']['adjCounty']=['PA']
    countyDict['TE']['adjCounty']=['PO','CMHD','CS','LC','FL']
    countyDict['TO']['adjCounty']=['GL','PO','LI']
    countyDict['TR']['adjCounty']=['RS','BH','YE']
    countyDict['VA']['adjCounty']=['PH','GF','MC','RO','CMHD']
    countyDict['WI']['adjCounty']=['RI','CMHD','FA']
    countyDict['YE']['adjCounty']=['CA','TR','BH']
    return countyDict
countyList=['BE','BH','BL','BR','CA','CS','CMHD','FA','FL','GA','GF','GL','HI',
          'JE','LA','LC','LI','LN','MA','MC','ME','MI','MS','PA','PH','PO','PR','PW',
          'RA','RI','RO','RS','SA','SH','SB','SG','TE','TO','TR','VA','WI','YE']
countyDict=countyData(countyList)
countyDict=adjcountyDict(countyList)
#%%Weighting function

#%% K-Nearest Exponential Function
def kNearest(predictionDict,countyList,years):
    #INPUT:Numver of nearest weeks:k
    #OUTPUT: prediction counts for 
    for county in countyList:
        for year in years:
            counts=countyDict[county][year]['count']
            for j in range(1,len(counts)+1):
                weightedCount=0
                ysum=0
                alpha=1-(0.01)**float(1/j)
                for i in range(1,j+1):
                    weight=alpha*(1-alpha)**(i-1) #exponential weights of each count
                    weightedCount+=weight*countyDict[county][year]['count'][j-i]
                    ysum+=countyDict[county][year]['count'][j-i]
                ybar=ysum/len(range(1,j+1))
                predictionDict[county][year]['count'].append(weightedCount)
                predictionDict[county][year]['ybar'].append(ybar)
    return weightedCount,ybar,predictionDict
#%%K-Nearest COnventional Function
def kNearestCon(predictionDict,countyList,years):
    #INPUT:Numver of nearest weeks:k
    #OUTPUT: prediction counts for 
    for county in countyList:
        for year in years:
            counts=countyDict[county][year]['count']
            k=3           #number of nearest weeks to predict week k+1
            for j in range(1,k+1):   #start to predict from week 2
                weightedCount=0
                ysum=0
                alpha=1-(0.01)**float(1/j)
                for i in range(1,k+1):
                    weight=alpha*(1-alpha)**(i-1) #exponential weights of each count
                    weightedCount+=weight*countyDict[county][year]['count'][k-i]
                    ysum+=countyDict[county][year]['count'][k-i]
                ybar=ysum/len(range(1,k+1))
                predictionDict[county][year]['count'].append(weightedCount)
                predictionDict[county][year]['ybar'].append(ybar)
            for j in range(k+1,len(counts)+1):   #start to predict from week k+1(6)
                weightedCount=0
                ysum=0
                alpha=1-(0.01)**float(1/k)
                for i in range(k):
                    weight=alpha*(1-alpha)**(i) #exponential weights of each count
                    weightedCount+=weight*countyDict[county][year]['count'][j-i-1]
                    ysum+=countyDict[county][year]['count'][j-i-1]
                ybar=ysum/len(range(k+1,len(counts)+1))
                predictionDict[county][year]['count'].append(weightedCount)
                predictionDict[county][year]['ybar'].append(ybar)
    return weightedCount,ybar,predictionDict
#%%Run k-nearest exponential function
predictionDict={}
for county in countyList:
    predictionDict.update({county:{}})
    for year in years:
        predictionDict[county].update({year:{'rate':[],'count':[],'ybar':[]}})
weightedCount,ybar,predictionDict=kNearest(predictionDict,countyList,years)
#weightedCount,ybar,predictionDict=kNearestCon(predictionDict,countyList,years)
#%%plotting different alpha's           
import matplotlib.pyplot as plt 
#alpha=0.7               
x=[i for i in range(1,len(countyDict['FL'][4]['count']))]    #weights from week 41 to 1
z=[i for i in countyDict['FL'][4]['4count'][1:]]
y=[i for i in predictionDict['FL'][4]['count'][:-1]]   
ybar=[i for i in predictionDict['FL'][4]['ybar'][:-1]]   
plt.plot(x,y,'bo-')
plt.plot(x,z,'ro-')
plt.plot(x,ybar,'go-')
#%%
