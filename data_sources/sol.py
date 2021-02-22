from data_sources.metrics import ChainMetricProvider
from data_sources.apicalls import retrieve_json, coin_gecko

from solana.rpc.api import Client

"""https://michaelhly.github.io/solana-py/"""
sol_client = Client("https://devnet.solana.com")


class SolanaMetricProvider(ChainMetricProvider):
    lamports: int

    def __init__(self):
        super().__init__("Ethereum")
        self.refresh()

    def refresh(self):
        """https://michaelhly.github.io/solana-py/api.html#solana.rpc.api.Client.get_fees"""
        result = sol_client.get_fees()['result']
        self.lamports = result['value']['feeCalculator']['lamportsPerSignature']

    def get_current_coin_price(self) -> float:
        return coin_gecko.get_price('solana', 'usd')['solana']['usd']

    def get_avg_gas_price(self) -> float:
        return NotImplemented

    def get_avg_txn_gas(self) -> int:
        return self.lamports

    def get_avg_txn_price(self) -> float:
        return self.get_current_coin_price() * (self.get_avg_gas_price() / 1e9) * self.get_avg_txn_gas()

    def get_avg_txn_time(self) -> float:
        return NotImplemented

    def get_last_block_time(self) -> float:
        return NotImplemented


provider = SolanaMetricProvider()

print(provider.get_current_coin_price())
print(provider.get_avg_txn_gas())
#print(provider.get_avg_txn_time())
#print(provider.get_avg_txn_price())
