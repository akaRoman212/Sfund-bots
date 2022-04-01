from web3 import Web3
import json
import config
import sys
import time
import webbrowser

private = config.private
bsc = "https://bsc-dataseed1.ninicoin.io/"
web3 = Web3(Web3.HTTPProvider(bsc))

print(web3.isConnected())

stakecontract = '0x66b8c1f8DE0574e68366E8c4e47d0C8883A6Ad0b'
abi = '[{"inputs":[{"internalType":"string","name":"name_","type":"string"},{"internalType":"address","name":"tokenAddress_","type":"address"},{"internalType":"uint64","name":"rate_","type":"uint64"},{"internalType":"uint256","name":"lockDuration_","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token","type":"address"},{"indexed":true,"internalType":"address","name":"staker_","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount_","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"reward_","type":"uint256"}],"name":"PaidOut","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint64","name":"index","type":"uint64"},{"indexed":false,"internalType":"uint64","name":"newRate","type":"uint64"},{"indexed":false,"internalType":"uint256","name":"lockDuration","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"RateAndLockduration","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"rewards","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"RewardsAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token","type":"address"},{"indexed":true,"internalType":"address","name":"staker_","type":"address"},{"indexed":false,"internalType":"uint256","name":"stakedAmount_","type":"uint256"}],"name":"Staked","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"status","type":"bool"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"StakingStopped","type":"event"},{"inputs":[],"name":"ERC20Interface","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rewardAmount","type":"uint256"}],"name":"addReward","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"}],"name":"calculate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"_status","type":"bool"}],"name":"changeStakingStatus","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"emergencyWithdraw","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"index","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"interestRateConverter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isStopped","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lockDuration","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rate","outputs":[{"internalType":"uint64","name":"","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint64","name":"","type":"uint64"}],"name":"rates","outputs":[{"internalType":"uint64","name":"newInterestRate","type":"uint64"},{"internalType":"uint256","name":"timeStamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"rewardBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint64","name":"rate_","type":"uint64"},{"internalType":"uint256","name":"lockduration_","type":"uint256"}],"name":"setRateAndLockduration","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"stake","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"stakedBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"stakedTotal","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tokenAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalParticipants","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"userDeposits","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"withdraw","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'
contract = web3.eth.contract(address=stakecontract, abi=abi)

sender_address = config.vholder_address #TokenAddress of holder

reward = contract.functions.calculate(sender_address).call()

options = contract.functions.userDeposits(sender_address).call()

epoch = float((options[2]) + 2)

print(f"You can claim {web3.fromWei(reward,'ether')} SFUND reward + {web3.fromWei(options[0],'ether')} SFUND that you staked.")

userchoice = input("Do you want to claim all tokens??? (0 for exit.)")

if(userchoice == '0'):
    sys.exit()

else:
    seconds = time.time()

    while (seconds <= epoch):
        print("Current time in seconds since epoch =", seconds)
        seconds = time.time()
        time.sleep(1)
    
    txn = contract.functions.withdraw().buildTransaction({
           'from': sender_address,
           'chainId': 56,
           'gas': 250000,
           'gasPrice': web3.toWei('7','gwei'),
           'nonce': web3.eth.get_transaction_count(sender_address),
                })
                        
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=config.private)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"Claimed SFUND: " + web3.toHex(tx_token))
    webbrowser.open("https://bscscan.com/tx/"+ web3.toHex(tx_token))


