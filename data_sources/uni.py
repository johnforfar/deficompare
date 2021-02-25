from typing import Union

from data_sources.apicalls import retrieve_json, print_red
from data_sources.graphcalls import get_uniswap_tvl
from data_sources.metrics import DexMetricProvider, ChainMetricProvider
from data_sources.eth import EthereumMetricProvider


class UniswapMetricProvider(DexMetricProvider):
    tvl: Union[None, dict]

    def __init__(self, chain: ChainMetricProvider = EthereumMetricProvider()):
        super().__init__("Uniswap V2", chain, "https://app.uniswap.org/")
        self.refresh()

    def refresh(self):
        try:
            self.total_value_locked = get_uniswap_tvl()
            self.min_apy
            self.avg_apy
            self.median_apy
            self.max_apy
            self.swap_cost = self.chain.avg_gas_price * 200000 * self.chain.coin_price
            self.staking_cost = self.chain.avg_gas_price * 175000 * self.chain.coin_price
        except Exception:
            print_red(Exception)
