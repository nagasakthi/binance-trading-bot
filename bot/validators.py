def validate(symbol, side, order_type, quantity, price, stop_price=None, client=None):
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must be like BTCUSDT")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Type must be MARKET / LIMIT / STOP_LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be > 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT")

    if order_type == "STOP_LIMIT":
        if price is None or stop_price is None:
            raise ValueError("STOP_LIMIT requires both price and stop_price")

        # 🔥 Advanced validation (very important)
        if client:
            current_price = float(
                client.futures_mark_price(symbol=symbol)["markPrice"]
            )

            if side == "BUY":
                if stop_price <= current_price:
                    raise ValueError(
                        f"BUY STOP_LIMIT: stop_price ({stop_price}) must be ABOVE current price ({current_price})"
                    )
                if price < stop_price:
                    raise ValueError(
                        "BUY STOP_LIMIT: price must be >= stop_price"
                    )

            elif side == "SELL":
                if stop_price >= current_price:
                    raise ValueError(
                        f"SELL STOP_LIMIT: stop_price ({stop_price}) must be BELOW current price ({current_price})"
                    )
                if price > stop_price:
                    raise ValueError(
                        "SELL STOP_LIMIT: price must be <= stop_price"
                    )

    return symbol, side, order_type