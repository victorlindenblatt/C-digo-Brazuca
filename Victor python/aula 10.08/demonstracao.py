class Wallet:
    def __init__(self, btc=0, eth=0, matic=0):
        self.btc = btc
        self.eth = eth
        self.matic = matic

    def __str__(self):
        return f"{self.btc} BTC, {self.eth} ETH, {self.matic} MATIC"

    def __add__(self, other, ):
        btc = self.btc + other.btc 
        eth = self.eth + other.eth 
        matic = self.matic + other.matic 
        return Wallet(btc, eth, matic)


vitin = Wallet(1, 2, 3)
rodrigo = Wallet(3, 2, 1)
victor = Wallet(3, 3, 3)
gabriel = Wallet(5, 5, 5)
total = vitin + rodrigo + victor + gabriel
print(total)