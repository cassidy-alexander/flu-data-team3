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
#%% K-Nearest Exponential Function
def kNearest(alpha,k,predictionDict):
    #INPUT:Numver of nearest weeks:k
    #OUTPUT: prediction counts for 
    for county in countyList:
        for year in years:
            counts=countyDict[county][year]['count']
            for j in range(1,len(counts)+1):
                sumWeight=0
                ysum=0
                for i in range(1,j+1):
                    weight=alpha*(1-alpha)**(i-1) #exponential weights of each rate
                    weightedCount=weight*countyDict[county][year]['count'][j-i]
                    sumWeight += weightedCount    #sum of weighted counts
                    ysum+=countyDict[county][year]['count'][j-i]
                ybar=ysum/len(range(1,j+1))
                predictionDict[county][year]['count'].append(sumWeight)
                predictionDict[county][year]['ybar'].append(ybar)
    return sumWeight,ybar
#%%Run k-nearest exponential function
k=4  #number of weeks that has rate closest to predictor week
alpha=1/k;
#create an empty prediction dictionary
predictionDict={}
for county in countyList:
    predictionDict.update({county:{}})
    for year in years:
        predictionDict[county].update({year:{'rate':[],'count':[],'ybar':[]}})
sumWeight,ybar=kNearest(alpha,k,predictionDict)
#%%plotting different alpha's           
import matplotlib.pyplot as plt 
#alpha=0.7               
x=[i for i in range(1,len(countyDict['CMHD'][4]['count']))]    #weights from week 41 to 1
z=[i for i in countyDict['CMHD'][4]['count'][1:]]
y=[i for i in predictionDict['CMHD'][4]['count'][:-1]] 
ybar=[i for i in predictionDict['CMHD'][4]['ybar'][:-1]]
plt.plot(x,y,'bo-')
plt.plot(x,z,'ro-')
plt.plot(x,ybar,'go-')
#%%Create csv file
import csv
firstRow=['year']
for county in countyList:
    firstRow.append(county+' count')
    firstRow.append(county+' pred count')
csv_file=r'C:\Users\vanna\Desktop\MAT567\data567\output_kNearest.csv'
kNearestDict=[]
for year in years:
    for i in range(len(predictionDict['BE'][year]['count'])):
        kNearestDict.append({firstRow[0]:year})
#newData=[]
#for county in countyList:
#    newData=[]
#    for year in years:
#        for i in range(len(predictionDict[county][year]['count'])):
#            newData.append({county+' pred count':predictionDict[county][year]['count'][i]})
newData=[]
for i in range(len(predictionDict)):
    for year in years:
        for county in countyList:
            newData.append({county+' pred count':predictionDict[county][year]['count'][i]})
with open(csv_file,'w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=firstRow)
    writer.writeheader()
    for data in kNearestDict:
        writer.writerow(data)
    for data in newData:
        writer.writerow(data)
#%%Testing
csv_columns = ['No','Name','Country']
dict_data = [
{csv_columns[0]: (2,1), 'Name': 'Alex', 'Country': 'India'},
{'No': 2, 'Name': 'Ben', 'Country': 'USA'},
#{'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
#{'No': 4, 'Name': 'Smith', 'Country': 'USA'},
#{'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
]
newData=[{'Name': 'Shri Ram', 'Country': 'India'}]
dict_data.append({'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'})
csv_file = "C:/Users/vanna/Desktop/output.csv"
with open(csv_file, 'w',newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)
    for data in newData:
        writer.writerow(data)
#%%
import csv
path = "C:/Users/vanna/Desktop/silly.csv"
my_dict = {'1': 'aaa', '2': 'bbb', '3': 'ccc'}
with open(path, 'w') as f:
    for key in my_dict.keys():
        f.write("%s,%s\n"%(key,my_dict[key]))