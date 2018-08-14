from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, send_from_directory
)
from core_ui.services import rpcrequest

wallet_bp = Blueprint('wallet', __name__)

@wallet_bp.route('/')
def index():
    rq = rpcrequest.get_info()
    return render_template('wallet/index.html', info=rq)

@wallet_bp.route('/send', defaults={'selected_address' : ''})
@wallet_bp.route('/send/<selected_address>', methods=['GET', 'POST'])
def send(selected_address):

    return render_template('wallet/......')

@wallet_bp.route('/send_coin', methods=['POST'])
def send_coin():

    return render_template('wallet/......')

@wallet_bp.route('/receive', defaults={'selected_address' : ''})
@wallet_bp.route('/receive/<selected_address>')
def receive(selected_address):

    return render_template('wallet/......')

@wallet_bp.route('/new_address', methods=['POST'])
def new_address():

    return render_template('wallet/......')

@wallet_bp.route('/transaction')
def transaction():

    return render_template('wallet/......')

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

@wallet_bp.route('/offline')
def offline():

    return render_template('wallet/......')

@wallet_bp.route('/start_wallet')
def start_wallet():

    return render_template('wallet/......')

@wallet_bp.route('/upload', methods=['POST'])
def upload():

    return redirect(url_for('index'))

@wallet_bp.route('/download', methods=['GET'])
def download():
    return send_from_directory()
