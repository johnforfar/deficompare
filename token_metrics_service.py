import pandas as pd


class TokenMetricsService:
    def __init__(self, db):
        self.db = db

    def get_df_by_token(self, token_code='') -> pd.DataFrame:
        return self.db.get_token_df(token_code)

