"""Here are 'soft' interfaces of ChainMetricProviders and other DeFi metric providers. These are subject to change."""


class ChainMetricProvider:
    name: str

    """Provides metrics related to blockchains like Solana and Ethereum."""
    def __init__(self, name):
        self.name = name

    def _retrieve_json(self) -> str:
        """Should be private or removed, as not every API provides JSON."""
        pass

    def get_current_gas_price(self) -> float:
        pass

    def get_last_block_time(self) -> float:
        pass

    def get_current_coin_price(self) -> float:
        pass

    # TODO: Find out whether we receive a time series of past prices or if we are only able to calculate current prices.


class DexMetricProvider:
    name: str
    referral_link: str

    """Provides metrics related to DEXes like Serum and Uni or 1inch."""
    def __init__(self, name):
        self.name = name

    def get_current_tvl(self) -> float:
        pass

    def get_minimum_maximum_apy(self) -> (float, float):
        pass

    def get_estimated_gas(self) -> int:
        pass
