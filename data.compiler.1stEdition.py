# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:49:11 2019

@author: matth
"""

#Hello, welcome to Group 1's interactive data compiler in python
#This program creates influenza related csv files by county in the state of montana
#This is a rough draft interface

#Please enter the following inputs. 
modpath="D:\\Spring 2019\\Data Science M46_\\" #path to Module folder. Please in format with \\ and end with \\
masterfile_path= "D:\\Spring 2019\\Data Science M46_\\Module\\initial_flu.01.28.csv" #This should be a file path to the master data file 
input1=['all'] #please put 'all' or a list of any n county abreviations as seen in our master key
#If feild not applicable please put XX
adj='Y' #please put Y to include adjacent counties in your data sets
input2=['XX'] #put any additional county abreivation in the quotation.
lag= 1       #Put any number for which you would like to lag the additional counties data
ins=".1"   #Incase you don't want to save over your previous data sets just yet, this number will differentiate files
#region=
#ppm=






#Do not touch ANYTHING below this line unless you know what you are doing






import os,sys
import pandas as pd
sys.path.insert(0,modpath)
from Module import functions as UM #imports functions from seperate file

countyDict=UM.countyDictBuild()
f=pd.read_csv(masterfile_path, engine='python')
countylist=UM.CountyListBuild()
if input1[0]=='all':
    for county in countylist:
        #print(county)
        keep_col = ['year','flu week',county+" rate",county+" pop",county+" count"]
        newf=f[keep_col]
        if adj=="Y":
            adjcounty=countyDict[county]
            n=0
            #print(adjcounty)
            adjlist=[]         
            for n in range(len(adjcounty)):
                keep_adj=[adjcounty[n]+' rate', adjcounty[n]+' count', adjcounty[n]+' pop']
                n=n+1
                adjlist.extend(keep_adj)
                #keep_col.extend(keep_adj)
                i=0
                #print(keep_col)
        if input2[i] in countylist:
            for i in range(len(input2)):
                add_county=[input2[i]+' rate', input2[i]+' count', input2[i]+' pop']
                print(add_county)
                adjlist.extend(add_county)
                i=i+1
        new_f1 = f[adjlist]
        #new_f1.rename(columns={'flu week':'lag week'},inplace=True)
        new_f1=new_f1.shift(lag)
        new_f= newf.join(new_f1, how='outer')
        if len(adjlist)==0:
            new_f=newf
        tpath=modpath+ "Module\\data\\" + county + ins + ".csv"
        new_f.to_csv(tpath, index=False)
        new_f.to_csv(tpath, index=False)          
for n in range(len(input1)):
    if input1[n] in countylist:
        county=input1[n]
        #print(county)
        keep_col = ['year','flu week',county+" rate",county+" pop",county+" count"]
        newf=f[keep_col]
        if adj=="Y":
            adjcounty=countyDict[county]
            n=0
            #print(adjcounty)
            adjlist=[]         
            for n in range(len(adjcounty)):
                keep_adj=[adjcounty[n]+' rate', adjcounty[n]+' count', adjcounty[n]+' pop']
                n=n+1
                adjlist.extend(keep_adj)
                #keep_col.extend(keep_adj)
                i=0
                #print(keep_col)
        if input2[i] in countylist:
            for i in range(len(input2)):
                add_county=[input2[i]+' rate', input2[i]+' count', input2[i]+' pop']
                print(add_county)
                adjlist.extend(add_county)
                i=i+1
        new_f1 = f[adjlist]
        #new_f1.rename(columns={'flu week':'lag week'},inplace=True)
        new_f1=new_f1.shift(lag)
        new_f= newf.join(new_f1, how='outer')
        if len(adjlist)==0:
            new_f=newf
        tpath=modpath+ "Module\\data\\" + county + ins + ".csv"
        new_f.to_csv(tpath, index=False)