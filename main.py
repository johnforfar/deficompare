from constants import ETHERIUM_CODE
from database import SQLLiteDatabase
from metrics_service import MetricsService
from polling_manager import PollingManager


# For now just a temp starting point for the backend testing
def main():
    db = SQLLiteDatabase()
    # TODO rm dummy data for prod
    db.store_dummy_data()

    polling_manager = PollingManager()
    metrics_service = MetricsService(db)
    eth_df = metrics_service.get_df_by_token(ETHERIUM_CODE)

    print(eth_df)

if __name__ == '__main__':
    main()

