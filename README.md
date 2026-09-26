# Bitget Market Brief

A lightweight Python market-research tool built for the Bitget AI Base Camp Hackathon. It retrieves live Bitget spot-market data and generates a concise market brief.

## Features

- Fetches live Bitget spot ticker data
- Retrieves recent hourly candlestick data
- Calculates 24h price change
- Calculates a 48-hour average price
- Compares current price with the 48-hour average
- Detects unusual recent volume activity
- Generates a concise market-analysis brief
- Runs directly from the command line

## Requirements

- Python 3
- Internet connection
- `requests` Python package

## Installation
From the project directory, install the required package:

pip3 install requests

## Usage

python3 brief.py

You'll be prompted to enter a symbol, e.g. BTCUSDT.

## Example Output

DAILY BRIEF - BTCUSDT
Last Price: 84313.55
24h Change: 0.41%
Price vs 48h Average: 0.23%
SIGNAL: NEUTRAL - WATCH
REASON: No strong signal either way.

## Disclaimer

For educational research purposes only. Not financial advice.

## Built For

Bitget AI Base Camp Hackathon S2 — AI Trading Desk track.
