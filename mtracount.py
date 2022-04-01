from web3 import Web3
import json
import config
import winsound
import time
duration = 1000  # milliseconds
freq = 440  # Hz


bsc = "https://apis.ankr.com/da0f895994864e028e42680005253879/3f9c242608423761e3d903276bbd9644/polygon/full/main"
# bsc = "https://speedy-nodes-nyc.moralis.io/b6905c301ad6187a708272d7/bsc/testnet"
web3 = Web3(Web3.HTTPProvider(bsc))

print(web3.isConnected())




wallet_id = web3.toChecksumAddress(input("Enter Wallet Address of token you want to watch: "))
# contract_id = web3.toChecksumAddress("0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c")


temp = web3.eth.getTransactionCount(wallet_id, "pending")
nounce = temp
while( nounce == temp ):
    nounce = web3.eth.getTransactionCount(wallet_id, "pending")
    
print(nounce)

            
winsound.Beep(freq, duration)








