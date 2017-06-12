# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
buyers
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')
print (prices)

#get_pricing()
#%%
from datetime import datetime
date1='8/29/2013 10:16'
dt1 = datetime.strptime(date1, '%m/%d/%Y %H:%M')
print(date1)
print(dt1)
print(dt1.strftime('%H'))
dt1.weekday()

#%%
trip_data = pd.read_csv('babs_y1_y2_summary.csv')
display(trip_data.head())
#%%
def featureScaling(arr):
    arr1=arr
    mn=min(arr)
    mx=max(arr)
    i=0
    for tmp in arr:
        arr1[i]=(tmp-mn)/(mx-mn)
        i=i+1
    return arr1

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print (featureScaling(data))