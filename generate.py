import requests
import json
import numpy as np
import pandas
from datetime import datetime

stocks=['ADBL','NABIL','NIFRA','SANIMA','EBL']
entries='4000'
start_dates=['2019-12-20','2011-03-20','2021-02-14','2012-02-27','2011-03-20']
today=str(datetime.today().date())

for stock,start_date in zip(stocks,start_dates):
  url='https://www.nepalipaisa.com/api/GetStockHistory?stockSymbol='+stock+'&fromDate='+start_date+'&toDate='+today+'&pageNo=1&itemsPerPage='+entries+'&pagePerDisplay=5&_=1725526625076'
  response=requests.get(url)
  jsn=response.json()
  stock_data=jsn.get('result').get('data')
  data=[]
  for row in stock_data:
    temp=[]
    temp.append(datetime.strptime(row['tradeDateString'], '%Y-%m-%d').date())
    temp.append(float(row['maxPrice']))
    temp.append(float(row['minPrice']))
    temp.append(float(row['closingPrice']))
    temp.append(float(row['noOfTransactions']))
    temp.append(float(row['volume']))
    temp.append(float(row['amount']))
    temp.append(float(row['previousClosing']))
    temp.append(float(row['differenceRs']))
    temp.append(float(row['percentChange']))
    data.append(temp)
  head=['date','high','low','close','noOfTransaction','volume','amount','open','change','chgPercent']
  data.reverse()
  df=pandas.DataFrame(data,columns=head)
  df.to_csv('data/'+stock+'.csv',index=False)
  
