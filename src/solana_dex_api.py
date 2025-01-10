import requests
from config.solana_config import SOLANA_RPC_URL
import sys


def fetch_solana_price(pair_address):
    """
    Fetch token price from Solana DEX (e.g., Serum) using the RPC endpoint.
    Example: Fetch DOGE/USDC price from Serum.
    """
    print("pair address")
    print(pair_address)
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getAccountInfo",
        "params": [pair_address]
    }
    response = requests.post(SOLANA_RPC_URL, json=payload)
    data = response.json()
    print(data)
    
    # You need to decode the specific account data to extract the price
    # Assuming price extraction logic here
    return float(data['result']['value']['price'])  # Placeholder
