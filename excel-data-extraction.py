import pandas as pd
from datetime import date

today = date.today()
print('todays date is',today)

reading = pd.read_excel('stocks_list.xlsx')
reading.Stock
'''
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
'''
