import pandas as pd


class ExchangeMetricsService:
    def __init__(self, db):
        self.db = db

    def get_df_by_exchange(self, exchange_code='') -> pd.DataFrame:
        return self.db.get_exchange_df(exchange_code)

