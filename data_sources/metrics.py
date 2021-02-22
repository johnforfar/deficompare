

class ChainMetricProvider:
    url: str
    name: str

    """Provides metrics related to blockchains like Solana and Ethereum."""
    def __init__(self):
        url = None
        name = None

    def _retrieve_json(self) -> str:
        """Should be private or removed, as not every API provides JSON."""
        pass

    def get_current_gas_price(self):
        pass

    def get_last_block_time(self):
        pass

    def get_current_coin_price(self):
        pass

    # TODO: Find out whether we receive a time series of past prices or if we are only able to calculate current prices.


class DexMetricProvider:
    url: str
    name: str
    referral_link: str

    """Provides metrics related to DEXes like Serum and Uni or 1inch."""
    def __init__(self):
        url = None
        name = None

    def get_current_tvl(self) -> float:
        pass

    def get_minimum_maximum_apy(self) -> (float, float):
        pass

    def get_estimated_gas(self) -> int:
        pass
