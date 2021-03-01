from typing import Union

from data_sources.metrics import ChainMetricProvider
from data_sources.apicalls import retrieve_json, get_price, print_red


def get_latest_blocks() -> Union[None, list]:
    """https://app.swaggerhub.com/apis-docs/V2261/solanabeach-backend_api/0.0.1"""
    try:
        return retrieve_json("https://api.solana.surf/v1/latest-blocks?limit=50")
    except Exception:
        print_red(f"Unsucessful call to https://api.solana.surf/v1/latest-blocks?limit=1")
        return None


class SolanaMetricProvider(ChainMetricProvider):

    def __init__(self):
        super().__init__("Solana", "SOL")
        self.refresh()

    def refresh(self):
        try:
            latest_blocks = get_latest_blocks()
            self.coin_price = get_price('solana')
            self.avg_gas_price = 0.000000001  # https://docs.solana.com/introduction#what-are-sols
            if latest_blocks is not None and len(latest_blocks) > 0:
                self.avg_tx_gas = latest_blocks[0]['metrics']['totalfees'] / latest_blocks[0]['metrics']['txcount']
                if self.coin_price is not None:
                    self.avg_tx_price = self.coin_price * self.avg_gas_price * self.avg_tx_gas
                self.avg_tx_time = (latest_blocks[0]['blocktime']['relative'] - latest_blocks[-1]['blocktime']['relative'])/len(latest_blocks)
                self.last_block_time = self.avg_tx_time  # can't find closer time

        except Exception as e:
            print(e)

