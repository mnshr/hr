# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 14:33:19 2017

@author: mnshr
"""

import pandas as pd
import datetime
from pandas_datareader import data, wb
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

start=datetime.datetime(2010,1,1)
end = datetime.datetime(2017,1,1)

df=data.DataReader("AMZN", "google", start, end) #Using Google finance APIs

print df.head() #head returns top 5 rows

df['Close'].plot()
plt.show()

#Pandas dataframe is like Python dictionary

#%%
web_stats={'Day': [1,2,3,4,5,6],
           'Visitors': [10, 20, 40, 80, 160, 200],
           'Bounce_Rate':[40, 50, 60, 70, 80, 100]}

df=pd.DataFrame(web_stats)
print(df)  #default index is 0, 1, 2... but we can set the index too

df['Day']

print df.set_index('Day') #Makes Day as the index and removes default index
                  #set_index returns a new data frame, so assign
print df.set_index('Day', inplace=True)
#inplace changes the existing data frame itself

print df.Visitors
print df['Visitors']
print df.loc[1:3]

print df[['Bounce_Rate', 'Visitors']] #Day won't work since its an index now
import numpy as np
print np.array(df[['Bounce_Rate', 'Visitors']]) #Creates a 2D array using NP
df2 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))
print df2 #Create a Data frame from a Numpy Array

#%%
