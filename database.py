#!/usr/bin/python

import sqlite3
import pandas as pd

from constants import TOKEN_CODES
from metrics_service import MetricsService

DB_NAME = 'db.db'

class SQLLiteDatabase:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)

        print(f"Opened {DB_NAME} successfully")

        # Create a table for each token
        for token_code in TOKEN_CODES:
            self.conn.execute(f'''CREATE TABLE IF NOT EXISTS {token_code}_metrics 
                     (id INT PRIMARY KEY     NOT NULL,
                     timestamp TIMESTAMP CURRENT_TIMESTAMP,
                     tx_fee            DOUBLE     NOT NULL,
                     tx_delay            DOUBLE     NOT NULL
                     );''')

        self.conn.close()

    def get_token_df(self, token_code) -> pd.DataFrame:
        """"""
        self.conn = sqlite3.connect(DB_NAME)

        print(f"Opened {DB_NAME} successfully")

        df = pd.read_sql_query(f"SELECT * from {token_code}_metrics", self.conn)

        self.conn.close()
        return df

    def store_dummy_data(self):
        """Just for development, storing test data"""
        self.conn = sqlite3.connect(DB_NAME)

        metric_service = MetricsService()
        eth_df = metric_service.get_dummy_data_eth()
        eth_df.to_sql("eth_metrics", self.conn, if_exists="replace")

        self.conn.close()

