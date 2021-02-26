import time
import numpy as np

from data_sources.apicalls import get_price
from data_sources.graphcalls import get_uniswap_tvl, get_uniswap_daily_pools, get_uniswap_pools
from data_sources.metrics import DexMetricProvider, ChainMetricProvider
from data_sources.eth import EthereumMetricProvider


class UniswapMetricProvider(DexMetricProvider):

    def __init__(self, chain: ChainMetricProvider = EthereumMetricProvider()):
        super().__init__("Uniswap V2", "UNI", chain, "https://app.uniswap.org/")
        self.refresh()

    def refresh(self):
        self.total_value_locked = get_uniswap_tvl()
        self.token_price = get_price('uniswap')
        if self.chain.avg_gas_price is not None and self.chain.coin_price is not None:
            self.swap_cost = self.chain.avg_gas_price * 200000 * self.chain.coin_price
            self.staking_cost = self.chain.avg_gas_price * 175000 * self.chain.coin_price

        volumes = get_uniswap_daily_pools(int(time.time()) - 86400)
        print(len(volumes))
        apys = [(float(pool['dailyVolumeUSD']) * 0.003 * 365 / float(pool['reserveUSD'])) * 100 for pool in volumes]
        self.min_apy = round(np.min(apys).item(), 2)
        self.avg_apy = round(np.average(apys), 2)
        self.median_apy = round(np.median(apys).item(), 2)
        self.max_apy = round(np.max(apys).item(), 2)
