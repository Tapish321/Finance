import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib import style


'''
Plotting the Ohlc over time for every 10 days
ohlc = open high low close
'''
style.use('ggplot')
df = pd.read_csv('tesla.csv', index_col=0, parse_dates = True)
# print(df.head())
# df['100ma'] = df['Adj Close'].rolling(window=100,min_periods=0).mean()
# print(df.head())
df_ohlc = df['Adj Close'].resample('10D').ohlc() #resmapling the data for 10 Days can also do minutes, months, year etc
df_volume = df['Volume'].resample('10D').sum()
# print(df_ohlc.head())
df_ohlc.reset_index(inplace=True) # Adding index column
# print(df_ohlc.head())
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)  # cahnging dates to numbers for ohlc plot
#matplot requires numbers on the date columns
print(df_ohlc.head())
ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=5,colspan =1,sharex =ax1)
ax1.xaxis_date()
candlestick_ohlc(ax1,df_ohlc.values, width= 2,colorup="blue")
ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0,facecolors='g') #filling inbetween(parameters- X, Y 0 for what to fill in between
plt.show()