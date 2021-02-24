from data_sources.metrics import ChainMetricProvider
from data_sources.apicalls import retrieve_json, coin_gecko


def get_eth_gas_json():
    """https://docs.ethgasstation.info/gas-price"""
    return retrieve_json("https://ethgasstation.info/api/ethgasAPI.json")


class EthereumMetricProvider(ChainMetricProvider):
    eth_gas_json: dict

    def __init__(self):
        super().__init__("Ethereum")
        self.refresh()

    def refresh(self):
        self.eth_gas_json = get_eth_gas_json()
        print(self.eth_gas_json)

    def get_current_coin_price(self) -> float:
        return coin_gecko.get_price('ethereum', 'usd')['ethereum']['usd']

    def get_avg_gas_price(self) -> float:
        return self.eth_gas_json["average"]/10

    def get_avg_txn_gas(self) -> int:
        return 21000

    def get_avg_txn_price(self) -> float:
        return self.get_current_coin_price() * (self.get_avg_gas_price() / 1e9) * self.get_avg_txn_gas()

    def get_avg_txn_time(self) -> float:
        return self.eth_gas_json["avgWait"]*60

    def get_last_block_time(self) -> float:
        return self.eth_gas_json["block_time"]


#provider = EthereumMetricProvider()

#print(provider.get_current_coin_price())
#print(provider.get_avg_gas_price())
#print(provider.get_avg_txn_time())
#print(provider.get_avg_txn_price())
