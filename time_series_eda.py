
## Install Pandas Data Reader
import pandas_datareader as pdr
import pandas as pd
from datetime import datetime
import os

from distutils.version import LooseVersion

df_tesla = pdr.DataReader('TSLA', 'stooq')

df_tesla.head()

df_tesla.tail()

df_tesla['High'].plot(figsize=(12,4))

## xlimit and y limit
df_tesla['High'].plot(xlim=['2022-01-01','2023-09-01'],figsize=(12,4))

## xlimit and y limit
df_tesla['High'].plot(xlim=['2022-01-01','2023-09-01'],ylim=[0,900],figsize=(12,4))

## xlimit and y limit and coloring
df_tesla['High'].plot(xlim=['2022-01-01','2023-09-01'],ylim=[0,900],figsize=(12,4),ls='--',c='green')

df_tesla.index

# Slice the DataFrame using timestamps
index=df_tesla.loc['2019-06-12':'2024-06-07'].index
share_open=df_tesla.loc['2019-06-12':'2024-06-07']['Open']

share_open
print(share_open)

index

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

figure,axis=plt.subplots()
plt.tight_layout()
## Preventing overlapping
figure.autofmt_xdate()
axis.plot(index,share_open)

##Datetime Index

df_tesla=df_tesla.reset_index()

df_tesla.info()

df_tesla=df_tesla.set_index('Date',drop=True)

df_tesla.head()

## datetime
from datetime import datetime

datetime(2021,11,21)

datetime.now()

date=datetime(2021,11,21)

date

date.date()

date.day

date.weekday()

date.year

date.month



"""## Time Resampling"""

df_tesla.head()

df_tesla.resample(rule='A').min()

df_tesla.resample(rule='A').max()

##year end frequency
df_tesla.resample(rule='A').max()['Open'].plot()

##quaterly start frequency
##https://towardsdatascience.com/resample-function-of-pandas-79b17ec82a78
df_tesla.resample(rule='QS').max()['High'].plot()

##Business End Frequency
##https://towardsdatascience.com/resample-function-of-pandas-79b17ec82a78
df_tesla.resample(rule='BA').max()

df_tesla.resample(rule='BQS').max()

##plotting
df_tesla['Open'].resample(rule='A').mean().plot(kind='bar')

df_tesla['Open'].resample(rule='M').max().plot(kind='bar',figsize=(15,6))

df_tesla['High'].rolling(11).max().head(20)

df_tesla.head()

df_tesla['Open:30 days rolling']=df_tesla['Open'].rolling(30).mean()

df_tesla.head(31)

df_tesla[['Open','Open:30 days rolling']].plot(figsize=(12,5))

"""##Assignment
##Here I have estimated the following in this assignment by performing EDA.
1. Read the Tesla Data using Pandas Data reader
2. Get the maximum price of the share from 2019 to 2024
3. Which is the date of the highest price of the stock?
4. Which is the date of the lowest price of the stock?

"""