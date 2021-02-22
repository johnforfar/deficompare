import requests
import json
from data_sources.metrics import ChainMetricProvider


class EthereumConnector(ChainMetricProvider):
    def __init__(self):
        super().__init__()
        self.url = "https://ethgasstation.info/api/ethgasAPI.json"

    def _retrieve_json(self):
        response = requests.request("GET", self.url)
        return json.dumps(response.json(), sort_keys=True, indent=4)

    def get_current_gas_price(self):
        pass

    def get_last_block_time(self):
        pass

    def get_current_coin_price(self):
        pass