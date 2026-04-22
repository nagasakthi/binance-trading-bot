import logging
import time

def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side,
            "quantity": quantity
        }

        if order_type == "MARKET":
            params["type"] = "MARKET"

        elif order_type == "LIMIT":
            params["type"] = "LIMIT"
            params["price"] = price
            params["timeInForce"] = "GTC"

        elif order_type == "STOP_LIMIT":
            params["type"] = "STOP"
            params["price"] = price
            params["stopPrice"] = stop_price
            params["timeInForce"] = "GTC"

        logging.info(f"Request: {params}")

        # ✅ Place order
        order = client.futures_create_order(**params)
        logging.info(f"Initial Response: {order}")

        # 🔥 SAFE handling
        order_id = order.get("orderId")

        if not order_id:
            logging.warning("orderId not found, returning raw response")
            return order  # avoid crash

        # ✅ Wait and fetch updated status
        time.sleep(2)

        updated = client.futures_get_order(
            symbol=symbol,
            orderId=order_id
        )

        logging.info(f"Updated Response: {updated}")

        return updated

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise