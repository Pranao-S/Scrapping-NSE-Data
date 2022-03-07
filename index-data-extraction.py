import pandas as pd
import requests
from nsepy import get_history
from datetime import date
# Extract Index Data
symbol = ['NIFTY SMLCAP 100','NIFTY SMLCAP 250','NIFTY SMLCAP 50','NIFTY MIDCAP 150','NIFTY 50','NIFTY NEXT 50','NIFTY FMCG']

data1=[]
data1 = pd.DataFrame(data1)
for x in symbol:
    data = get_history(symbol=x, start=date(2019,1,1), end=date(2020,12,31), index = True)
    data = pd.DataFrame(data)
    data['Index_Name'] = x
    data1 = pd.concat([data1,data])
    print(x)

# Save Index Data
data1.to_csv('Index_Data_2020.csv', index=True)