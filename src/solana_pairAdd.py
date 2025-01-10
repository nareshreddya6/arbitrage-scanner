import requests

# Example: Serum API endpoint to fetch market addresses
def fetch_serum_market_address(base_token, quote_token):
    url = f"https://api.serum.xyz/markets/{base_token}/{quote_token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()['address']
    else:
        print("Error fetching Serum market address")
        return None

# Fetch Serum market address for DOGE/USDC pair
solana_pair_address = fetch_serum_market_address("DOGE", "USDC")
print(f"Serum market address for DOGE/USDC: {solana_pair_address}")
