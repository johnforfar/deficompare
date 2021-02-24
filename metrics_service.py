import pandas as pd


class MetricsService:
    def __init__(self):
        pass

    def get_df_by_token(self, token_code='') -> pd.DataFrame:
        # TODO get this from db
        pass

    def get_dummy_data_eth(self, token_code='eth') -> pd.DataFrame:
        # Note: datetime is just python datetime.datetime.now()
        df = pd.DataFrame(
            [
                ['2021-02-24 21:20:00.000000', 1693.78, 110.0,   96.0,  3.9435454543623435, 12.804878048780488],
                ['2021-02-24 21:21:00.000000', 1507.78, 100.0,   60.0,  2.3435454353453243, 12.404761904761905],
                ['2021-02-24 21:22:00.000000', 1796.78, 140.0,   100.0, 4.1435454353453242, 13],
                ['2021-02-24 21:23:00.000000', 1592.78, 120.0,   93.0,  3.9435453454356346, 12.047619047619047],
                ['2021-02-24 21:24:00.000000', 1990.78, 110.0,   97.0,  3.9126317999999998, 12.047619047619047],
            ],
            columns=['datetime', 'current_coin_price', 'avg_gas_price', 'avg_txn_time', 'avg_txn_price', 'last_block_time']
        )
        return df

metric_service = MetricsService()
eth_df = metric_service.get_dummy_data_eth()
print(eth_df)

