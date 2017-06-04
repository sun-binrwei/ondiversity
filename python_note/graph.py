#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 23:50:52 2017

@author: Robin
"""

import pandas as pd
import numpy as np


def graph(df = pd.read_csv('output.csv'), cr, groupName):
    
   '''
   df is a dataframe
   cr is a list of criteria, eg. ['gender', 'nat', 'profession']
   groupName is a list with 1 or 2 elements, eg. ['section', 'group'],
   the first element is main group, the second is subgroup
   '''
   
   #Get unique numbers of the main group
   maingroup = df[groupName[0]].unique()
   
   #Get unique numbers of the subgroup
   if len(groupName) > 1:
       subgroup = df[groupName[1]].unique()
   else:
       subgroup = None
       subResult = None
       
   #Calcualte the Richness of each main group and subgroup
   mainResult = pd.DataFrame(columns = [groupName[0], 'cr', 'richness', 'IER'])
   subResult = pd.DataFrame(columns = [groupName[0], groupName[1],'cr', 'richness', 'IER'])

   for i in maingroup:
       
       for c in cr:
           r = richness(df[groupName[0] == i], c)
           IER = simpsonIER(df[groupName[0] == i], c)
           index = len(mainResult)
           mainResult.set_value(index,groupName[0], i)
           mainResult.set_value(index,'cr', c)
           mainResult.set_value(index,'richness', r)
           mainResult.set_value(index,'IER', IER)
           if subgroup != None:
               for s in subgroup:
                   r = richness(df[groupName[1] == s], c)
                   IER = simpsonIER(df[groupName[1] == s], c)
                   index = len(subResult)
                   subResult.set_value(index,groupName[0], i)
                   subResult.set_value(index,groupName[1], s)
                   subResult.set_value(index,'cr', c)
                   subResult.set_value(index,'richness', r)
                   subResult.set_value(index,'IER', IER)
       
                   
    
    #Plot result for maingroup
    
    
    
    
    
    #Plot result for subgroup
           
       
       
    
def richness(df, cr):
# This function returns the richness of the 'kind'    
# df : the data frame
# str : the string for column name (specity 'kind')
    items = df[cr].dropna()
    R = len(np.unique(items)) # richness
    return(R)


def simpsonIER(df, cr):
# This function returns the IER (inter-kind encounter rate) 
# c : the data frame
# str : the string for column name
    items = pd.DataFrame(df[cr].dropna())
    N = len(items)
    p = items.groupby(cr).size()
    IER = (1 - sum((p/N)**2)) * N / (N-1)
    return(IER)