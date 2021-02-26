import time

from constants import ETHERIUM_TOKEN_CODE, POLLING_DELAY_SECONDS
from database import SQLLiteDatabase

from token_metrics_service import TokenMetricsService
from exchange_metrics_service import ExchangeMetricsService
from polling_manager import PollingManager


# For now just a temp starting point for the backend testing


def main():
    db = SQLLiteDatabase()
    polling_manager = PollingManager(db)

    while True:
        # Main loop for polling APIs
        polling_manager.poll()
        time.sleep(POLLING_DELAY_SECONDS)


if __name__ == '__main__':
    main()

