import time
import database
# from data_sources.eth import EthereumMetricProvider
from metrics_service import MetricsService


class PollingManager:
    def __init__(self):
        db = database.SQLLiteDatabase()
        db.store_dummy_data()
        # etherium_metrics = EthereumMetricProvider()

        # TODO enable the polling loop
        # while True:
        #     # Main loop for polling APIs
        #
        #
        #     etherium_metrics = EthereumMetricProvider()
        #     # etherium_metrics.
        #     # TODO start with long delay for testing
        #     time.sleep(60)


polling_manager = PollingManager()

metrics_service = MetricsService()

