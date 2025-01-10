import logging
import os
# Set up logging
log_dir = "data/logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename="data/logs/arbitrage.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def log_message(message):
    """
    Log a message to the arbitrage log file.
    """
    logging.info(message)
