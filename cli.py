import argparse
import logging
from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
)
from bot.logging_config import setup_logging

def main():
    setup_logging()
    logger = logging.getLogger("CLI")

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")
    parser.add_argument("--stop_price")

    args = parser.parse_args()

    try:
        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)

        client = BinanceFuturesClient()
        manager = OrderManager(client)

        print("\n===== ORDER SUMMARY =====")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")
        if args.stop_price:
            print(f"Stop Price: {args.stop_price}")
        print("=========================\n")

        if args.type == "MARKET":
            response = manager.place_market_order(
                args.symbol, args.side, args.quantity
            )

        elif args.type == "LIMIT":
            if not args.price:
                raise ValueError("LIMIT order requires --price.")
            response = manager.place_limit_order(
                args.symbol, args.side, args.quantity, args.price
            )

        elif args.type == "STOP":
            if not args.price or not args.stop_price:
                raise ValueError("STOP order requires --price and --stop_price.")
            response = manager.place_stop_limit_order(
                args.symbol, args.side, args.quantity, args.price, args.stop_price
            )

        print("✅ Order Placed Successfully!")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

    except Exception as e:
        logger.error(str(e))
        print("❌ Order Failed:", str(e))

if __name__ == "__main__":
    main()
