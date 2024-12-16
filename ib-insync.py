from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 4001, clientId=1)
if ib.isConnected():
    print('Connected')
else:
    raise Exception('Not connected')

amd = Stock('AMD')
details = ib.reqContractDetails(amd)
contracts = [cd.contract for cd in details]
print(contracts)

ib.disconnect()
