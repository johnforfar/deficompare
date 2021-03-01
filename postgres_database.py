#!/usr/bin/python

# import sqlite3
import pandas as pd

from constants import DB_NAME, TOKEN_METRICS_SUFFIX, EXCHANGE_METRICS_SUFFIX, UNISWAP_EXCHANGE_CODE, SOLANA_TOKEN_CODE, \
    ETHERIUM_TOKEN_CODE, SERUM_EXCHANGE_CODE, TOKEN_CODES, DEX_SYMBOLS
from exchange_metrics_service import ExchangeMetricsService
from token_metrics_service import TokenMetricsService
import psycopg2
from psycopg2.extras import execute_values


class PostgresDatabase:
    def __init__(self):
        conn = self.connect()
        cursor = conn.cursor()

        print(f"Opened {DB_NAME} successfully")
        commands = []
        # Create a table for each token
        for token_code in TOKEN_CODES:
            commands.append(f'''CREATE TABLE IF NOT EXISTS {token_code}{TOKEN_METRICS_SUFFIX}
                     (id BIGSERIAL PRIMARY KEY,
                     datetime DATE,
                     current_coin_price DOUBLE PRECISION,
                     avg_gas_price DOUBLE PRECISION,
                     avg_tx_time DOUBLE PRECISION,
                     avg_tx_price DOUBLE PRECISION,
                     last_block_time DOUBLE PRECISION
                     );''')

        # Create a table for each dex
        for symbol in DEX_SYMBOLS:
            commands.append(f'''CREATE TABLE IF NOT EXISTS {symbol}{EXCHANGE_METRICS_SUFFIX}
                     (id BIGSERIAL PRIMARY KEY,
                     datetime DATE,
                     current_token_price DOUBLE PRECISION,
                     total_value_locked DOUBLE PRECISION,
                     min_apy DOUBLE PRECISION,
                     avg_apy DOUBLE PRECISION,
                     max_apy DOUBLE PRECISION,
                     swap_cost DOUBLE PRECISION,
                     staking_cost DOUBLE PRECISION
                     );''')
        for command in commands:
            cursor.execute(command)
        cursor.close()
        conn.commit()


    def get_token_df(self, token_code) -> pd.DataFrame:
        """"""
        conn = self.connect()
        cursor = conn.cursor()
        print(f"Opened {DB_NAME} successfully")

        df = pd.read_sql_query(f"SELECT * from {token_code}{TOKEN_METRICS_SUFFIX}", conn)

        cursor.close()
        return df


    def connect(self):
        """ Connect to the PostgreSQL database server """
        # conn = None
        try:

            # connect to the PostgreSQL server
            conn = psycopg2.connect(
                host="localhost",
                database="defi_compare",
                user="postgres",
                # password="password",
                port=5432)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return conn

    def get_exchange_df(self, exchange_code) -> pd.DataFrame:
        """"""
        conn = self.connect()
        cursor = conn.cursor()
        print(f"Opened {DB_NAME} successfully")

        df = pd.read_sql_query(f"SELECT * from {exchange_code}{EXCHANGE_METRICS_SUFFIX}", conn)

        cursor.close()
        return df

    def get_next_index_increment(self, table):
        """Quick and easy way to get the next index, auto increment not working with sqlite_insert"""
        conn = self.connect()
        cursor = conn.cursor()
        query = f"""SELECT MAX(id) FROM {table}"""
        cursor.execute(query)
        res = self.cursor.fetchone()
        cursor.close()
        return int(res[0]) + 1

    def sqlite_insert(self, table, row):

        conn = self.connect()
        cursor = conn.cursor()

        rows = [row]
        # keys = row.keys()
        # columns = ', '.join(keys)
        # vals = ', '.join('"{}"'.format(col) for col in row.values())
        # sql = 'insert into {0} ({1}) values ({2})'.format(table, columns, vals)
        columns = rows[0].keys()
        query = "INSERT INTO {0} ({1}) VALUES %s".format(table, ','.join(columns))

        # convert projects values to sequence of seqeences
        values = [[value for value in project.values()] for project in rows]

        execute_values(cursor, query, values)

        conn.commit()
        conn.close()

    def store_dummy_data(self):
        """Just for development, storing test data"""
        conn = self.connect()

        # Add tokens - manually for now
        token_metrics_service = TokenMetricsService(self)

        eth_df = token_metrics_service.get_dummy_data_eth()
        eth_df.to_sql(f"{ETHERIUM_TOKEN_CODE}{TOKEN_METRICS_SUFFIX}", conn, if_exists="replace", index_label='id')
        sol_df = token_metrics_service.get_dummy_data_sol()
        sol_df.to_sql(f"{SOLANA_TOKEN_CODE}{TOKEN_METRICS_SUFFIX}", conn, if_exists="replace", index_label='id')

        exchange_metrics_service = ExchangeMetricsService(self)
        uniswap_df = exchange_metrics_service.get_dummy_data_uniswap()
        uniswap_df.to_sql(f"{UNISWAP_EXCHANGE_CODE}{EXCHANGE_METRICS_SUFFIX}", conn, if_exists="replace", index_label='id')
        serum_df = exchange_metrics_service.get_dummy_data_serum()
        serum_df.to_sql(f"{SERUM_EXCHANGE_CODE}{EXCHANGE_METRICS_SUFFIX}", conn, if_exists="replace", index_label='id')


        conn.close()

