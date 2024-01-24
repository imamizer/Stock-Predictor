# pip install yfinance --upgrade --no-cache-dir
import yfinance as yf
import pandas as pd

# Hisselerin sembolleri
symbols = ['AAPL', 'AMZN', 'GOOG', 'MSFT', 'TSLA']

# Veri aralığı
start_date = '2022-01-01'
end_date = '2022-04-15'

# Verileri indir
data = yf.download(symbols, start=start_date, end=end_date)

# Haftalık getirileri hesapla
weekly_returns = data['Adj Close'].resample('W-FRI').ffill().pct_change()

# En yüksek getirili hisseyi bul
max_return = weekly_returns.max()
max_symbol = weekly_returns[max_return.idxmax()].name[0]

# Sonuçları yazdır
print("En yüksek getiri:", round(max_return*100, 2), "%")
print("En yüksek getirili hisse:", max_symbol)
