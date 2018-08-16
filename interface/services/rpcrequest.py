from . import wallet

# Gets all the info from the wallet
def wallet_info():
    result = {'immature_coins' : immature_coins(), 'address' : wallet.getaccountaddress(''),
            'tx_list' : wallet.listtransactions('*', 100)}
    list = [wallet.getwalletinfo(), wallet.getnetworkinfo(), wallet.getstakinginfo(),
            wallet.getblockchaininfo(), wallet.getnettotals()]

    for pairs in list:
        result.update(pairs)

    time = int(result['expectedtime']) / 60 / 60 / 24
    expected_time = round(time)
    result['expected_time'] = expected_time #Time to stake in days
    result['block_time'] = wallet.getblock(wallet.getbestblockhash())['time'] # Time since last Block

    return result

# Gets the coins/tokens that are not mature for staking. (less than 500 confirmations)
def immature_coins():
    get_list = wallet.listunspent(0)
    confirmations = filter(lambda x : x['confirmations'] < 500, get_list)
    immature_coins = sum(map(lambda x : float(x['amount']), confirmations))
    return immature_coins
