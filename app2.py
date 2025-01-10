from flask import Flask, jsonify
from src.binance_api import get_usdc_pairs
from src.solana_dex_api import fetch_solana_price
from src.arbitrage import calculate_arbitrage
from src.utils import log_message
from src.solana_price import get_solana_price
from src.radaddpairs import raydiumpairs
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/arbitrage', methods=['GET'])
def get_arbitrage_opportunities():
    """
    This endpoint calculates arbitrage opportunities and returns the result as a JSON.
    """
    # Fetch Binance USDC pairs
    binance_pairs = get_usdc_pairs()
    arbitrage_opportunities = []

    for pair, binance_price in binance_pairs.items():
        # Example: Doge/USDC pair for the arbitrage check
        if pair not in ["DOGEUSDC"]:  # Replace with actual pairs to monitor
            continue
        
        # Fetch price from Solana DEX (You can replace this with actual Solana fetching logic)
        solana_price = get_solana_price()

        # Arbitrage calculation (example trade amount)
        trade_amount = 100
        profit = calculate_arbitrage(binance_price, solana_price, trade_amount)

        if profit > 0:
            message = f"Arbitrage Opportunity: {pair}, Profit: ${profit:.2f}"
            arbitrage_opportunities.append({
                'pair': pair,
                'binancePrice': binance_price,
                'solanaPrice': solana_price,
                'profit': profit,
                'message': message
            })
            log_message(message)

    return jsonify(arbitrage_opportunities)

if __name__ == '__main__':
    app.run(debug=True)
