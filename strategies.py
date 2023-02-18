import pandas as pd

def mean_reversion(indicator, long_threshold=-1.0, short_threshold=1.0, stop_loss=2.0, take_profit=2.0):
    signals = pd.DataFrame(index=indicator.index)
    signals['Positions'] = 0
    signals['Buy'] = (indicator['Indicator'] < long_threshold).astype(int)
    signals['Sell'] = (indicator['Indicator'] > short_threshold).astype(int)
    signals['Stop Loss'] = indicator['Lower Band'] * stop_loss
    signals['Take Profit'] = indicator['Upper Band'] * take_profit
    return signals
