from constants import ETHERIUM_TOKEN_CODE
from database import SQLLiteDatabase

from token_metrics_service import TokenMetricsService
from exchange_metrics_service import ExchangeMetricsService
from polling_manager import PollingManager


# For now just a temp starting point for the backend testing


def main():
    db = SQLLiteDatabase()
    # TODO rm dummy data for prod
    db.store_dummy_data()

    polling_manager = PollingManager(db)
    exchange_metrics_service = ExchangeMetricsService(db)
    token_metrics_service = TokenMetricsService(db)
    # eth_df = token_metrics_service.get_df_by_token(ETHERIUM_TOKEN_CODE)
    #
    # print(eth_df)

if __name__ == '__main__':
    main()

