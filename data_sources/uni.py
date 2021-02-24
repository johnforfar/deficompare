from typing import Union

from data_sources.apicalls import retrieve_json, print_red
from data_sources.graphcalls import get_uniswap_tvl
from data_sources.metrics import DexMetricProvider, ChainMetricProvider
from data_sources.eth import EthereumMetricProvider


def get_all_pools():
    pools = retrieve_json("https://serum-api.bonfida.com/pools")
    return pools


class UniswapMetricProvider(DexMetricProvider):
    tvl: Union[None, dict]

    def __init__(self, chain: ChainMetricProvider = EthereumMetricProvider()):
        super().__init__("Uniswap V2", chain, "https://app.uniswap.org/")
        self.refresh()

    def refresh(self):
        try:
            self.tvl = get_uniswap_tvl()
        except Exception:
            self.tvl = None
            print_red(Exception)

    def get_estimated_swap_cost(self) -> Union[None, float]:
        return self.chain.get_avg_gas_price() * 200000 * self.chain.get_current_coin_price()

    def get_minimum_maximum_apy(self) -> (float, float):
        raise NotImplemented

    def get_current_tvl(self) -> Union[None, float]:
        return self.tvl
