from . import wallet as rpc_call # This is the flask_wallet_rpc variable


# Gets all the info from the wallet for the index page.
def wallet_info():
    result = {'immature_coins' : immature_coins(), 'address' : rpc_call.getaccountaddress(''),
            'tx_list' : list_tx()}
    wallet_list = [
        rpc_call.getwalletinfo(), rpc_call.getnetworkinfo(), rpc_call.getstakinginfo(),
        rpc_call.getblockchaininfo(), rpc_call.getnettotals(),
    ]

    for pairs in wallet_list:
        result.update(pairs)

    time = int(result['expectedtime']) / 60 / 60 / 24
    result['expected_time'] = round(time) #Time to stake in days
    result['block_time'] = rpc_call.getblock(rpc_call.getbestblockhash())['time'] # Time since last Block

    return result

# Gets the coins/tokens that are not mature for staking. (less than 500 confirmations)
def immature_coins():
    get_list = rpc_call.listunspent(0)
    confirmations = filter(lambda x : x['confirmations'] < 500, get_list)
    immature_coins = sum(map(lambda x : float(x['amount']), confirmations))
    return immature_coins

# Gets the last 60 wallet tx and removes duplicate tx id's from unspent outs and block staking.
def list_tx():
    list_tx = rpc_call.listtransactions('*', 60)
    txid = filter(lambda x : x['txid'] != txid, list_tx)
    output = list(txid)
    return output

def unspent_tx():
    get_list = rpc_call.listunspent(0)
    pass

def encrypt_wallet():
    encrypt = rpc_call.encryptwallet('password')
    pass

def enable_staking(passwd, duration, stake): # Wallet needs to be encrypted (use encryptwallet)
    unlock = rpc_call.walletpassphrase("%s" %d %s) % (passwd, duration, stake)
    pass

def lock_wallet():
    lock = rpc_call.walletlock()
    pass

def add_node():
    node = rpc_call.addnode('ipaddress', 'add')
    pass

def qrcode(address, amount, name, msg):
    response = 'coin:%s?amount=%s&label=%s&message=%s' % (address, amount, name, msg)
    pass
