def calculate_binance_fee(trade_amount, fee_rate=0.001):
    """
    Calculate Binance trading fee (default: 0.1%).
    """
    return trade_amount * fee_rate

def calculate_solana_swap_fee(trade_amount, fee_rate=0.003):
    """
    Calculate Solana DEX swap fee (default: 0.3%).
    """
    return trade_amount * fee_rate

def calculate_solana_transaction_fee():
    """
    Return Solana network transaction fee.
    """
    return 0.01  # Placeholder for actual Solana network fee
