import data_sources as ds
from constants import SOLANA_TOKEN_CODE, TOKEN_METRICS_SUFFIX, ETHERIUM_TOKEN_CODE, SERUM_EXCHANGE_CODE, \
    UNISWAP_EXCHANGE_CODE


class PollingManager:
    def __init__(self, db):
        self.solana_metrics = ds.SolanaMetricProvider()  # constructor automatically polls data
        solana_data = self.solana_metrics.to_dict()
        self.solana_metrics.store_row_in_db(db, SOLANA_TOKEN_CODE, solana_data)

        self.etherium_metrics = ds.EthereumMetricProvider()
        etherium_data = self.solana_metrics.to_dict()
        self.etherium_metrics.store_row_in_db(db, ETHERIUM_TOKEN_CODE, etherium_data)

        self.serum_metrics = ds.SerumMetricProvider()
        serum_data = self.serum_metrics.to_dict()
        self.serum_metrics.store_row_in_db(db, SERUM_EXCHANGE_CODE, serum_data)

        self.uniswap_metrics = ds.UniswapMetricProvider()
        uniswap_data = self.uniswap_metrics.to_dict()
        self.uniswap_metrics.store_row_in_db(db, UNISWAP_EXCHANGE_CODE, uniswap_data)

        print(self.solana_metrics)
        print(self.etherium_metrics)
        print(self.serum_metrics)
        print(self.uniswap_metrics)

        # TODO enable the polling loop
        # while True:
        #     # Main loop for polling APIs
        #
        #
        #     etherium_metrics = EthereumMetricProvider()
        #     # TODO start with long delay for testing
        #     time.sleep(60)



