import numpy as np
from typing import Union

from data_sources.apicalls import retrieve_json, print_red
from data_sources.metrics import DexMetricProvider, ChainMetricProvider
from data_sources.sol import SolanaMetricProvider


def get_all_pools() -> Union[None, dict]:
    try:
        pools = retrieve_json("https://serum-api.bonfida.com/pools")
        if pools['success'] == 'false':
            print_red(pools)
    except Exception:
        print_red(Exception)
        return None
    return pools


class SerumMetricProvider(DexMetricProvider):
    def __init__(self, chain: ChainMetricProvider = SolanaMetricProvider()):
        super().__init__("SerumSwap", chain, "https://swap.projectserum.com/")
        self.refresh()

    def refresh(self):
        self.swap_cost = self.chain.avg_tx_price
        self.staking_cost = self.swap_cost

        pools = get_all_pools()
        if pools is not None:
            self.total_value_locked = 0
            for pool in pools['data']:
                self.total_value_locked += pool['liquidity_locked']
            self.total_value_locked = round(self.total_value_locked, 2)

            apys = list(filter(lambda x: x > 0, [pool['apy'] for pool in pools['data']]))
            self.min_apy = round(np.min(apys).item(), 2)
            self.avg_apy = round(np.average(apys), 2)
            self.median_apy = round(np.median(apys).item(), 2)
            self.max_apy = round(np.max(apys).item(), 2)
