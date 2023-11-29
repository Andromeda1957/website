import tickers
import price

from flask import *
from tradingview_ta import TA_Handler, Exchange, Interval

app = Flask(__name__)
HOST = '127.0.0.1'
PORT = 8000

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stocks')
def stocks():
    pypl = price.get_stock_price('PYPL')
    nvda = price.get_stock_price('NVDA')
    dis = price.get_stock_price('dis')
    ulta = price.get_stock_price('ulta')
    vsco = price.get_stock_price('vsco')
    tgt = price.get_stock_price('tgt')
    dg = price.get_stock_price('dg')
    cvs = price.get_stock_price('cvs')
    rtx = price.get_stock_price('rtx')
    ge = price.get_stock_price('ge')
    
    return render_template('stocks.html',pypl=pypl, nvda=nvda, dis=dis,
                           ulta=ulta, vsco=vsco, tgt=tgt, dg=dg, cvs=cvs,
                           rtx=rtx, ge=ge)

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

