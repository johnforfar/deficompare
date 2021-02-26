import datetime
from typing import Union

from data_sources.metrics import ChainMetricProvider
from data_sources.apicalls import retrieve_json, get_price, print_red


def get_latest_block() -> Union[None, dict]:
    """https://app.swaggerhub.com/apis-docs/V2261/solanabeach-backend_api/0.0.1"""
    try:
        return retrieve_json("https://api.solana.surf/v1/latest-blocks?limit=1")[0]
    except Exception:
        print_red(f"Unsucessful call to https://api.solana.surf/v1/latest-blocks?limit=1")
        return None


class SolanaMetricProvider(ChainMetricProvider):

    def __init__(self):
        super().__init__("Solana", "SOL")
        self.refresh()

    def refresh(self):
        latest_block = get_latest_block()
        self.coin_price = get_price('solana')
        self.avg_gas_price = 0.000000001  # https://docs.solana.com/introduction#what-are-sols
        if latest_block is not None:
            self.avg_tx_gas = latest_block['metrics']['totalfees'] / latest_block['metrics']['txcount']
            if self.coin_price is not None:
                self.avg_tx_price = self.coin_price * self.avg_gas_price * self.avg_tx_gas


