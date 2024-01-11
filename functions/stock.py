import datetime
import yfinance as yf


def download_stock_data(symbol, interval, days):
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days)
    if interval == 1:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
    else:
        stock_data = yf.download(symbol, start=start_date, end=end_date, interval=interval)

    return stock_data


def download_stock_data_price(symbol, interval, days):
    df1 = download_stock_data(symbol, interval, days)
    df2 = df1['Close']
    return df2
