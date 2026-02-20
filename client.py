import os
from binance.client import Client
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)

TESTNET_URL = "https://testnet.binancefuture.com"

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API credentials not found.")

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = TESTNET_URL
        logger.info("Initialized Binance Futures Testnet client.")

    def create_order(self, **kwargs):
        try:
            logger.info(f"Sending order request: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logger.info(f"Received response: {response}")
            return response
        except Exception as e:
            logger.error(f"API Error: {str(e)}")
            raise      
