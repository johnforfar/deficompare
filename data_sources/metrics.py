"""Here are 'soft' interfaces of ChainMetricProviders and other DeFi metric providers. These are subject to change."""
import abc
import datetime
from typing import Union

from constants import TOKEN_METRICS_SUFFIX, EXCHANGE_METRICS_SUFFIX


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

    def to_dict(self):
        return {
            'datetime': datetime.datetime.now(),
            'current_coin_price': self.coin_price,
            'avg_gas_price': self.avg_gas_price,
            'avg_tx_time': self.avg_tx_time,
            'avg_tx_price': self.avg_tx_price,
            'last_block_time': self.last_block_time
        }

    def poll(self):
        self.refresh()
        return self.to_dict()

    def store_row_in_db(self, db, code, data):
        db.sqlite_insert(f'{code}{TOKEN_METRICS_SUFFIX}', data)


class DexMetricProvider(MetricProvider, metaclass=abc.ABCMeta):
    name: str
    symbol: str
    chain: ChainMetricProvider
    referral_link: str
    total_value_locked: Union[None, float] = None
    token_price: Union[None, float] = None
    min_apy: Union[None, float] = None
    avg_apy: Union[None, float] = None
    median_apy: Union[None, float] = None
    max_apy: Union[None, float] = None
    swap_cost: Union[None, float] = None
    staking_cost: Union[None, float] = None

    """Provides metrics related to DEXes like Serum and Uni or 1inch."""
    def __init__(self, name, symbol, chain, referral_link):
        self.name = name
        self.symbol = symbol
        self.chain = chain
        self.referral_link = referral_link

    def __repr__(self):
        return f"""{self.name} ({self.referral_link}) on {self.chain.name}:
    Token price (USD): {self.token_price}
    Total value locked (USD): {self.total_value_locked:.2f}
    Min/Avg/Median/Max APY rounded: {self.min_apy}/{self.avg_apy}/{self.median_apy}/{self.max_apy}
    Predicted swap/staking cost (USD): {self.swap_cost:.5f}/{self.staking_cost:.5f}
    """

    def to_dict(self):
        return {
            'datetime': datetime.datetime.now(),
            'current_token_price': self.token_price,
            'total_value_locked': self.total_value_locked,
            'min_apy': self.min_apy,
            'avg_apy': self.avg_apy,
            'max_apy': self.max_apy,
            'swap_cost': self.swap_cost,
            'staking_cost': self.staking_cost
        }

    def poll(self):
        self.refresh()
        return self.to_dict()

    def store_row_in_db(self, db, code, data):
        db.sqlite_insert(f'{code}{EXCHANGE_METRICS_SUFFIX}', data)

