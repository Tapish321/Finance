import bs4 as bs
import pickle
import requests
# from lxml import etree



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


sp500_comapnies_tickers()