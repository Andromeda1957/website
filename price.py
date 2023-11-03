import yfinance as yf

def get_stock_price(ticker):
    ticker = yf.Ticker(ticker)
    data = ticker.history()
    stock_price = '{:.2f}'.format(round(data['Close'].iloc[-1], 2))
    return stock_price
