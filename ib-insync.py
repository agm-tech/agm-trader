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


from ib_insync import *
from utils.logger import logger
from utils.api import access_api
import pandas as pd
import io

ib = IB()
ib.connect('127.0.0.1', 4001, clientId=1)
if ib.isConnected():
    logger.info('Connected')
else:
    logger.error('Not connected')
    raise Exception('Not connected')

response = access_api('/drive/download_file', method='POST', data={'file_id': '1_dvlQLjb5kAw45mMNO0PrugOoohcgF_G', 'mime_type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'})

try:
    excel_data = io.BytesIO(response)
    df = pd.read_excel(excel_data)
    
    logger.info(f"Successfully loaded data into DataFrame with shape {df.shape}")
except Exception as e:
    logger.error(f"Error parsing Excel file: {str(e)}")
    raise


"""
bond = Bond(secIdType='ISIN', secId='US620076AM16')
details = ib.reqContractDetails(bond)
logger.info(details)
"""

ib.disconnect()