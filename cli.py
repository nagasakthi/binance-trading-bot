import click
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate
from bot.logging_config import setup_logging

setup_logging()

@click.command()
@click.option('--symbol', required=True)
@click.option('--side', required=True)
@click.option('--type', 'order_type', required=True)
@click.option('--quantity', required=True, type=float)
@click.option('--price', required=False, type=float)
@click.option('--stop_price', required=False, type=float)
def main(symbol, side, order_type, quantity, price, stop_price):
    try:
        # ✅ Normalize input
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        # ✅ Create client FIRST (needed for validation)
        client = get_client()

        #  AUTO calculate (ADD HERE)
        if order_type == "STOP_LIMIT" and side == "BUY":
            if price is None or stop_price is None:
                current_price = float(client.futures_mark_price(symbol=symbol)["markPrice"])
                stop_price = round(current_price + 300, 1)
                price = round(stop_price + 100, 1)

        # ✅ Validate input (with market price check)
        symbol, side, order_type = validate(
            symbol, side, order_type, quantity, price, stop_price, client
        )

        # ✅ Place order
        order = place_order(client, symbol, side, order_type, quantity, price, stop_price)
        # ✅ Handle missing orderId safely
        if not order.get("orderId"):
            print("⚠️ Order accepted but not fully registered yet")
            print("Raw Response:", order)
            return
        print("\n=== ORDER SUMMARY ===")

        if order_type == "STOP_LIMIT":
            print(f"{symbol} {side} {order_type} qty={quantity} price={price} stop_price={stop_price}")
        else:
            print(f"{symbol} {side} {order_type} qty={quantity} price={price}")

        print("\n=== RESPONSE ===")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice", "N/A"))

        # ✅ Clean status message
        if order.get("status") == "FILLED":
            print("\n✅ Order executed successfully")
        else:
            print("\n⚠️ Order placed but not filled yet")

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()