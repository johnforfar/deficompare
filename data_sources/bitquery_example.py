from datetime import datetime, timedelta
import pandas as pd

from data_sources.graphcalls import get_average_eth_like_gas, get_average_btc_like_fees

now = datetime.strptime("2021-05-19T16:00:00+02:00", "%Y-%m-%dT%H:%M:%S%z")

costs_eth = pd.Series(get_average_eth_like_gas("ethereum", now - timedelta(hours=2), now, timedelta(minutes=15)), name="ETH")
costs_etc = pd.Series(get_average_eth_like_gas("ethclassic", now - timedelta(hours=2), now, timedelta(minutes=15)), name="ETC")
costs_bsc = pd.Series(get_average_eth_like_gas("bsc", now - timedelta(hours=2), now, timedelta(minutes=15)), name="BNB")
costs_btc = pd.Series(get_average_btc_like_fees("bitcoin", now - timedelta(hours=2), now, timedelta(minutes=15)), name="BTC")
costs_doge = pd.Series(get_average_btc_like_fees("dogecoin", now - timedelta(hours=2), now, timedelta(minutes=15)), name="DOGE")
costs_ltc = pd.Series(get_average_btc_like_fees("litecoin", now - timedelta(hours=2), now, timedelta(minutes=15)), name="LTC")

series = [costs_eth, costs_etc, costs_bsc, costs_btc, costs_doge, costs_ltc]

df = pd.concat(series, axis=1)
print(df)