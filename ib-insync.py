from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 4001, clientId=1)
if ib.isConnected():
    print('Connected')
else:
    raise Exception('Not connected')

bond = Bond(secIdType='ISIN', secId='US620076AM16')
details = ib.reqContractDetails(bond)
print(details)

ib.disconnect()
