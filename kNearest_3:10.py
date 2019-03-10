#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:24:59 2019

@author: Cassidy
"""

'''To get this code to work for you:
    1. reset paths to your own machine's flu folder
    2. make a new folder in the flu folder called ModuleDir
    3. insert the script functions.py into ModuleDir
    
'''

#Testing Function
import sys
#import numpy as np
path = '/Users/Cassidy/Desktop/Flu_project'
sys.path.insert(0,path)
if path not in sys.path:
    sys.path.append(path) #add the path
path = '/Users/Cassidy/Desktop/Flu_project/current.csv'

path = r'/Users/Cassidy/Desktop/Flu_project'
if path not in sys.path:
    sys.path.append(path)
from ModuleDir import functions

'''Van's K Nearest Neighbors Functions'''

years=[1,2,3,4,5,6,7,8,9]

countyList=['BE','BH','BL','BR','CA','CS','CMHD','FA','FL','GA','GF','GL','HI',
          'JE','LA','LC','LI','LN','MA','MC','ME','MI','MS','PA','PH','PO','PR','PW',
          'RA','RI','RO','RS','SA','SH','SB','SG','TE','TO','TR','VA','WI','YE']
countyDict = functions.countyData(countyList)
countyDict = functions.adjcountyDict(countyList)


#Run k-nearest exponential function
k=4  #number of weeks that has rate closest to predictor week
alpha=1/k;
#create an empty prediction dictionary
predictionDict={}
for county in countyList:
    predictionDict.update({county:{}})
    for year in years:
        predictionDict[county].update({year:{'rate':[],'count':[],'ybar':[]}})
sumWeight,ybar = functions.kNearest(alpha,k,predictionDict)

#plotting different alpha's           
import matplotlib.pyplot as plt 
#alpha=0.7               
x=[i for i in range(1,len(countyDict['CMHD'][4]['count']))]    #weights from week 41 to 1
z=[i for i in countyDict['CMHD'][4]['count'][1:]]
y=[i for i in predictionDict['CMHD'][4]['count'][:-1]] 
ybar=[i for i in predictionDict['CMHD'][4]['ybar'][:-1]]
plt.plot(x,y,'bo-')
plt.plot(x,z,'ro-')
plt.plot(x,ybar,'go-')

#Create csv file
import csv
firstRow=['year']
for county in countyList:
    firstRow.append(county+' count')
    firstRow.append(county+' pred count')
csv_file = r'/Users/Cassidy/Desktop/Flu_project/output_kNearest.csv'
kNearestDict=[]
for year in years:
    for i in range(len(predictionDict['BE'][year]['count'])):
        kNearestDict.append({firstRow[0]:year})
newData=[]
for county in countyList:
    newData=[]
    for year in years:
        for i in range(len(predictionDict[county][year]['count'])):
            newData.append({county+' pred count':predictionDict[county][year]['count'][i]})
#newData=[]
#for i in range(len(predictionDict)):
#    for year in years:
#        for county in countyList:
#            newData.append({county+' pred count':predictionDict[county][year]['count'][i]})
with open(csv_file,'w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=firstRow)
    writer.writeheader()
    for data in kNearestDict:
        writer.writerow(data)
    for data in newData:
        writer.writerow(data)