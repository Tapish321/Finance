import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
# import pandas_datareader.data as web
# import pandas_datareader
style.use('ggplot')
df = pd.read_csv('tesla.csv', index_col = 0, parse_dates=True)

print(df.head())
df['Adj Close'].plot()
# plt.show()

# print(df['Open'])
# print(df[['Open','Close']].head())
#to get 100 moving average and add that column
df['100ma'] = df['Adj Close'].rolling(window = 100).mean()
#or we can just put same values in place i.e. same values till 99 as Adj close
df['100ma'] = df['Adj Close'].rolling(window = 100, min_periods = 0).mean()

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=5,colspan=1)

ax1.plot(df.index,df['Adj Close'])
ax1.plot(df.index,df['100ma'])
ax2.bar(df.index,df['Volume'])
# plt.show()

#To move both grids together i.e zooming together we can add a parameter

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=5,colspan=1,sharex =ax1)

ax1.plot(df.index,df['Adj Close'])
ax1.plot(df.index,df['100ma'])
ax2.bar(df.index,df['Volume'])
# plt.show()



