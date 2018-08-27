import time
from flask import (
    Blueprint, flash, redirect, current_app, render_template, request, send_from_directory
)

from interface.services import rpcrequest

wallet_bp = Blueprint('wallet', __name__)

@wallet_bp.route('/')
def index():
    wallet_info = rpcrequest.wallet_info()
    return render_template('wallet/index.html', wallet_info=wallet_info, time=time, ui_version=current_app.config['UI_VERSION'])

@wallet_bp.route('/send', defaults={'selected_address' : ''})
@wallet_bp.route('/send/<selected_address>', methods=['GET', 'POST'])
def send(selected_address):

    return render_template('wallet/send.html', wallet_info=rpcrequest.wallet_info())

# @wallet_bp.route('/send_coin', methods=['POST'])
# def send_coin():
#
#     return render_template('wallet/send.html')

@wallet_bp.route('/receive', defaults={'selected_address' : ''})
@wallet_bp.route('/receive/<selected_address>')
def receive(selected_address):

    return render_template('wallet/......')

@wallet_bp.route('/new_address', methods=['POST'])
def new_address():

    return render_template('wallet/......')

@wallet_bp.route('/history')
def history():

    return render_template('wallet/tx_history.html', all_tx=rpcrequest.list_tx(), time=time)

@wallet_bp.route('/setup', methods=['GET', 'POST'])
def setup():

    return render_template('wallet/......')

@wallet_bp.route('/encrypt_wallet', methods=['POST'])
def encrypt_wallet():

    return render_template('wallet/......')

@wallet_bp.route('/staking_service', methods=['POST'])
def staking_service():

    return render_template('wallet/......')

@wallet_bp.route('/add_node', methods=['POST'])
def add_node():

    return render_template('wallet/......')

@wallet_bp.route('/send_req', defaults={'selected_cmd' : ''})
@wallet_bp.route('/send_req/<selected_cmd>', methods=['GET'])
def send_req(selected_cmd):

    return render_template('wallet/......')

@wallet_bp.route('/download', methods=['GET'])
def download():
    return send_from_directory()
