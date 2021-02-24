from typing import Union

from data_sources.metrics import ChainMetricProvider
from data_sources.apicalls import retrieve_json, coin_gecko, print_red


def get_latest_block():
    """https://app.swaggerhub.com/apis-docs/V2261/solanabeach-backend_api/0.0.1"""
    return retrieve_json("https://api.solana.surf/v1/latest-blocks?limit=1")[0]


def get_network_health():
    """https://app.swaggerhub.com/apis-docs/V2261/solanabeach-backend_api/0.0.1"""
    return retrieve_json("https://api.solana.surf/v1/health")


class SolanaMetricProvider(ChainMetricProvider):
    latest_block: Union[None, dict]
    current_price: Union[None, float]

    def __init__(self):
        super().__init__("Solana")
        self.refresh()

    def refresh(self):
        try:
            self.latest_block = get_latest_block()
        except Exception:
            self.latest_block = None
            print_red(Exception)
        try:
            self.current_price = coin_gecko.get_price('solana', 'usd')['solana']['usd']
        except Exception:
            self.current_price = None
            print_red(Exception)

    def get_current_coin_price(self) -> Union[None, float]:
        return self.current_price

    def get_avg_gas_price(self) -> Union[None, float]:
        """https://docs.solana.com/introduction#what-are-sols"""
        return 0.000000001

    def get_avg_txn_gas(self) -> Union[None, int]:
        if self.latest_block is None:
            return None
        return self.latest_block['metrics']['totalfees'] / self.latest_block['metrics']['txcount']

    def get_avg_txn_price(self) -> Union[None, float]:
        if self.latest_block is None or self.current_price is None:
            return None
        return self.get_current_coin_price() * self.get_avg_gas_price() * self.get_avg_txn_gas()

    def get_avg_txn_time(self) -> Union[None, float]:
        return None

    def get_last_block_time(self) -> Union[None, float]:
        return None
