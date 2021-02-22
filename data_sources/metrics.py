"""Here are 'soft' interfaces of ChainMetricProviders and other DeFi metric providers. These are subject to change."""
import abc


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

    @abc.abstractmethod
    def get_current_coin_price(self) -> float:
        pass

    @abc.abstractmethod
    def get_avg_gas_price(self) -> float:
        pass

    @abc.abstractmethod
    def get_avg_txn_gas(self) -> int:
        pass

    @abc.abstractmethod
    def get_avg_txn_price(self) -> float:
        pass

    @abc.abstractmethod
    def get_avg_txn_time(self) -> float:
        pass

    @abc.abstractmethod
    def get_last_block_time(self) -> float:
        pass

    # TODO: Find out whether we receive a time series of past prices or if we are only able to calculate current prices.


class DexMetricProvider(MetricProvider, metaclass=abc.ABCMeta):
    name: str
    referral_link: str

    """Provides metrics related to DEXes like Serum and Uni or 1inch."""
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def get_current_tvl(self) -> float:
        pass

    @abc.abstractmethod
    def get_minimum_maximum_apy(self) -> (float, float):
        pass

    @abc.abstractmethod
    def get_estimated_gas(self) -> int:
        pass
