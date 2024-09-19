import yfinance as yf
import pandas as pd

# stock_data = yf.download('NVDA', start='2014-09-01', end='2024-09-01')
nvda = yf.Ticker("NVDA")

nvda_data = nvda.history(start='2010-01-01', end='2024-09-01', interval='1d')

nvda_history_sample = nvda.history(start='2024-08-24', end='2024-09-01', interval='1d')

print(nvda_history_sample)

