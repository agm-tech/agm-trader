from ib_insync import *
from utils.logger import logger

ib = IB()
ib.connect('127.0.0.1', 4001, clientId=1)
if ib.isConnected():
    print('Connected')
else:
    raise Exception('Not connected')

contract = Stock('TSLA', 'SMART', 'USD')

dt = ''
barsList = []
while True:
    bars = ib.reqHistoricalData(
        contract,
        endDateTime=dt,
        durationStr='10 D',
        barSizeSetting='1 min',
        whatToShow='MIDPOINT',
        useRTH=True,
        formatDate=1)
    if not bars:
        break
    barsList.append(bars)
    dt = bars[0].date
    print(dt)