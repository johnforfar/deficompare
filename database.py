#!/usr/bin/python

import sqlite3


class SQLLiteDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('test.db')

        print("Opened database successfully")

        self.conn.execute('''CREATE TABLE IF NOT EXISTS eth_metrics 
                 (id INT PRIMARY KEY     NOT NULL,
                 timestamp TIMESTAMP CURRENT_TIMESTAMP,
                 tx_fee            DOUBLE     NOT NULL,
                 tx_delay            DOUBLE     NOT NULL
                 );''')

        self.conn.execute('''CREATE TABLE IF NOT EXISTS sol_metrics 
                 (id INT PRIMARY KEY     NOT NULL,
                 timestamp TIMESTAMP CURRENT_TIMESTAMP,
                 tx_fee            DOUBLE     NOT NULL,
                 tx_delay            DOUBLE     NOT NULL
                 );''')
        self.conn.close()




