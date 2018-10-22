import matplotlib.pyplot as plt
import numpy as np
import csv
import glob
import pandas as pd

# 2: A is equal to the contents inside of the Question field.  Here is the script to extract
# the contents of the column:

df = pd.read_csv('./CDC_Obesity_Data.csv')
saved_column = df['Question']
Question = df.Question
print (Question)

#3: For all of Y, B is the sum of y1 at each data point. I need to get the sum of data	
# in column 'Data_Value.' Here is the script to do so:


df = pd.read_csv('./CDC_Obesity_Data.csv')
print (df['Data_Value'].sum())

#4 (not working): 
#df = pd.read_csv('./CDC_Obesity_Data.csv')
#x_start, x_end = 2, 29 
#y_start, y_end = 2, 29 

#x = np.genfromtxt('Question',  usecols=(1))
y = np.genfromtxt('Data_Value', usecols=(1))

#x = x[x_start - 1:x_end]
#y = y[y_start - 1:y_end]

#print (' x=', x, '\n\n y=', y)

#plt.plot(x, y)
#plt.show()

