import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate mean reversion indicator
def mean_reversion(prices, window=14, num_std=2):
    rolling_mean = prices.rolling(window=window).mean()
    rolling_std = prices.rolling(window=window).std()
    upper_band = rolling_mean + (rolling_std * num_std)
    lower_band = rolling_mean - (rolling_std * num_std)
    return rolling_mean, upper_band, lower_band

# Fetch price data from Alpha Vantage API
api_key = 'YOUR_API_KEY'
symbol = 'EURUSD'

url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={symbol}&to_symbol=USD&apikey={api_key}&datatype=json'
response = requests.get(url)
data = json.loads(response.text)

prices = []
dates = []
for date in sorted(data['Time Series FX (Daily)']):
    price = float(data['Time Series FX (Daily)'][date]['4. close'])
    prices.append(price)
    dates.append(date)

# Convert price data to a Pandas dataframe
df = pd.DataFrame({'Date': dates, 'Price': prices})
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Calculate mean reversion indicator
rolling_mean, upper_band, lower_band = mean_reversion(df['Price'])

# Plot price data and mean reversion indicator
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Price'], label='EURUSD')
plt.plot(rolling_mean.index, rolling_mean, label='Rolling Mean')
plt.plot(upper_band.index, upper_band, label='Upper Band')
plt.plot(lower_band.index, lower_band, label='Lower Band')
plt.legend(loc='upper left')
plt.title('EURUSD Mean Reversion Indicator')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
