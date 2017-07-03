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