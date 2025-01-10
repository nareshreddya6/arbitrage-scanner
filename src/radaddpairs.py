import requests

# Raydium API to fetch pool addresses
raydium_pool_url = "https://api.raydium.io/pairs"

import requests

# Raydium API to fetch pool addresses
#raydium_pool_url = "https://api.raydium.io/v2/pairs"
def raydiumpairs():

    response = requests.get(raydium_pool_url)

    # Check if the response is valid
    if response.status_code == 200:
        pools = response.json()  # Parse the JSON response
        
        # Filter out the pairs involving USDC
        usdc_pools = [pool for pool in pools if 'USDC' in pool['name']]
        
        print("Raydium USDC Pair Addresses:")
        for pool in usdc_pools:
            # Print the token pair name and the AMM ID (or any relevant address field)
            print(f"{pool['name']} : {pool['amm_id']}")
    else:
        print("Error fetching data from Raydium API")

# response = requests.get(raydium_pool_url)
# #pools = response.json()
# print(pools)
# # Filter out the pairs involving USDC
# usdc_pools = [pool for pool in pools if 'USDC' in pool['tokenA']['symbol'] or 'USDC' in pool['tokenB']['symbol']]

# print("Raydium USDC Pair Addresses:")
# for pool in usdc_pools:
#     print(f"{pool['tokenA']['symbol']}/{pool['tokenB']['symbol']} : {pool['address']}")
