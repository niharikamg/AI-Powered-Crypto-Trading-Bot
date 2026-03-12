import os
from binance.client import Client

class TradingService:
    def __init__(self):
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = Client(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_SECRET_KEY"))
        return self._client

    def get_balance(self):
        return self.client.get_account()

    def execute_trade(self, symbol="BTCUSDT", quantity=0.01, trade_type="BUY"):
        order = self.client.order_market(symbol=symbol, side=trade_type, quantity=quantity)
        return order
