from src.arbitrage import calculate_arbitrage

def test_calculate_arbitrage():
    binance_price = 100
    solana_price = 105
    trade_amount = 10

    profit = calculate_arbitrage(binance_price, solana_price, trade_amount)
    assert profit > 0  # Should return a positive profit
