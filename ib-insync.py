from ib_insync import *
from utils.logger import logger
from utils.api import access_api
import pandas as pd
import io

response = access_api('/drive/download_file', method='POST', data={'file_id': '1_dvlQLjb5kAw45mMNO0PrugOoohcgF_G', 'mime_type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'})

try:
    csv_data = io.BytesIO(response)
    df = pd.read_csv(csv_data)
except Exception as e:
    logger.error(f"Error parsing Excel file: {str(e)}")
    raise Exception(f"Error parsing Excel file: {str(e)}")

isin_codes = df['ISIN'].str.strip().tolist()

ib = IB()

try:
    ib.connect('127.0.0.1', 4001, clientId=1)
except Exception as e:
    logger.error(f"Error connecting to IB: {str(e)}")
    raise Exception(f"Error connecting to IB: {str(e)}")

bonds = []
logger.info(f'Found a total of {len(isin_codes)} bonds in the database, fetching details for the first 5...')

for isin in isin_codes[0:5]:
    bond = Bond(secIdType='ISIN', secId=isin)
    details = ib.reqContractDetails(bond)
    for d in details:
        logger.info(d.descAppend)
        bonds.append(d)

ib.disconnect()
