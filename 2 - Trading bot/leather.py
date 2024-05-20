class Leather:

    buy_amount = 500

    def __init__(self):
        self.usd_wallet = 1000
        self.btc_wallet = 0

    def buy(self, price):
        if self.usd_wallet > self.buy_amount:
            self.btc_wallet = 1 * self.buy_amount / price
            self.usd_wallet = self.usd_wallet - self.buy_amount
            # print("Buying at {}".format(price))

    def sell(self, price):
        # print("BTC WALLET BEFORE SELLING {}".format(self.btc_wallet))
        net = self.btc_wallet * price
        self.usd_wallet = self.usd_wallet + net
        self.btc_wallet = 0

        # print("Selling {} at {}".format(net, price))
        # print("Wallet now: {}".format(self.usd_wallet))
