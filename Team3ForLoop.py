# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 14:17:02 2019

@author: annag


team 3
for loop
"""


import matplotlib.pyplot as plt
import numpy as np

path1 = r"C:\Users\annag\Documents\2018-2019\Spring_2019\BigDataProjects\flu-data-linear-regression\initial_flu.csv"
path2 = "/home/mandub/Desktop/6th semester/courses/Data Science Projects/data flu/flu-data-linear-regression/initial_flu.csv"
path3 = r"C:\Users\jakeo\OneDrive\Documents\M467\flu-data-linear-regression\initial_flu.csv"
path4 = r"C:\Users\Bill Griffin\flu-data-linear-regression\initial_flu.csv"



pathlist = [path1, path2, path3, path4]
names = ["Anna", "Mandub", "Jake", "Bill"]
for paths in range(len(pathlist)):
    try:
        with open(pathlist[paths]) as f:#, encoding = "utf-8"
            print ("This is", names[paths])   
            path = pathlist[paths]
            break
    except:
        print("This is not", names[paths])


from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import csv


#################################################
# read from the file and create Data dictionaries
#################################################
#============================================================ Mandub code 
CountyDict = defaultdict(list)
yeardata=defaultdict(list)

CountyRateDict = defaultdict(list)  # Rate
CountyCDict = defaultdict(list)     # C
CountyPopDict = defaultdict(list)   #population
actualNames=[]         # hold the actual county Names for presentation purpose
countyLicenceNumber=[] # hold the actual county Licence Number for presentation purpose
counties=[]              # hold county Shortcut names
countyIndexes=defaultdict(list)       # hold 3 name and indexes for each county 
                                        # first will be for the rate 
                                        # the second will be for C
                                        # the third will be for population
counter = 1     # number of line in the file 
with open(path) as f:
    for line in f:
        if counter == 1: # read the first line in the file
            actualNames = line.split(",")
            actualNames = actualNames[3:] # remove the first 3 elements in the list
            actualNames[-1] = actualNames[-1].rstrip('\n') # remove newline char from last element
            counter +=1
            # need to clean redundant data
            
        elif counter == 2: #read the second line in the file
            countyLicenceNumber= line.split(",")
            countyLicenceNumber    = countyLicenceNumber[3:] # remove the first 3 elements in the list
            countyLicenceNumber[-1] = countyLicenceNumber[-1].rstrip('\n') # remove newline char from last element
            counter +=1
            # need to clean redundant data and convert  to int
            
        elif counter == 3: #read the third line in the file
            counter +=1
            counties = line.split(",")
            counties[-1] = counties[-1].rstrip('\n') # remove newline char from last element
            temp = counties                 # hold the line structure to use the indexes
            counties = counties[3:]
            
            counties2 = []                  # to remove redundant data  
            for county in counties:
                if county not in counties2:
                    counties2.append(county)
            counties = counties2
            
             
            for county in counties:        # add counties indexes to countyIndexes
                indexes= []                    #hold indexes for only one county
# =============================================================================
                CountyRateDict[county]= [] # ...we fill CountyRateDict by counties with empty list for the years
                                           # ....where index zreo will be year 1
                CountyCDict[county]=[]     # ...we fill CountyCDict by counties with empty list for the years
                CountyPopDict[county]= []  # ...we fill CountyPopDict by counties with empty list for the years
# =============================================================================
                for index,value in enumerate (temp):  # if the same county append the index 
                    if county == value:
                        indexes.append(index)
                countyIndexes[county]=indexes 
                
        
        elif counter == 4:               #read the third line in the file
            counter+=1                   # we do not do any thing because this line is headers line     
        else:                            # read the others lines in the file for Data 
            data =line.split(",")
            year = int (data[1]) -1      # to use year as index for Dicts
            weak = int (data[2]) -1      # to use weak as index ofr Dicts

            if weak == 0 :                #newyear start
                for county in CountyRateDict:
                    CountyRateDict[county].append([])   # add new list for the weaks
                    CountyCDict[county].append([])
                    CountyPopDict[county].append([])
                    
                    rateIndex= countyIndexes[county][0] #take the index of rate
                    rate = float (data[rateIndex])
                    
                    CIndex= countyIndexes[county][1] #take the index of C
                    C = int (data[CIndex])
                    
                    popIndex= countyIndexes[county][2] #take the index of population
                    pop = int (data[popIndex])
                    
                    CountyRateDict[county][year].append(rate)
                    CountyCDict[county][year].append(C)
                    CountyPopDict[county][year].append(pop)
                    #repat for othre dict
            else:
                for county in CountyRateDict:
                    rateIndex= countyIndexes[county][0] #take the index of rate
                    rate = float (data[rateIndex])

                    CIndex= countyIndexes[county][1] #take the index of C
                    C = int (data[CIndex])
                    
                    popIndex= countyIndexes[county][2] #take the index of population
                    pop = int (data[popIndex])
                    
                    CountyRateDict[county][year].append(rate)
                    CountyCDict[county][year].append(C)
                    CountyPopDict[county][year].append(pop)
                

#%%   
###################################
# Apply line regulation and create
# prediction dictionary
###################################

predictionDict = defaultdict(list)

for county in counties:                # fill predictionDict with empty list for ecah county 
    predictionDict[county] =[]

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def sklearn_linear_Regression(weeksRateslist):
    Y_hat=np.array(weeksRateslist[-1])
    del weeksRateslist[-1]
    X_hat=np.array([weeksRateslist[-1]])
    x_hat= weeksRateslist[-1]
    del weeksRateslist[-1]
    X = np.array(weeksRateslist)
    del weeksRateslist[0]
    weeksRateslist.append(x_hat)
    Y= np.array(weeksRateslist)
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X.reshape(-1, 1), Y)
    y_pred = regr.predict(X_hat.reshape(1, -1))    
    return y_pred[0]
 
def linearRegression2(weeksRateslist):
    if len (weeksRateslist) ==1:
        return weeksRateslist[0]
    elif len (weeksRateslist) == 2:
        return weeksRateslist[1]
    elif len (weeksRateslist) == 3:
        return weeksRateslist[2]
    else:
        y_pred = sklearn_linear_Regression(weeksRateslist)
    return y_pred



def predictionFun2(CountyRate):
    alist2D = []
    
    for yearIndex,year in enumerate (CountyRate):
        weeks_up_today=[]
        alist2D.append([])
        for weekIndex,week in enumerate(year):
            alist2D[yearIndex].append([])   #make space for a week
            weeks_up_today.append(week)
            aWeekPrediction = linearRegression2(weeks_up_today)
            alist2D[yearIndex][weekIndex]=aWeekPrediction
    return alist2D
            
#predictionDict["SB"]= predictionFun(CountyRateDict["SB"])
for county in counties:
    predictionDict[county]= predictionFun2(CountyRateDict[county])


###############################################################################
from itertools import chain



def ErrorScores(TrueData, PredictedData):    
    Ytrue = np.array(list(chain.from_iterable(TrueData)))
    Yhat = np.array(list(chain.from_iterable(PredictedData)))
    r2score = r2_score(Ytrue, Yhat, multioutput = "uniform_average" )
    RMSEscore = mean_squared_error(Ytrue, Yhat, multioutput = "uniform_average" )
    MAEscore = mean_absolute_error(Ytrue, Yhat, multioutput = "uniform_average" )
    return r2score, RMSEscore, MAEscore   
 
    
countyScores = {}
for county in counties:
    r2score, RMSEscore, MAEscore = ErrorScores(CountyRateDict[county], predictionDict[county])
    LR_scores=[r2score, RMSEscore, MAEscore]
    countyScores[county]=LR_scores
