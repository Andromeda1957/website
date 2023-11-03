from tradingview_ta import TA_Handler, Exchange, Interval

interval_time = Interval.INTERVAL_1_DAY

pypl = TA_Handler(
    symbol='pypl',
    screener='america',
    exchange='NASDAQ',
    interval=interval_time
)

nvda = TA_Handler(
    symbol='nvda',
    screener='america',
    exchange='NASDAQ',
    interval=interval_time
)

dis = TA_Handler(
    symbol='DIS',
    screener='america',
    exchange='NYSE',
    interval=interval_time
)

ulta = TA_Handler(
    symbol='ulta',
    screener='america',
    exchange='NASDAQ',
    interval=interval_time
)

vsco = TA_Handler(
    symbol='vsco',
    screener='america',
    exchange='NYSE',
    interval=interval_time
)

tgt = TA_Handler(
    symbol='tgt',
    screener='america',
    exchange='NYSE',
    interval=interval_time
)

dg = TA_Handler(
    symbol='dg',
    screener='america',
    exchange='NYSE',
    interval=interval_time
)

cvs = TA_Handler(
    symbol='cvs',
    screener='america',
    exchange='NYSE',
    interval=interval_time
)

rtx = TA_Handler(
    symbol='rtx',
    screener='america',
    exchange='NYSE',
    interval=interval_time
)

ge = TA_Handler(
    symbol='ge',
    screener='america',
    exchange='NYSE',
    interval=interval_time
)
