from binance.client import Client
from config.binance_config import BINANCE_API_KEY, BINANCE_API_SECRET

# Initialize Binance Client
client = Client(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET)

def get_binance_prices():
    """
    Fetch current prices for all trading pairs from Binance.
    """
    tickers = client.get_all_tickers()
    return {ticker['symbol']: float(ticker['price']) for ticker in tickers}

def get_usdc_pairs():
    """
    Get all USDC trading pairs from Binance.
    """
    prices = get_binance_prices()
    #print("prices of binance:",prices)
    return {pair: price for pair, price in prices.items() if 'USDC' in pair}
