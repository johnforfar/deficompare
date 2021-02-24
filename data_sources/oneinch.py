from typing import Union

from data_sources.apicalls import retrieve_json
from data_sources.metrics import DexMetricProvider, ChainMetricProvider
from data_sources.eth import EthereumMetricProvider


def get_all_pools():
    pools = retrieve_json("https://serum-api.bonfida.com/pools")
    return pools


class OneInchMetricProvider(DexMetricProvider):
    pools_resp: dict

    def __init__(self, chain: ChainMetricProvider = EthereumMetricProvider()):
        super().__init__("SerumSwap", chain, "https://swap.projectserum.com/")
        self.refresh()

    def refresh(self):
        self.pools_resp = get_all_pools()

    def get_estimated_gas(self) -> Union[None, int]:
        return self.chain.get_avg_txn_gas()

    def get_minimum_maximum_apy(self) -> (float, float):
        raise NotImplemented

    def get_current_tvl(self) -> Union[None, float]:
        if self.pools_resp['success'] == 'false':
            return None

        tvl = 0
        for pool in self.pools_resp['data']:
            tvl += pool['liquidity_locked']
        return round(tvl, 2)
