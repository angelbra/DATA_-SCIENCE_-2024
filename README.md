
# Analys av priser för Tesla och Bitcoin (2014-2017)
INLÄMINGS uppgifter 1

Analys av priser för Tesla och Bitcoin (2014-2017)
## Datakällor
 - Bitcoin 2014-2024:
 https://www.kaggle.com/datasets/kapturovalexander/bitcoin-and-ethereum-prices-from-start-to-2023
 - TESLA aktie priser:
 https://www.kaggle.com/datasets/henryshan/tesla-stock-price

## Code

import pandas as pd

df = pd.read_csv("TSLA.csv" and "BTC-USD (2014-2024).csv")

tsla_df = pd.read_csv("TSLA.csv")
btc_df = pd.read_csv("BTC-USD (2014-2024).csv")

print("first rows TSLA.csv:")
print(tsla_df.head())

ska visas så här:
first rows TSLA.csv:
|   |    Date    |   open     |   high   |   low    |  Close   |  adj Close |  Volumen  | 
|---|------------|------------|----------|----------|----------|------------|-----------|
| 0 | 2010-06-29 | 1.266667   | 1.666667 | 1.169333 | 1.592667 |  1.592667  | 281494500 |
| 1 | 2010-06-30 | 1.719333   | 2.028000 | 1.553333 | 1.588667 |  1.588667  | 257806500 |
| 2 | 2010-07-01 | 1.666667   | 1.728000 | 1.351333 | 1.464000 |  1.464000  | 123282000 | 
| 3 | 2010-07-02 | 1.533333   | 1.540000 | 1.247333 | 1.280000 | 1.280000   | 77097000  |         
| 4 | 2010-07-06 | 1.333333   | 1.333333 | 1.055333 | 1.074000 | 1.074000   | 103003500 |


print("first rows BTC-USD (2014-2024).csv:")
print(btc_df.head())

ska visas så här:
first rows BTC-USD (2014-2024).csv:
|   |    Date    |   open     |    high    |   low    |    Close     |  adj Close |  Volumen  | 
|---|------------|------------|------------|----------|--------------|------------|-----------|
| 0 | 2014-09-18 | 456.859985 | 456.859985 | 413.104004 | 424.440002 |  1.592667  | 34483200.0| 
| 1 | 2014-09-19 | 424.102997 | 427.834991 | 384.532013 | 394.795990 | 394.795990 | 37919700.0|
| 2 | 2014-09-20 | 394.673004 | 423.295990 | 389.882996 | 408.903992 | 408.903992 | 36863600.0|   
| 3 | 2014-09-21 | 408.084991 | 412.425995 | 393.181000 | 398.821014 | 398.821014 | 26580100.0| 
| 4 | 2014-09-22 | 399.100006 | 406.915985 | 397.130005 | 402.152008 | 402.152008 | 24127600.0| 

här organiserar jag data bara innan 2017. 
btc_before_2017 = btc_df[btc_df['Date'] < '2017-01-01']
tsla_before_2017 = tsla_df[tsla_df['Date'] < '2017-01-01']

print("Bitcoin Date Before 2017:")
print(btc_before_2017)

print("Tesla Date Before 2017:")
print(tsla_before_2017)

btc_prices_before_2017 = btc_df[btc_df['Date'] < '2017-01-01'][['Open', 'High', 'Low', 'Close']]
tsla_prices_before_2017 = tsla_df[tsla_df['Date'] < '2017-01-01'][['Open', 'High', 'Low', 'Close']]

print("Bitcoin Prices Before 2017:")
print(btc_prices_before_2017)

print("Tesla Prices Before 2017:")
print(tsla_prices_before_2017)

här ville jag skapa graphic av priser från 2014 till 2017 av båda bts och tesla:
import matplotlib.pyplot as plot 

plot.plot(btc_before_2017['Date'], btc_before_2017['High'], label='Bitcoin High Prices', color='blue')
plot.plot(tsla_before_2017['Date'], tsla_before_2017['High'], label='Tesla High Prices', color='orange')

plot.xlabel('Date')
plot.ylabel('High Prices')
plot.title('Bitcoin and Tesla High Prices Before 2017')
plot.legend()

![image](https://github.com/user-attachments/assets/b27c9ac7-145b-48c7-9631-d506b0b2fb53)
