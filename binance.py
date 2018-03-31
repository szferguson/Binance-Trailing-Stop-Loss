import ccxt

class Binance():

    def __init__(self, api_key, api_secret):
        self.ccxtClient = ccxt.binance({
            'apiKey': api_key,
            'secret': api_secret,
        })

    def buy(self, market, amount, price):
        return (self.ccxtClient.create_order(
            symbol=market,
            type="limit",
            side="buy",
            amount=amount,
            price=price,
        ))

    def sell(self, market, amount, price):
        return (self.ccxtClient.create_order(
            symbol=market,
            type="limit",
            side="sell",
            amount=amount,
            price=price,
        ))

    def get_price(self, market):
        return float(self.ccxtClient.fetch_ticker(market)['info']['lastPrice'])

    def get_balance(self, coin):
        return float(self.ccxtClient.fetch_balance()[coin]['free'])
