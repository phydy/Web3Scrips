from web3 import Web3


def check_balance():
    infura_link = 'https://mainnet.infura.io/v3/a2c0525e61a54ad3aba9d25d1dde8d38'
    ganache_link = 'http://127.0.0.1:7545' # ganache on localhost
    bsc_link = 'https://bsc-dataseed1.binance.org'
    x = int(input('Enter active platform. 1 for infura, 2 for ganache and 3 for bsc: '))
    if x == 1:
        url_link = infura_link
        print('using infura')
    if x == 2:
        url_link = ganache_link
        print('using ganache')
    else:
        url_link = bsc_link
        print('using bsc')

    web3 = Web3(Web3.HTTPProvider(url_link))
    print(web3.isConnected())
    
    balance = web3.eth.getBalance(str(input('Enter wallet adress: ')))
    wei = Web3.fromWei(balance, 'ether')
    print('Balance in Wei: ', balance)
    print(wei)
check_balance()