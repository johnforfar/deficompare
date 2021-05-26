import data_providers as dp
from constants import SOLANA_TOKEN_CODE, TOKEN_METRICS_SUFFIX, ETHERIUM_TOKEN_CODE, SERUM_EXCHANGE_CODE, \
    UNISWAP_EXCHANGE_CODE


class PollingManager:
    def __init__(self, db):
        self.db = db
        self.solana_metrics = dp.SolanaMetricProvider()  # constructor automatically polls data
        self.etherium_metrics = dp.EthereumMetricProvider()
        self.serum_metrics = dp.SerumMetricProvider()
        self.uniswap_metrics = dp.UniswapMetricProvider()

        print(self.solana_metrics)
        print(self.etherium_metrics)
        print(self.serum_metrics)
        print(self.uniswap_metrics)

    def poll(self):
        solana_data = self.solana_metrics.poll()
        self.solana_metrics.store_row_in_db(self.db, SOLANA_TOKEN_CODE, solana_data)

        etherium_data = self.etherium_metrics.poll()
        self.etherium_metrics.store_row_in_db(self.db, ETHERIUM_TOKEN_CODE, etherium_data)

        serum_data = self.serum_metrics.poll()
        self.serum_metrics.store_row_in_db(self.db, SERUM_EXCHANGE_CODE, serum_data)

        uniswap_data = self.uniswap_metrics.poll()
        self.uniswap_metrics.store_row_in_db(self.db, UNISWAP_EXCHANGE_CODE, uniswap_data)




