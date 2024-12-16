from ib_insync import *
from utils.logger import logger
from utils.api import access_api

ib = IB()
ib.connect('127.0.0.1', 4001, clientId=1)
if ib.isConnected():
    logger.info('Connected')
else:
    logger.error('Not connected')
    raise Exception('Not connected')


response = access_api('/drive/download_file', method='POST', data={'file_id': '1_dvlQLjb5kAw45mMNO0PrugOoohcgF_G'})
logger.info(response)