def validate_symbol(symbol):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs are allowed (e.g., BTCUSDT).")

def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")

def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP.")

def validate_quantity(quantity):
    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0.")
