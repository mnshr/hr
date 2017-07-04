# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 16:20:46 2017

@author: mnshr
"""

import pandas as pd1

web_stats={'Day': [1,2,3,4,5,6],
           'Visitors': [10, 20, 40, 80, 160, 200],
           'Bounce_Rate':[40, 50, 60, 70, 80, 100]}

df=pd1.DataFrame(web_stats)
print(df)  #default index is 0, 1, 2... but we can set the index too

df['Day']

print(df.set_index('Day')) #Makes Day as the index and removes default index
                  #set_index returns a new data frame, so assign
print( df.set_index('Day', inplace=True))
#inplace changes the existing data frame itself

print( df.Visitors)
print (df.Visitors.tolist())
print( df['Visitors'])
print( df.loc[1:3])
print( df[['Bounce_Rate', 'Visitors']]) #Working in Py3
#%%

import pandas as pd1
#https://pythonprogramming.net/join-merge-data-analysis-python-pandas-tutorial/
df1 = pd1.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd1.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd1.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

print(pd1.merge(df1,df3, on='HPI'))

#%%
df1 = pd1.DataFrame({'Year':[2001, 2002, 2003, 2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]})

df3 = pd1.DataFrame({'Year':[2001, 2003, 2004, 2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]})
# Default is INNER (Intersection)
merged=pd1.merge(df1, df3, on = 'Year')
merged.set_index('Year', inplace=True)
print (merged)

# LEFT
merged=pd1.merge(df1, df3, on = 'Year', how='left')
merged.set_index('Year', inplace=True)
print (merged)

# RIGHT
merged=pd1.merge(df1, df3, on = 'Year', how='right')
merged.set_index('Year', inplace=True)
print (merged)

# OUTER - UNION
merged=pd1.merge(df1, df3, on = 'Year', how='outer')
merged.set_index('Year', inplace=True)
print (merged)

#%%

#https://pythonprogramming.net/pickle-data-analysis-python-pandas-tutorial/

import pickle
#serialize and save the byte stream in disk
pickle_out = open('merged.pkl', 'wb')
pickle.dump(merged, pickle_out)
pickle_out.close()

pickle_in = open('merged.pkl', 'rb')
df4 = pickle.load(pickle_in)
print(df4)

# Pandas' Pickle in 2 lines
df4.to_pickle('merged2.pkl')
df5 = pd1.read_pickle('merged2.pkl')
print(df5)

#%%
# Statistics
# https://pythonprogramming.net/percent-change-correlation-data-analysis-python-pandas-tutorial/

import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
#style.use('ggplot')

df5.plot()
plt.legend().remove()
plt.show()

# Correlation function
df5.corr()
df5.describe()

#%%
# Resampling (change frequency)
# https://pythonprogramming.net/resample-data-analysis-python-pandas-tutorial/

TX1yr = HPI_data['TX'].resample('A', how='mean') # A is for annual
TX1yr = HPI_data['TX'].resample('A', how='ohlc') # ohlc is for open, hi, lo, close
print(TX1yr.head())

#%%
# Handling missing data (remove, fill, replace)
df5.dropna(inplace=True) # how default is 'any'
df5.dropna(inplace=True, how='all') # all cols must have values, else dropped

# Fillna
df5.fillna(method='ffill', inplace=True)  #Forward fill using prev values
df5.fillna(method='bfill', inplace=True)  #Forward bak using fwd values

# Filling with a value
df5.fillna(value=999, inplace=True)

#%%
# Rolling stats
# https://pythonprogramming.net/rolling-statistics-data-analysis-python-pandas-tutorial/

# Moving Average = Rolling mean, across a time window - 12 mo
HPI_data['TX12MA'] = pd.rolling_mean(HPI_data['TX'], 12) # 12 months
HPI_data['TX12STD'] = pd.rolling_std(HPI_data['TX'], 12) # 12 months

#%%
# Comparison Operators
bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}
df = pd1.DataFrame(bridge_height)


df['STD'] = pd1.rolling_std(df['meters'], 2)
print(df)

#df.plot()

df_std = df.describe()['meters']['std']
df = df[ (df['STD'] < df_std) ]
print(df)
print (df_std)
df['meters'].plot()
