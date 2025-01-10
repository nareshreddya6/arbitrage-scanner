from flask import Flask, jsonify, render_template
from src.binance_api import get_usdc_pairs
from src.solana_price import get_solana_price
from src.arbitrage import calculate_arbitrage

app = Flask(__name__)

# Route to serve the HTML page
@app.route("/")
def index():
    return render_template("index.html")  # Make sure the HTML file is in the 'templates' folder

# API route to fetch arbitrage opportunities
@app.route("/api/arbitrage", methods=["GET"])
def get_arbitrage_opportunities():
    # Fetch Binance USDC pairs
    binance_pairs = get_usdc_pairs()

    # Solana DEX pair addresses (example, replace with actual logic)
    solana_pair_address = "9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin"  # Example pair address

    opportunities = []
    for pair, binance_price in binance_pairs.items():
        # Solana pair token logic
        if pair not in ["DOGEUSDC", "SOLUSDC", "BONKUSDC"]:
            continue
        
        # Fetch Solana price
        solana_price = get_solana_price()

        # Arbitrage calculation
        trade_amount = 100  # Example trade amount
        profit = calculate_arbitrage(binance_price, solana_price, trade_amount)
        percentage_difference = ((solana_price - binance_price) / binance_price) * 100

        opportunities.append({
            "token": pair,
            "binancePrice": binance_price,
            "solanaPrice": solana_price,
            "priceDifference": solana_price - binance_price,
            "percentageDifference": percentage_difference,
            "profitAfterFees": profit,
            "volume24h": 15234567  # Replace with real data if available
        })
        print(opportunities)

    return jsonify(opportunities)

if __name__ == "__main__":
    app.run(debug=True)
