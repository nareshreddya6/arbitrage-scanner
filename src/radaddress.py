import requests

def fetch_raydium_markets():
    raydium_url = "https://api.raydium.io/markets"  # Example endpoint, you need to verify
    response = requests.get(raydium_url)
    if response.status_code == 200:
        markets = response.json()
        usdc_pairs = [market for market in markets if 'USDC' in market['baseCurrency']]
        return [(market['baseCurrency'], market['address']) for market in usdc_pairs]
    else:
        print("Error fetching Raydium markets")
        return []

# Fetch Raydium USDC markets
usdc_markets = fetch_raydium_markets()
print("Raydium USDC Markets:")
for pair, address in usdc_markets:
    print(f"{pair}: {address}")
