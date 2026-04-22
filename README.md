# Binance Futures Trading Bot (Testnet)

##  Overview
A Python CLI-based trading bot that places MARKET, LIMIT, and STOP-LIMIT orders on Binance Futures Testnet (USDT-M).  
Designed with clean architecture, input validation, logging, and error handling.

---

## Features
- MARKET, LIMIT, and STOP-LIMIT orders
- CLI-based input using Click
- Input validation (symbol, side, order type, price)
- Logging of API requests, responses, and errors
- Error handling for API and network issues
- Binance Futures Testnet integration

---

## Project Structure

trading_bot/
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ ├── logging_config.py
├── cli.py
├── config.py
├── requirements.txt
├── README.md


---

##  Setup

1. Clone repository:
```bash
git clone https://github.com/nagasakthi/binance-trading-bot.git
cd binance-trading-bot
Install dependencies:
pip install -r requirements.txt
Create .env file:
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret
 Run Examples
Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 80000
Stop-Limit Order (auto price supported)
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.01
 Sample Output
=== ORDER SUMMARY ===
BTCUSDT BUY MARKET qty=0.01

=== RESPONSE ===
Order ID: 12345678
Status: FILLED
Executed Qty: 0.0100
Avg Price: 77921.70

 Order executed successfully
 Notes
Uses Binance Futures Testnet (no real money)
STOP-LIMIT orders are conditional and may remain in NEW state until triggered
API keys must be stored in .env (not committed)
 Requirements
Python 3.x
python-binance
click
python-dotenv

---

#  Why this is better

| Improvement | Impact |
|------|--------|
| Sections (Overview, Setup, Examples) | Easy to read |
| Code blocks formatted | Professional |
| Project structure added | Shows organization |
| Sample output | Proves it works |
| Notes section | Shows understanding |

---

#  What to do now

1. Replace your README with this
2. Push:

```bash
git add README.md
git commit -m "Improve README"
git push
