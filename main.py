from pandas_datareader import data
import requests_cache
import datetime
from pandas_datareader.yahoo.headers import DEFAULT_HEADERS
expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)
session.headers = DEFAULT_HEADERS
#Get the stock quote
start = datetime.datetime(2021, 1, 1) #start date Year-month-date
end = datetime.datetime(2021, 12, 31) #end date  Year-month-date
df = data.DataReader('BBCA.JK', 'yahoo', start, end,session=session)

#Show the data
print(df)
df = df.reset_index() #reset index data , old index is added as a column
df.to_excel("BBCA.xlsx", sheet_name="BBCA", index=False) #save to xlsx format same location with py file
df.to_csv('BBCA.csv',index=False) #save to csv format same location with py file
