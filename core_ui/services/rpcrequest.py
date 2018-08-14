from . import wallet


def get_info():
    rq = wallet.getinfo()
    return rq
