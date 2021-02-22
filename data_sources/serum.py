from data_sources.requests import retrieve_json
from data_sources.metrics import DexMetricProvider


def get_all_pools():
    pools = retrieve_json("https://serum-api.bonfida.com/pools")
    return pools


class SerumMetricProvider(DexMetricProvider):
    def __init__(self):
        super().__init__("Serum")

    def get_estimated_gas(self) -> int:
        pass

    def get_minimum_maximum_apy(self) -> (float, float):
        pass

    def get_current_tvl(self) -> float:
        pass
