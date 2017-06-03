import numpy as np
import pandas as pd
from sortData import sorting
from cleanData import dataCleanUp
from grouping import grouping


file_name = input('Please enter file name or press enter to continue:\n')
cr = None
GroupName = ['Section', 'Study Group']
NumofGroup = [3, 15]
if file_name == '':
    file_name = "/Users/Robin/Documents/GitHub/ondiversity/Data/data_public1.csv"

df = pd.read_csv(file_name)
df = dataCleanUp(df)
df = sorting(df, cr)


for i in range(len(GroupName)):
    if i == 0:
        indexG = None
    else:
        indexG = GroupName[i-1]

    df = grouping(df,NumofGroup[i],indexG,GroupName[i], cr)

df = df.sort_values(by = GroupName)    
df.to_csv('output.csv', index = False)
