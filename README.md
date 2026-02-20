# binance-futures-trading-bot

## Features
- Market Orders
- Limit Orders
- Stop-Limit Orders
- BUY & SELL
- CLI interface
- Logging & error handling
- Binance Futures Testnet ready

## Setup

pip install -r requirements.txt

Create .env with API credentials.

## Example Commands

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000

Stop-Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type STOP --quantity 0.001 --price 49000 --stop_price 49500
