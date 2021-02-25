"""Here are 'soft' interfaces of ChainMetricProviders and other DeFi metric providers. These are subject to change."""
import abc
from typing import Union


class MetricProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def refresh(self):
        """Refreshes the underlying data by retrieving new data from called APIs."""
        pass


class ChainMetricProvider(MetricProvider, metaclass=abc.ABCMeta):
    name: str
    symbol: str
    coin_price: Union[None, float] = None
    avg_gas_price: Union[None, float] = None
    avg_tx_gas: Union[None, int] = None
    avg_tx_price: Union[None, float] = None
    avg_tx_time: Union[None, float] = None
    last_block_time: Union[None, float] = None

    """Provides metrics related to blockchains like Solana and Ethereum."""
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return f"""{self.name} ({self.symbol}):
    Coin price (USD): {self.coin_price}
    Avg-speed gas price ({self.symbol}): {self.avg_gas_price}
    Avg gas per tx: {self.avg_tx_gas:.0f}
    Avg-speed tx price (USD): {self.avg_tx_price:.5f}
    Avg tx time (sec): {self.avg_tx_time}
    Last block time (sec): {self.last_block_time}
    """


class DexMetricProvider(MetricProvider, metaclass=abc.ABCMeta):
    name: str
    chain: ChainMetricProvider
    referral_link: str
    total_value_locked: Union[None, float] = None
    min_apy: Union[None, float] = None
    avg_apy: Union[None, float] = None
    median_apy: Union[None, float] = None
    max_apy: Union[None, float] = None
    swap_cost: Union[None, float] = None
    staking_cost: Union[None, float] = None

    """Provides metrics related to DEXes like Serum and Uni or 1inch."""
    def __init__(self, name, chain, referral_link):
        self.name = name
        self.chain = chain
        self.referral_link = referral_link

    def __repr__(self):
        return f"""{self.name} ({self.referral_link}) on {self.chain.name}:
    Total value locked (USD): {self.total_value_locked:.2f}
    Min/Avg/Median/Max APY rounded: {self.min_apy}/{self.avg_apy}/{self.median_apy}/{self.max_apy}
    Predicted swap/staking cost (USD): {self.swap_cost:.5f}/{self.staking_cost:.5f}
    """
