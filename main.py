import pandas as pd
df = pd.read_csv("TSLA.csv" and "BTC-USD (2014-2024).csv")

#scrapping från kraggle 

tsla_df = pd.read_csv("TSLA.csv")
btc_df = pd.read_csv("BTC-USD (2014-2024).csv")

print("first rows TSLA.csv:")
print(tsla_df.head())
#visas 5 första rows av TESLA transaktioner

print("first rows BTC-USD (2014-2024).csv:")
print(btc_df.head())
#visas 5 första rows av BTC från 2014-2024

#här organiserar jag data bara innan 2017. 
btc_before_2017 = btc_df[btc_df['Date'] < '2017-01-01']
tsla_before_2017 = tsla_df[tsla_df['Date'] < '2017-01-01']

print("Bitcoin Date Before 2017:")
print(btc_before_2017)
#här skrivs ut rows innan 2017 av BTC
print("Tesla Date Before 2017:")
print(tsla_before_2017)
#här skrivs ut rows innan 2017 av Tsla.

btc_prices_before_2017 = btc_df[btc_df['Date'] < '2017-01-01'][['Open', 'High', 'Low', 'Close']]
tsla_prices_before_2017 = tsla_df[tsla_df['Date'] < '2017-01-01'][['Open', 'High', 'Low', 'Close']]
#här ville jag hantera data så det kan visas bara priset innan 2017 

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

