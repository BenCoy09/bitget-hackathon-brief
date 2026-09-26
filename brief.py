import requests
from datetime import datetime

def get_ticker(symbol):
    url = f"https://api.bitget.com/api/v2/spot/market/tickers?symbol={symbol}"
    r = requests.get(url)
    data = r.json()
    if data.get("data"):
        return data["data"][0]
    return None

def get_candles(symbol, granularity="1h", limit=48):
    url = f"https://api.bitget.com/api/v2/spot/market/candles?symbol={symbol}&granularity={granularity}&limit={limit}"
    r = requests.get(url)
    data = r.json()
    return data.get("data", [])

def analyze(symbol):
    ticker = get_ticker(symbol)
    candles = get_candles(symbol)

    if not ticker or not candles:
        return f"Could not fetch data for {symbol}. Check the symbol or try again."

    last_price = float(ticker["lastPr"])
    change_24h = float(ticker["change24h"]) * 100
    volume_24h = float(ticker["baseVolume"])

    closes = [float(c[4]) for c in candles]
    avg_price_48h = sum(closes) / len(closes)

    price_vs_avg = ((last_price - avg_price_48h) / avg_price_48h) * 100

    volumes = [float(c[5]) for c in candles]
    avg_volume = sum(volumes) / len(volumes)
    recent_volume = volumes[-1]
    volume_spike = recent_volume > (avg_volume * 1.5)

    if change_24h > 3 and price_vs_avg < 2 and not volume_spike:
        signal = "GOOD ENTRY POINT"
        reason = "Price is rising but still near its 48h average, with no unusual volume spike suggesting a blow-off top."
    elif volume_spike and change_24h > 5:
        signal = "WAIT"
        reason = "Sharp price rise combined with a volume spike often signals short-term overextension."
    elif change_24h < -3:
        signal = "WAIT"
        reason = "Price is dropping; entering now risks catching a continued downtrend."
    else:
        signal = "NEUTRAL - WATCH"
        reason = "No strong signal either way. Price action is roughly stable."

    brief = f"""
DAILY BRIEF - {symbol}
Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}

Last Price: {last_price}
24h Change: {change_24h:.2f}%
Price vs 48h Average: {price_vs_avg:.2f}%
Volume Spike Detected: {volume_spike}

SIGNAL: {signal}
REASON: {reason}

--- For educational research purposes only. Not financial advice. ---
"""
    return brief

if __name__ == "__main__":
    symbol = input("Enter symbol (e.g. BTCUSDT): ").strip().upper()
    print(analyze(symbol))
