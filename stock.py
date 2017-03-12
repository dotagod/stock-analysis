import pandas as pd
import re, sys, datetime
import matplotlib.pyplot as plt
import pylab

symbols_list = ['AAPL', 'YHOO','GOOG', 'MSFT']

stocks = pd.DataFrame()

for index, symbol in enumerate(symbols_list):
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/{}/chartdata;type=quote;range=1d/csv'.format(symbol)
    #print url
    data = pd.read_csv(url, skiprows=17)
    data.columns = ['timestamp', 'close', 'high', 'low', 'open', 'close']    
    stock = pd.DataFrame(data)
    stock['date'] = pd.to_datetime(stock['timestamp'],unit='s')
    date = stock['date']
    price = stock['open']
    #print '{}: has min date: {} and max date: {}'.format(symbol, date.min(), date.max())
    #print '{}: has min open price: {} and max date: {}'.format(symbol, price.min(), price.max())

    stocks['date'] = date
    stocks[symbol] = price

    plt.style.use('ggplot') 
    plt.plot(date, price)
    plt.show()

# Common graph should be the straight line
stocks.set_index('date', inplace=True)
plt.style.use('ggplot') 
stocks.plot()
plt.show()
