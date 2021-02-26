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
                ['2021-02-24 21:20:00.000000', 0, 4255567402.04, None, None, None, 47.46517, 41.53202],
                ['2021-02-24 21:21:00.000000', 0, 4257493715.98, None, None, None, 49.60139, 43.40121],
                ['2021-02-24 21:22:00.000000', 0, 4256536161.94, None, None, None, 49.60139, 43.40121],
                ['2021-02-24 21:23:00.000000', 0, 4257648853.70, None, None, None, 49.60139, 43.40121],
                ['2021-02-24 21:24:00.000000', 0, 4257648853.70, None, None, None, 49.60139, 43.40121],
            ],
            columns=['datetime', 'current_token_price', 'total_value_locked', 'min_apy', 'avg_apy', 'max_apy', 'swap_cost', 'staking_cost']
        )
        return df

    def get_dummy_data_serum(self) -> pd.DataFrame:
        # Note: datetime is just python datetime.datetime.now()
        df = pd.DataFrame(
            [
                ['2021-02-24 21:20:00.000000', 0, 27311270.76, 0.01, 2.26, 14.87, 0.00008, 0.00008],
                ['2021-02-24 21:21:00.000000', 0, 27411270.76, 0.01, 2.26, 14.87, 0.00008, 0.00008],
                ['2021-02-24 21:22:00.000000', 0, 27511270.76, 0.01, 2.26, 14.87, 0.00008, 0.00008],
                ['2021-02-24 21:23:00.000000', 0, 27611270.76, 0.01, 2.26, 14.87, 0.00008, 0.00008],
                ['2021-02-24 21:24:00.000000', 0, 27711270.76, 0.01, 2.26, 14.87, 0.00008, 0.00008],

            ],
            columns=['datetime', 'current_token_price', 'total_value_locked', 'min_apy', 'avg_apy', 'max_apy', 'swap_cost', 'staking_cost']
        )
        return df

