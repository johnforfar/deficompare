from data_sources.metrics import ChainMetricProvider
from data_sources.requests import retrieve_json, retrieve_json_as_string


def get_eth_gas_json():
    """Does the same as retrieve_json() in the earlier version."""
    return retrieve_json_as_string("https://ethgasstation.info/api/ethgasAPI.json")


class EthereumMetricProvider(ChainMetricProvider):
    def __init__(self):
        super().__init__("Ethereum")

    def get_current_gas_price(self):
        pass

    def get_last_block_time(self):
        pass

    def get_current_coin_price(self):
        pass
