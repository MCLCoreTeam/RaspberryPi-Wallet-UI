from . import wallet


def wallet_info():
    # Gets all the info from the wallet
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



def immature_coins():
    # Gets the coins/tokens that are not mature for staking. (less than 500 confirmations)
    total_coins = 0
    unspent_coins = wallet.listunspent()
    for unspent in unspent_coins:
        if unspent['confirmations'] < 500:
            total_coins += unspent['amount']
        return total_coins
    return total_coins
