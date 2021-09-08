from web3 import Web3



def send_ether():
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


    account_one =  str(input('Enter your account: '))#'0xF9e1592cB538AdD0c27F64A18E262776ede96ad8'
    account_2 = str(input('Enter destination: ')) #'0xc3127d30566a5566a5c577D42d06470Fa9748152'
    amount = int(input('Enter Amount to send: '))
    #private key for account one
    private_key = str(input('Enter Private key for Your Account: ')) #'2c15bef27415cb3a4075f3828c5e88fd413807ac37801594f83558b539e9357a'
    #get the nonce
    #nonce prevents sending the transaction twice.
    nonce = web3.eth.getTransactionCount(account_one)
    #build Ttansaction
    transaction_dic ={
        'nonce': nonce,
        'to': account_2,
        'value': web3.toWei(amount, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei')
    }
    #signing the transaction
    signed_transaction = web3.eth.account.signTransaction(transaction_dic, private_key)
    trans_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    print(trans_hash)
send_ether()