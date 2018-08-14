from . import wallet


def wallet_info():
    rq = wallet.getwalletinfo()
    x = wallet.getnetworkinfo()
    y = wallet.getstakinginfo()
    z = wallet.getblockchaininfo()
    block_time = wallet.getblock(z['bestblockhash'])
    rq.update(x)
    rq.update(y)
    time = int(rq['expectedtime']) / 60 / 60 / 24
    expected_time = round(time)
    rq['expected_time'] = expected_time #Time to stake in days
    rq['blocks'] = z['blocks']
    rq['bestblockhash'] = z['bestblockhash']
    rq['block_time'] = block_time['time']
    x1 = wallet.getnettotals()
    rq['totalbytesrecv'] = x1['totalbytesrecv']
    rq['totalbytessent'] = x1['totalbytessent']
    return rq

def immature_coins():
    total_coins = 0
    unspent_coins = wallet.listunspent()
    for unspent in unspent_coins:
        if unspent['confirmations'] < 500:
            total_coins += unspent['amount']
        return total_coins
    return total_coins

def get_address():
    addr = wallet.getaccountaddress('')
    return addr


def get_received_tx():
    tx_in = wallet.listtransactions('*', 100)
    return tx_in
