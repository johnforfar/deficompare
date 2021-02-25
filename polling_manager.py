import data_sources as ds
from constants import SOLANA_TOKEN_CODE, TOKEN_METRICS_SUFFIX

# print(ds.SolanaMetricProvider())
# print(ds.SerumMetricProvider())
# print(ds.EthereumMetricProvider())
# print(ds.UniswapMetricProvider())


class PollingManager:
    def __init__(self, db):
        self.solana_metrics = ds.SolanaMetricProvider()
        solana_data = self.solana_metrics.poll()
        self.db = db
        self.db.sqlite_insert(f'{SOLANA_TOKEN_CODE}{TOKEN_METRICS_SUFFIX}', solana_data)

        self.etherium_metrics = ds.EthereumMetricProvider()
        self.serum_metrics = ds.SerumMetricProvider()
        self.uniswap_metrics = ds.UniswapMetricProvider()

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



