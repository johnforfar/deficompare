import time
import database
from etherium_metrics import EtheriumMetrics


class PollingManager:
    def __init__(self):
        db = database.SQLLiteDatabase()
        etherium_metrics = EtheriumMetrics()

        # TODO enable the polling loop
        # while True:
        #     # Main loop for polling APIs
        #
        #
        #     etherium_metrics = EtheriumMetrics()
        #     # etherium_metrics.
        #     # TODO start with long delay for testing
        #     time.sleep(60)


polling_manager = PollingManager()


