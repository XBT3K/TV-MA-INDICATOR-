import pandas as pd
import numpy as np

def mean_reversion(ohlcv, N=20):
    close = ohlcv['Close']
    upper_band = close.rolling(window=N).mean() + close.rolling(window=N).std()
    lower_band = close.rolling(window=N).mean() - close.rolling(window=N).std()
    indicator = (close - close.rolling(window=N).mean()) / close.rolling(window=N).std()
    return pd.DataFrame({'Upper Band': upper_band, 'Lower Band': lower_band, 'Indicator': indicator})
