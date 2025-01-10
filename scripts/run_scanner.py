from src.binance_api import get_usdc_pairs
from src.solana_dex_api import fetch_solana_price
from src.arbitrage import calculate_arbitrage
from src.utils import log_message
from src.radaddpairs import  raydiumpairs
from src.solana_price import get_solana_price


print("run_scanner")
def main():
    # Fetch Binance USDC pairs
    binance_pairs = get_usdc_pairs()
    print("binance pairs",binance_pairs)
    # Example: Solana DEX address for a token pair
    base_token = "DOGE"
    quote_token = "USDC"
    solana_pair_address ="9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin"
    #"srmqPvymJeFKQ4zGQed1GFppgkRHL9kaELCbyksJtPX"
    
   # Doge/USDC : 3CPk8ssR4A6XE8brxFLiikrdRuMt2kSDuFecmkEQyxUS
                 
    #solana_pair_address = raydiumpairs()

    for pair, binance_price in binance_pairs.items():
        # Skip pairs not available on Solana
        if pair not in ["DOGEUSDC"]:  # Replace with actual pairs to monitor
            continue
        
        #print(solana_pair_address)
        # Fetch price from Solana DEX
        solana_price = get_solana_price()

        # Arbitrage calculation
        trade_amount = 100  # Example trade amount
        profit = calculate_arbitrage(binance_price, solana_price, trade_amount)

        if profit > 0:
            message = f"Arbitrage Opportunity: {pair}, Profit: ${profit:.2f}"
            print(message)
            log_message(message)
        else:
            print(f"No profitable arbitrage for {pair}")

if __name__ == "__main__":
    main()
