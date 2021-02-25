import pandas as pd


class ExchangeMetricsService:
    def __init__(self, db):
        self.db = db

    def get_df_by_exchange(self, exchange_code='') -> pd.DataFrame:
        return self.db.get_exchange_df(exchange_code)

    def get_dummy_data_uniswap(self) -> pd.DataFrame:
        # Note: datetime is just python datetime.datetime.now()
        df = pd.DataFrame(
            [
                ['2021-02-24 21:20:00.000000', 4255567402.04, None, None, None, None, 47.46517, 41.53202],
                ['2021-02-24 21:21:00.000000', 4257493715.98, None, None, None, None, 49.60139, 43.40121],
                ['2021-02-24 21:22:00.000000', 4256536161.94, None, None, None, None, 49.60139, 43.40121],
                ['2021-02-24 21:23:00.000000', 4257648853.70, None, None, None, None, 49.60139, 43.40121],
                ['2021-02-24 21:24:00.000000', 4257648853.70, None, None, None, None, 49.60139, 43.40121],
            ],
            columns=['datetime', 'total_value_locked', 'apy_min','apy_max','apy_med','apy_avg', 'est_swap_cost', 'est_staking_cost']
        )
        return df
