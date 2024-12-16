from ib_insync import *
from utils.logger import logger

ib = IB()
ib.connect('127.0.0.1', 4001, clientId=1)
if ib.isConnected():
    logger.info('Connected')
else:
    logger.error('Not connected')
    raise Exception('Not connected')

bond = Bond(secIdType='ISIN', secId='US620076AM16')
details = ib.reqContractDetails(bond)
logger.info(details)

ib.disconnect()