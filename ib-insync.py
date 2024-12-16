from ib_insync import *
from utils.logger import logger

ib = IB()
ib.connect('127.0.0.1', 4001, clientId=1)
if ib.isConnected():
    print('Connected')
else:
    raise Exception('Not connected')

account_positions = ib.positions(account='U14313113')
logger.info(account_positions)

ib.disconnect()