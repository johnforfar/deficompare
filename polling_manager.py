import time
import database
from data_sources import EthereumConnector


class PollingManager:
    def __init__(self):
        db = database.SQLLiteDatabase()
        etherium_metrics = EthereumConnector()

        # TODO enable the polling loop
        # while True:
        #     # Main loop for polling APIs
        #
        #
        #     etherium_metrics = EthereumConnector()
        #     # etherium_metrics.
        #     # TODO start with long delay for testing
        #     time.sleep(60)


polling_manager = PollingManager()


