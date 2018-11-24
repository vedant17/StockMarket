import pandas as pd
import quandl as quant

data = pd.read_csv("/home/vegeta/NIFTYDATA/ind_niftybanklist.csv")

symbol = data["Symbol"]

for i in range(0,10):
    url = symbol[i]
    url_dataset = 'NSE/' + url
    quant.ApiConfig.api_key  = 'KuTgzkSh6BkjfsSjYYxo'
    stocks = quant.get(url_dataset, start_date='2018-01-01', end_date='2018-04-01')
    filename = symbol[i] + ' Jan to March'
    stocks.to_csv('/home/vegeta/NIFTYDATA/'+filename+'.csv',sep=',')