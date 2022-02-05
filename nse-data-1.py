import os
import yfinance as yf  # pip install yfinance
import pandas as pd  # pip install pandas

start = "2020-01-01"
end= "2020-07-31"
tickers = 'GOOG TSLA MMM'

df = yf.download(tickers, start=start, end=end)
df.index = df.index.strftime('%Y-%m-%d')
df.to_excel('stock_data_1.xlsx')

#Navigate to NSE's(National stock exchange) archive page where historical data of any stock can be downloaded in archive format
driver.get("https://www.nseindia.com/products/content/equities/equities/eq_security.htm")

#importing data from excel to python
pd.read_excel('stocks.xlsx')
