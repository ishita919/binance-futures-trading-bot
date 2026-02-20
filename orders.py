import logging

logger = logging.getLogger(__name__)

class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_market_order(self, symbol, side, quantity):
        return self.client.create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        
      )
    def place_limit_order(self, symbol, side, quantity, price):
        return self.client.create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )

    # BONUS: Stop-Limit Order
    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        return self.client.create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=quantity,
            price=price,
            stopPrice=stop_price,
            timeInForce="GTC",
        )
