# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:49:11 2019

@author: matth
"""

#Hello, welcome to Group 1's interactive data compiler in python
#This program creates influenza related csv files by county in the state of montana
#This is a rough draft interface

#Please enter the following inputs. 
modpath="F:\\Spring 2019\\Data Science M46_\\" #path to Module folder. Please in format with \\ and end with \\
masterfile_path= "F:\\Spring 2019\\Data Science M46_\\Module\\initial_flu.02.02.csv" #This should be a file path to the master data file 
input1=['MI'] #please put 'all' or a list of any n county abreviations as seen in our master key
#If feild not applicable please put XX
adj='Y' #please put Y to include adjacent counties in your data sets
input2=['XX'] #put any additional county abreivation in the quotation.
lag= 1       #Put any number for which you would like to lag the additional counties data
ins=".1"   #Incase you don't want to save over your previous data sets just yet, this number will differentiate files
a=.1 #alpha for input
#region=
#ppm=


#Do not touch ANYTHING below this line unless you know what you are doing


import os,sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,modpath)
from Module import functions as UM #imports functions from seperate file

countyDict=UM.countyDictBuild()
f=pd.read_csv(masterfile_path, engine='python')
countylist=UM.CountyListBuild()
f=UM.smoothdata(countylist,a,f)
if input1[0]=='all': #unique line
    for county in countylist:#unique line
        new_f=UM.databuild(county,adj,input2,lag,f,countyDict,countylist)
        tpath=modpath+ "Module\\data\\" + county + ins + ".csv"
        new_f.to_csv(tpath, index=False)          
for n in range(len(input1)): #unique line
    if input1[n] in countylist: #unique line
        county=input1[n] #unique line
        new_f=UM.databuild(county,adj,input2,lag,f,countyDict,countylist)
        tpath=modpath+ "Module\\data\\" + county + ins + ".csv"
        new_f.to_csv(tpath, index=False)
        
##Plotting test
week_list = [i for i in range(442)]
MI_list = f["MI rate"].tolist()
MI_weighted = f["MI weighted rate"].tolist()
plt.plot(week_list,MI_weighted)
plt.plot(week_list,MI_list,'ro')