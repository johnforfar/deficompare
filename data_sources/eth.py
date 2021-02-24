from typing import Union

from data_sources.metrics import ChainMetricProvider
from data_sources.apicalls import retrieve_json, coin_gecko, print_red


def get_eth_gas_json():
    """https://docs.ethgasstation.info/gas-price"""
    return retrieve_json("https://ethgasstation.info/api/ethgasAPI.json")


class EthereumMetricProvider(ChainMetricProvider):
    eth_gas_json: Union[None, dict]
    current_price: Union[None, float]

    def __init__(self):
        super().__init__("Ethereum")
        self.refresh()

    def refresh(self):
        try:
            self.eth_gas_json = get_eth_gas_json()
        except Exception:
            print_red(Exception)
            self.eth_gas_json = None
        try:
            self.current_price = coin_gecko.get_price('ethereum', 'usd')['ethereum']['usd']
        except Exception:
            print_red(Exception)
            self.current_price = None

    def get_current_coin_price(self) -> Union[None, float]:
        return self.current_price

    def get_avg_gas_price(self) -> Union[None, float]:
        if self.eth_gas_json is None:
            return None
        return self.eth_gas_json["average"]/10

    def get_avg_txn_gas(self) -> Union[None, int]:
        return 21000

    def get_avg_txn_price(self) -> Union[None, float]:
        if self.eth_gas_json is None or self.current_price is None:
            return None
        return self.get_current_coin_price() * (self.get_avg_gas_price() / 1e9) * self.get_avg_txn_gas()

    def get_avg_txn_time(self) -> Union[None, float]:
        if self.eth_gas_json is None:
            return None
        return self.eth_gas_json["avgWait"]*60

    def get_last_block_time(self) -> Union[None, float]:
        if self.eth_gas_json is None:
            return None
        return self.eth_gas_json["block_time"]


