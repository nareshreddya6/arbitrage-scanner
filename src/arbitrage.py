from src.fees import calculate_binance_fee, calculate_solana_swap_fee, calculate_solana_transaction_fee
from config.binance_config import BINANCE_API_KEY
print("heel")
def calculate_arbitrage(binance_price, solana_price, trade_amount):
    """
    Calculate arbitrage profit after fees.
    """


    # Buying on Binance, selling on Solana
    binance_fee = calculate_binance_fee(trade_amount)
    solana_fee = calculate_solana_swap_fee(trade_amount)
    solana_tx_fee = calculate_solana_transaction_fee()
    #print(trade_amount,binance_price,binance_fee,solana_fee,solana_tx_fee)
    slippage_tolerance=0.001
     # Adjust for slippage tolerance (typically 0.1%)
    adjusted_binance_price = binance_price * (1 - slippage_tolerance)
    adjusted_solana_price = solana_price * (1 - slippage_tolerance)
    # Total cost
    total_cost = trade_amount * adjusted_binance_price + binance_fee + solana_fee + solana_tx_fee
    print(trade_amount,solana_price,total_cost)
    # Profit after selling on Solana
    profit = (trade_amount * adjusted_solana_price) - total_cost
    return profit
