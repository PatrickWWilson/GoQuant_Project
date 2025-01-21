# Patrick Wilson GoQuant Project Test

import time
import ccxt

# Measure execution time for fetching ticker data
def benchmarkFetchTicker(exchange, symbol):
   
    startTime = time.time() # Record the start time before the API call
    ticker = exchange.fetch_ticker(symbol)
    endTime = time.time() # Record the end time after the API call
    timeTaken = endTime - startTime  # Calculate elapsed time
    
    price = ticker['last']  # Get the latest price

    # Print the exchange name, price, and time taken
    print(f"{exchange.id}: Price = ${price:.2f}, Time = {timeTaken:.6f} seconds")
    
    return price, timeTaken

# Test Code
if __name__ == "__main__":
    symbol = "BTC/USDT"
    exchanges = [ccxt.binance(), ccxt.kraken(), ccxt.coinbase()] # A list of exchange APIs to test

    print(f"Checking {symbol} prices and timing the API responses...\n")
    
    for exchange in exchanges:
        benchmarkFetchTicker(exchange, symbol) # Call function for each exchange
