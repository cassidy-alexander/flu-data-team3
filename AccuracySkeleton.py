# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:31:10 2019

@author: mm111335
"""

import sys
import numpy as np
import matplotlib.pyplot as plt 
path = "D:\Spring 2019\Data Science M46_"
sys.path.insert(0,path)
if path not in sys.path:
    sys.path.append(path) #add the path
from Module import functions2 as f #functions is imported from the moduleDir
path = r'D:\Spring 2019\Data Science M46_\Module\current.csv'
countyList=['BE','BH','BL','BR','CA','CS','CMHD','FA','FL','GA','GF','GL','HI',
          'JE','LA','LC','LI','LN','MA','MC','ME','MI','MS','PA','PH','PO','PR','PW',
          'RA','RI','RO','RS','SA','SH','SB','SG','TE','TO','TR','VA','WI','YE']
countyDict=f.countyData(countyList)
countyDict=f.adjcountyDict(countyList)

#%% K Nearest neighbors
k=4  #number of weeks that has rate closest to predictor week
alpha=1/k
predictionkNearest=f.createPredictionDict(countyList)
f.kNearest(alpha,k,predictionkNearest)
CountyScoresKNN=f.AccuracyScores(countyDict,predictionkNearest)
#%%Accuaracy K Nearest neighbors
county='MI'
year= 4
model=' kNearest'  
#%%           
x=[i for i in range(1,len(countyDict[county][year]['count']))]    #weights from week 41 to 1
z=[i for i in countyDict[county][year]['count'][1:]]
y=[i for i in predictionkNearest[county][year]['count'][:-1]]   
titlename= county +" year_"+ str(year)
fig=plt.figure()
fig.suptitle(titlename, fontsize=14, fontweight='bold')
plt.plot(x,y,'bo-',label=county+' counts')
plt.plot(x,z,'ro-',label=county+ model)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.ylabel('counts')
plt.xlabel('weeks')
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textstr="r^2= "+ str(np.array(CountyScoresKNN["MS"][4]))
## place a text box in upper left in axes coords
plt.text(0.05, 0.95, textstr, fontsize=11,verticalalignment='top', bbox=props)
plt.show()