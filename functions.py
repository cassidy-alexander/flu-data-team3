# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:36:58 2019

@author: matth
"""
#countyDict['GR']=['MI','PW','CMHD','RA','BE']
#countyDict['PI']=['GF','MC','CMHD','WI','FA','CMHD']
#countyDict['ST']=['PA','SG','YE','CA']
#'GR','PI','ST'

def CountyListBuild():
    countyList=['BE','BH','BL','BR','CA','CS','CMHD','FA','FL','GA','GF','GL','HI',
          'JE','LA','LC','LI','LN','MA','MC','ME','MI','MS','PA','PH','PO','PR','PW',
          'RA','RI','RO','RS','SA','SH','SB','SG','TE','TO','TR','VA','WI','YE']
    return countyList
def countyDictBuild():
    countyList=CountyListBuild()
    countyDict={}
    countyDict=dict.fromkeys(countyList)
    countyDict['BE']=['RA','SB','MA','CMHD']
    countyDict['BH']=['YE','TR','CA','RS','PR']
    countyDict['BL']=['HI','PH']
    countyDict['BR']=['LC','JE','GA','ME']
    countyDict['CA']=['PA','YE','BH']
    countyDict['CS']=['TE','LC','ME','CMHD']
    countyDict['CMHD']=['YE','RS','GF','PH','BL','CS','ME','SG']
    countyDict['FA']=['WI','PR','CS']
    countyDict['FL']=['LI','SA','LA','MS','PW','LC','TE','PO','GL']
    countyDict['GA']=['MA','JE','BR','ME','PA']
    countyDict['GF']=['RO','PH','VA','MC','CMHD']
    countyDict['GL']=['FL','PO','TO']
    countyDict['HI']=['LI','CMHD','BL']
    countyDict['JE']=['MA','SB','CMHD','PW','LC','BR','GA']
    countyDict['LA']=['MS','SA','FL','PW']
    countyDict['LC']=['FL','TE','CS','ME','BR','JE','PW']
    countyDict['LI']=['TO','PO','CMHD','HI']
    countyDict['LN']=['FL','SA']
    countyDict['MA']=['BE','SB','JE','GA']
    countyDict['MC']=['GF','VA','RO','RI','CMHD',]
    countyDict['ME']=['LC','CS','SG','PA','GA','BR']
    countyDict['MI']=['SA','MS']
    countyDict['MS']=['MI','SA','LA','FL','PW','RA']
    countyDict['PA']=['GA','ME','SG','CA']
    countyDict['PH']=['BL','GF','VA']
    countyDict['PO']=['GL','FL','TE','CMHD','LI','TO']
    countyDict['PR']=['BH','RS','CMHD',]
    countyDict['PW']=['CMHD','MS','FL','LC','JE']
    countyDict['RA']=['MS','CMHD','BE']
    countyDict['RI']=['RO','MC','CMHD','WI']
    countyDict['RO']=['SH','CMHD','VA','MC','RI']
    countyDict['RS']=['GF','TR','BH','PR','CMHD']
    countyDict['SA']=['LN','FL','LA','MS','MI']
    countyDict['SH']=['CMHD','RO']
    countyDict['SB']=['JE','CMHD','BE','MA']
    countyDict['SG']=['PA']
    countyDict['TE']=['PO','CMHD','CS','LC','FL']
    countyDict['TO']=['GL','PO','LI']
    countyDict['TR']=['RS','BH','YE']
    countyDict['VA']=['PH','GF','MC','RO','CMHD']
    countyDict['WI']=['RI','CMHD','FA']
    countyDict['YE']=['CA','TR','BH']
    return countyDict