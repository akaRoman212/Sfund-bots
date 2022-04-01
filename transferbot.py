
from web3 import Web3
import json
import config
import time 
private = config.private


bsc = "https://polygon-rpc.com"
web3 = Web3(Web3.HTTPProvider(bsc))

print(web3.isConnected())

contract_id = web3.toChecksumAddress(input("Enter the Contract Address of token you want to transfer: "))
# contract_id = web3.toChecksumAddress("0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c")

abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeSub","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeDiv","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeMul","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeAdd","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"}]')

contract = web3.eth.contract(address=contract_id, abi=abi)

totalSupply = contract.functions.totalSupply().call()

print(web3.fromWei(totalSupply, 'ether'))
print(contract.functions.name().call())
print(contract.functions.symbol().call())

me = web3.toChecksumAddress(config.sender_addr)  #send from this address
to_address= web3.toChecksumAddress(config.rec_addr)   #to this address

readable = 0
receipt = {
    'status': 0
}

while receipt['status'] == 0:
    while (readable < 1):
        balanceOf = contract.functions.balanceOf(me).call()
        readable = web3.fromWei(balanceOf, 'ether')
        print(readable)
        time.sleep(1)


    send = int(readable) - 1
    amount = web3.toWei(send, 'ether')
    nonce = web3.eth.getTransactionCount(me)

    token_tx = contract.functions.transfer(to_address, amount).buildTransaction({
        'chainId': 137,
        'gas': 150000,
        'maxFeePerGas': web3.toWei('300','gwei'),
        'maxPriorityFeePerGas': web3.toWei('100','gwei'),
        'nonce':nonce
    })
    sign_txn = web3.eth.account.signTransaction(token_tx, private)
    tx = web3.eth.sendRawTransaction(sign_txn.rawTransaction)
    receipt  = web3.eth.wait_for_transaction_receipt(web3.toHex(tx))
    if(receipt['status'] == 1):
        print('SUCCESS!!!')
    else:
        print('FAILED!!!') 
    print(f"Transaction has been sent to {to_address}")
