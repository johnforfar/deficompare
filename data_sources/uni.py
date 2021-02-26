from data_sources.apicalls import get_price
from data_sources.graphcalls import get_uniswap_tvl
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

        # TODO: Add APY

#provider = UniMetricProvider()
#print(provider)