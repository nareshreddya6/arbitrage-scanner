import requests
from config.binance_config import BINANCE_API_KEY,BINANCE_API_SECRET

def fetch_binance_fees(api_key):
    url = "https://api.binance.com/sapi/v1/asset/tradeFee"
    headers = {
        'X-MBX-APIKEY': BINANCE_API_KEY
    }
    response = requests.get(url, headers=headers)
    fees = response.json()
    print(fees)
    for fee in fees:
        print(f"Symbol: {fee['symbol']}, Maker Fee: {fee['maker']}, Taker Fee: {fee['taker']}")

# Replace 'your_api_key' with your actual Binance API key
fetch_binance_fees('your_api_key')
