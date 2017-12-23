import pandas as pd
import pickle
import numpy as np
import datetime as dt
import os   #creates new directories
import pandas_datareader.data as web   #this import is not working in pycharm please check notebook
import bs4 as bs
import requests
import time




#get the 500 companies tickers from wikipedia scrapping
def sp500_comapnies_tickers():
    request = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(request.text)
    table = soup.find('table', {'class':'wikitable sortable'})   # Find the table we want
    tickers = []
    for row in table.findAll('tr')[1:]:     #tr= table rwo from the page
        ticker = row.findAll('td')[0].text  #In every row we want object from first column which is ticker of the company
        tickers.append(ticker)
    # Append the object into pickle

    with open('sp500tickers.pickle', 'wb') as f:
        pickle.dump(tickers,f)

    print(tickers)
    return tickers
'''
once we have the tickers we need the stock data. We will grab that from yahoo 
We can either reload(call) above function or upload ticker file

'''


def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:  # if it was true in call above
        tickers = sp500_comapnies_tickers()
    else:
        with open('sp500tickers.pickle', 'rb') as f:  # take from pickle
            tickers = pickle.load(f)
    if not os.path.exists('stocks_dfs'):  # check if the directory exist
        os.makedirs('stocks_dfs')  # if not make one

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2017, 12, 20)

    for ticker in tickers:
        # print(ticker)
        print (tickers.index(ticker),':',ticker)

        if not os.path.exists('stocks_dfs/{}.csv'.format(ticker)):  # Check if it already exist
            # time.sleep(5)
            df = web.DataReader(ticker, 'yahoo', start, end)  # if not grab from yahoo
            # df = web.DataReader('TSLA', 'yahoo',start,end)

            df.to_csv('stocks_dfs/{}.csv'.format(ticker))  # save in csv file
        else:
            print('Already have{}'.format(ticker))  # or print already have

get_data_from_yahoo()
'''
for i in range(0,100):
    try:

        get_data_from_yahoo()

        # raise RemoteDataError()
    except  :
        pass

'''