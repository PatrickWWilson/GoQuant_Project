# Patrick Wilson GoQuant Project Test

import time
import ccxt

# Measure execution time for fetching ticker data
def benchmarkFetchTicker(exchange, symbol):
   
    startTime = time.time() # Record the start time before the API call
    ticker = exchange.fetch_ticker(symbol)
    endTime = time.time() # Record the end time after the API call

    # Print how long it took for this exchange to return the ticker
    print(f"{exchange.id}: {endTime - startTime:.6f} seconds")
    return ticker

# Test Code
if __name__ == "__main__":
    symbol = "BTC/USDT"
    exchanges = [ccxt.binance(), ccxt.kraken(), ccxt.coinbasepro()] # A list of exchange APIs to test

    print(f"Checking {symbol} prices and timing the API responses...\n")
    
    for exchange in exchanges:
        benchmarkFetchTicker(exchange, symbol) # Call function for each exchange
