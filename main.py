from indicators import mean_reversion
from strategies import mean_reversion as mean_reversion_strategy
from backtest import Backtest

with open('config.json') as f:
    config = json.load(f)

ticker = config['ticker']
timeframe = config['timeframe']
indicator_settings = config['indicator_settings']
strategy_settings = config['backtest_settings']['strategy_settings']
initial_capital = config['backtest_settings']['initial_capital']
commission = config['backtest_settings']['commission']
slippage = config['backtest_settings']['slippage']
start_date = config['backtest_settings']['start_date']
end_date = config['backtest_settings']['end_date']

ohlcv = get_ohlcv(ticker, timeframe, start_date, end_date)
indicator = mean_reversion(ohlcv, N=indicator_settings['N'])
signals = mean_reversion_strategy(indicator, long_threshold=strategy_settings['long_threshold'], short_threshold=strategy_settings['short_threshold'])
bt = Backtest(signals, ohlcv, initial_capital=initial_capital, commission=commission, slippage=slippage)
bt.run()
