import yfinance as yf
import tickers

from flask import Flask, render_template, redirect, request, jsonify
from tradingview_ta import TA_Handler, Exchange, Interval

app = Flask(__name__)
HOST = '127.0.0.1'
PORT = 8000

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stocks')
def stocks():
    return render_template('stocks.html')

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    ticker = request.get_json()['ticker']
    data = yf.Ticker(ticker).history(period='1y')
    return jsonify({'currentPrice': data.iloc[-1].Close,
                    'openPrice': data.iloc[-1].Open})

@app.route('/recommendations')
def recommendations():
    pypl = tickers.pypl.get_analysis().summary['RECOMMENDATION']
    nvda = tickers.nvda.get_analysis().summary['RECOMMENDATION']
    dis = tickers.dis.get_analysis().summary['RECOMMENDATION']
    ulta = tickers.ulta.get_analysis().summary['RECOMMENDATION']
    vsco = tickers.vsco.get_analysis().summary['RECOMMENDATION']
    tgt = tickers.tgt.get_analysis().summary['RECOMMENDATION']
    dg = tickers.dg.get_analysis().summary['RECOMMENDATION']
    cvs = tickers.cvs.get_analysis().summary['RECOMMENDATION']
    rtx = tickers.rtx.get_analysis().summary['RECOMMENDATION']
    ge = tickers.ge.get_analysis().summary['RECOMMENDATION']
    return render_template('recommendations.html',pypl=pypl, nvda=nvda, dis=dis,
                           ulta=ulta, vsco=vsco, tgt=tgt, dg=dg, cvs=cvs,
                           rtx=rtx, ge=ge)

if __name__ == '__main__':
    app.run(HOST, PORT)

