"""
Market Alert Bot

Simple crypto/stock price monitor with console alerts.
Supports custom thresholds.

Author: Peter
"""

import requests
import time
import argparse
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def get_crypto_price(symbol="BTCUSDT"):
    """Fetch crypto price from Binance API."""
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return float(data["price"])
    except Exception as e:
        logging.error(f"Failed to fetch price for {symbol}: {e}")
        return None

def monitor_price(symbol, target_price, condition="above", interval=60):
    """Monitor price loop."""
    logging.info(f"Starting monitor for {symbol}. Alert when {condition} {target_price}.")
    
    while True:
        price = get_crypto_price(symbol)
        
        if price:
            logging.info(f"Current {symbol} Price: ${price:.2f}")
            
            if condition == "above" and price >= target_price:
                print(f"\n[ALERT] {symbol} is ABOVE {target_price}! Current: ${price:.2f}\n")
                break
            elif condition == "below" and price <= target_price:
                print(f"\n[ALERT] {symbol} is BELOW {target_price}! Current: ${price:.2f}\n")
                break
        
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crypto Price Alert")
    parser.add_argument("symbol", help="Symbol pair (e.g., BTCUSDT)")
    parser.add_argument("target", type=float, help="Target price")
    parser.add_argument("--condition", choices=["above", "below"], default="above", help="Alert condition")
    parser.add_argument("--interval", type=int, default=60, help="Check interval in seconds")

    args = parser.parse_args()
    
    monitor_price(args.symbol, args.target, args.condition, args.interval)
