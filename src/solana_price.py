import requests

def get_solana_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        print("solana prices",data)
        print('Current Solana Price in USD:', data['solana']['usd'])
        return data['solana']['usd']
    except requests.exceptions.RequestException as error:
        print('Error fetching Solana price:', error)

get_solana_price()
