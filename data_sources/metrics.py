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

    """Provides metrics related to blockchains like Solana and Ethereum."""
    def __init__(self, name):
        self.name = name

    """Result can either be None or float."""
    @abc.abstractmethod
    def get_current_coin_price(self) -> Union[None, float]:
        pass

    @abc.abstractmethod
    def get_avg_gas_price(self) -> Union[None, float]:
        pass

    @abc.abstractmethod
    def get_avg_txn_gas(self) -> Union[None, int]:
        pass

    @abc.abstractmethod
    def get_avg_txn_price(self) -> Union[None, float]:
        pass

    @abc.abstractmethod
    def get_avg_txn_time(self) -> Union[None, float]:
        pass

    @abc.abstractmethod
    def get_last_block_time(self) -> Union[None, float]:
        pass


class DexMetricProvider(MetricProvider, metaclass=abc.ABCMeta):
    name: str
    chain: ChainMetricProvider
    referral_link: str

    """Provides metrics related to DEXes like Serum and Uni or 1inch."""
    def __init__(self, name, chain, referral_link):
        self.name = name
        self.chain = chain
        self.referral_link = referral_link

    @abc.abstractmethod
    def get_current_tvl(self) -> Union[None, float]:
        """Returns tvl in USD"""
        pass

    @abc.abstractmethod
    def get_minimum_maximum_apy(self) -> (Union[None, float], Union[None, float]):
        pass

    @abc.abstractmethod
    def get_estimated_gas(self) -> Union[None, int]:
        pass
