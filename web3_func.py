#import Web3 (capital W) from web3 (small W)
from web3 import Web3
import json
#put API url(infura) or (ganache) or BSC


def assign_platform():
    infura_link = 'https://mainnet.infura.io/v3/a2c0525e61a54ad3aba9d25d1dde8d38'
    bsc_link = 'https://bsc-dataseed1.binance.org'
    x = int(input('Enter active platform. 1 for infura, 2 for ganache and 3 for bsc: '))
    if x == 1:
        url_link = infura_link
        print('using infura')
    else:
        url_link = bsc_link
        print('using bsc')

    web3 = Web3(Web3.HTTPProvider(url_link))

    print(web3.isConnected())

    print(web3.eth.blockNumber)
 
    contract_address = Web3.toChecksumAddress(str(input('Enter contract adress: '))) #str(input('Enter contract Address: '))
    ABI = str(input('Enter ABI: '))
    abi = json.loads(ABI)
    contract = web3.eth.contract(address=contract_address, abi=abi)
    total_supply = contract.functions.totalSupply().call()
    print(total_supply)
assign_platform()