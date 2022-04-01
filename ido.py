import os
os.system("")
import decimal
import sys
from web3 import Web3
import json
import config
import time
import webbrowser
import chalk

private = config.private
slippage= config.norm_slippage
tgas = config.gas
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())
sender_address = config.vholder_address #TokenAddress of holder

idocontract = web3.toChecksumAddress(input("Enter the Contract Address of IDO to buy from: "))
abi = '[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"uint256","name":"_maxCap","type":"uint256"},{"internalType":"uint256","name":"_saleStart","type":"uint256"},{"internalType":"uint256","name":"_saleEnd","type":"uint256"},{"internalType":"uint256","name":"_noOfTiers","type":"uint256"},{"internalType":"address","name":"_projectOwner","type":"address"},{"internalType":"address","name":"_tokenAddress","type":"address"},{"internalType":"uint256","name":"_totalUsers","type":"uint256"},{"internalType":"uint8","name":"_phaseNo","type":"uint8"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":true,"internalType":"uint8","name":"phase","type":"uint8"}],"name":"UserInvestment","type":"event"},{"inputs":[],"name":"ERC20Interface","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"buyTokens","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"maxCap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"noOfTiers","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"phaseNo","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"projectOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"saleEnd","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"saleStart","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"tierDetails","outputs":[{"internalType":"uint256","name":"maxTierCap","type":"uint256"},{"internalType":"uint256","name":"minUserCap","type":"uint256"},{"internalType":"uint256","name":"maxUserCap","type":"uint256"},{"internalType":"uint256","name":"amountRaised","type":"uint256"},{"internalType":"uint256","name":"users","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tokenAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalBUSDReceivedInAllTier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalUsers","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newSaleEnd","type":"uint256"}],"name":"updateEndTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_maxCap","type":"uint256"}],"name":"updateMaxCap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newsaleStart","type":"uint256"}],"name":"updateStartTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_tier","type":"uint256[]"},{"internalType":"uint256[]","name":"_maxTierCap","type":"uint256[]"},{"internalType":"uint256[]","name":"_minUserCap","type":"uint256[]"},{"internalType":"uint256[]","name":"_maxUserCap","type":"uint256[]"},{"internalType":"uint256[]","name":"_tierUsers","type":"uint256[]"}],"name":"updateTiers","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_users","type":"address[]"},{"internalType":"uint256[]","name":"_tiers","type":"uint256[]"}],"name":"updateUsers","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"userDetails","outputs":[{"internalType":"uint256","name":"tier","type":"uint256"},{"internalType":"uint256","name":"investedAmount","type":"uint256"}],"stateMutability":"view","type":"function"}]'
contract = web3.eth.contract(address=idocontract, abi=abi)

tier = contract.functions.userDetails(sender_address).call()
options = contract.functions.tierDetails(tier[0]).call()

print(chalk.yellow("You can buy upto " + str(web3.fromWei(options[2],'ether')) + " BUSD \n"))

busd_addr = web3.toChecksumAddress("0xe9e7cea3dedca5984780bafc599bd69add087d56")
tokenAbi = '[{"inputs":[{"internalType":"string","name":"_NAME","type":"string"},{"internalType":"string","name":"_SYMBOL","type":"string"},{"internalType":"uint256","name":"_DECIMALS","type":"uint256"},{"internalType":"uint256","name":"_supply","type":"uint256"},{"internalType":"uint256","name":"_txFee","type":"uint256"},{"internalType":"uint256","name":"_lpFee","type":"uint256"},{"internalType":"uint256","name":"_MAXAMOUNT","type":"uint256"},{"internalType":"uint256","name":"SELLMAXAMOUNT","type":"uint256"},{"internalType":"address","name":"routerAddress","type":"address"},{"internalType":"address","name":"tokenOwner","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"minTokensBeforeSwap","type":"uint256"}],"name":"MinTokensBeforeSwapUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tokensSwapped","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"ethReceived","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tokensIntoLiqudity","type":"uint256"}],"name":"SwapAndLiquify","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"enabled","type":"bool"}],"name":"SwapAndLiquifyEnabledUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"_liquidityFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_maxTxAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_taxFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"claimTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"}],"name":"deliver","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"excludeFromFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"excludeFromReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"geUnlockTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"includeInFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"includeInReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isExcludedFromFee","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isExcludedFromReward","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"time","type":"uint256"}],"name":"lock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"numTokensSellToAddToLiquidity","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tAmount","type":"uint256"},{"internalType":"bool","name":"deductTransferFee","type":"bool"}],"name":"reflectionFromToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"liquidityFee","type":"uint256"}],"name":"setLiquidityFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"maxTxPercent","type":"uint256"}],"name":"setMaxTxPercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"swapNumber","type":"uint256"}],"name":"setNumTokensSellToAddToLiquidity","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_enabled","type":"bool"}],"name":"setSwapAndLiquifyEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"taxFee","type":"uint256"}],"name":"setTaxFeePercent","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"swapAndLiquifyEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rAmount","type":"uint256"}],"name":"tokenFromReflection","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalFees","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"uniswapV2Pair","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"uniswapV2Router","outputs":[{"internalType":"contract IUniswapV2Router02","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"unlock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'
busd_contract = web3.eth.contract(busd_addr, abi=tokenAbi)
balance = busd_contract.functions.balanceOf(sender_address).call()

if balance < options[1]:
    print(chalk.red("You have Insufficient BUSD \n"))
    sys.exit()


al_value = busd_contract.functions.allowance(sender_address, idocontract).call()
ap_quan = busd_contract.functions.balanceOf(sender_address).call()

if int(al_value) <= int(ap_quan):
    approve = busd_contract.functions.approve(idocontract, 4200999399996203280118531922).buildTransaction({
            'from': sender_address,
            'chainId': 56,
            'gas': 100000,
            'gasPrice': web3.toWei('5','gwei'),
            'nonce': web3.eth.get_transaction_count(sender_address),
            })
    signed_txn = web3.eth.account.sign_transaction(approve, private_key=config.private)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(chalk.green(f"Approved: " + "https://bscscan.com/tx/"+ web3.toHex(tx_token)))
    webbrowser.open("https://bscscan.com/tx/"+ web3.toHex(tx_token))
else:
    print(chalk.yellow("BUSD is already approved to trade on IDO Contract!!!"))



user = input("Do you want to continue??? (0 for exit)")

if user == '0':
    sys.exit()


seconds = time.time()

epoch = float(contract.functions.saleStart().call())

receipt = {
    'status' : 0
}
 
while (seconds <= (epoch + 1)):
    print("Current time in seconds since epoch =", seconds)
    seconds = time.time()
    time.sleep(1)

    
while (receipt['status'] != 1 ):
        txn = contract.functions.buyTokens(
        options[2]
         ).buildTransaction({
           'from': sender_address,
           'chainId': 56,
           'gas': 150000,
           'gasPrice': web3.toWei('8','gwei'),
           'nonce': web3.eth.get_transaction_count(sender_address),
         })
               
        print("Waiting for txn ..............")       
        signed_txn = web3.eth.account.sign_transaction(txn, private_key=config.private)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        receipt  = web3.eth.wait_for_transaction_receipt(web3.toHex(tx_token))
        if(receipt['status'] == 1):
            print('SUCCESS!!!')
        else:
            print('FAILED!!!') 
            
print(chalk.green(f"Bought: " + "https://bscscan.com/tx/"+ web3.toHex(tx_token)))
webbrowser.open("https://bscscan.com/tx/"+ web3.toHex(tx_token))
