CEX/DEX Arbitrage Scanner

Overview:
This project is designed to identify arbitrage opportunities between centralized exchange (CEX) Binance and decentralized exchanges (DEX) on the Solana blockchain. It scans token pairs traded against USDC, calculates real-time price differences, and determines profitability after accounting for trading fees, network costs, and slippage.

Features:
Fetches real-time price data from:
Binance (CEX API)
Solana DEX (e.g., coingecko/Serum/Raydium) via RPC
Calculates arbitrage profitability considering:
Binance trading fees (0.1% maker/taker)
Solana DEX swap fees (0.3%)
Solana transaction costs
Potential slippage and execution risks
Displays actionable arbitrage opportunities.

Installations:
python-binance
requests
pytest
Flask==2.2.2
flask-cors==3.1.1
requests==2.28.1

Usage
Run the arbitrage scanner:


python run_arbitrage_scanner.py
The script will output potential arbitrage opportunities with the following details:

Token Pair (e.g., SOL/USDC)
Binance Price
Solana DEX Price
Potential Profit (after fees and costs)
Configuration
Binance Configuration
Configure your Binance API key and secret in config/binance_config.py:
sending the opportunities list to frontend to display the output on the page
Run:
flask run


pre requisites:
BINANCE_API_KEY = "your_api_key"
BINANCE_API_SECRET = "your_api_secret"

The output looks like this:
![image](https://github.com/user-attachments/assets/1c8ca727-f1a7-4ce7-908f-8d037e98fe09)
![Uploading image.png…]()

Solana Configuration
Set the Solana RPC URL in config/solana_config.py:




