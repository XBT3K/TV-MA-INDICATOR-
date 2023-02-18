import pandas as pd

def mean_reversion(indicator, long_threshold=-1.0, short_threshold=1.0):
    signals = pd.DataFrame(index=indicator.index)
    signals['
