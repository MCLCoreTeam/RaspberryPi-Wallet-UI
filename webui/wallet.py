from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, send_from_directory
)

wal = Blueprint('wallet', __name__)

@wal.route('/')
def index():

    return render_template('wallet/index.html')

@wal.route('/send', defaults={'selected_address' : ''})
@wal.route('/send/<selected_address>', methods=['GET', 'POST'])
def send(selected_address):

    return render_template('wallet/......')

@wal.route('/send_coin', methods=['POST'])
def send_coin():

    return render_template('wallet/......')

@wal.route('/receive', defaults={'selected_address' : ''})
@wal.route('/receive/<selected_address>')
def receive(selected_address):

    return render_template('wallet/......')

@wal.route('/new_address', methods=['POST'])
def new_address():

    return render_template('wallet/......')

@wal.route('/transaction')
def transaction():

    return render_template('wallet/......')

@wal.route('/setup', methods=['GET', 'POST'])
def setup():

    return render_template('wallet/......')

@wal.route('/encrypt_wallet', methods=['POST'])
def encrypt_wallet():

    return render_template('wallet/......')

@wal.route('/staking_service', methods=['POST'])
def staking_service():

    return render_template('wallet/......')

@wal.route('/add_node', methods=['POST'])
def add_node():

    return render_template('wallet/......')

@wal.route('/send_req', defaults={'selected_cmd' : ''})
@wal.route('/send_req/<selected_cmd>', methods=['GET'])
def send_req(selected_cmd):

    return render_template('wallet/......')

@wal.route('/offline')
def offline():

    return render_template('wallet/......')

@wal.route('/start_wallet')
def start_wallet():

    return render_template('wallet/......')

@wal.route('/upload', methods=['POST'])
def upload():

    return redirect(url_for('index'))

@wal.route('/download', methods=['GET'])
def download():
    return send_from_directory()
