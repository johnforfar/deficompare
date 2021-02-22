from data_sources.metrics import ChainMetricProvider
from data_sources.apicalls import retrieve_json, retrieve_json_as_string


def get_eth_gas_json():
    """https://docs.ethgasstation.info/gas-price"""
    return retrieve_json("https://ethgasstation.info/api/ethgasAPI.json")


class EthereumMetricProvider(ChainMetricProvider):
    eth_gas_json: dict

    def refresh(self):
        self.eth_gas_json = get_eth_gas_json()

    def __init__(self):
        super().__init__("Ethereum")
        self.refresh()

    def get_current_gas_price(self) -> float:
        return self.eth_gas_json["average"]/10

    def get_last_block_time(self) -> float:
        return self.eth_gas_json["avgWait"]*60

    def get_current_coin_price(self) -> float:
        pass
