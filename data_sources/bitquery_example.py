from datetime import datetime, timedelta, timezone
import pandas as pd
import numpy as np

from data_sources.bitquery import get_average_btc_like_fees, get_average_eth_like_gas
from data_sources.coingecko import get_historic_prices

tz = timezone(timedelta(hours=2))
interval = timedelta(minutes=15)
till = datetime.now(tz=tz)
since = till - timedelta(hours=6)

usd_prices = get_historic_prices("ethereum", since, till)
gas_prices = get_average_eth_like_gas("ethereum", since - interval, till, interval)

binned_prices = usd_prices.resample(interval).mean().interpolate()
binned_gas = gas_prices.resample(interval).mean().interpolate()
binned_txn_fees = pd.Series({timestamp: price * (binned_gas[timestamp] / 1e9) * 65000  # GWEI <-> ETH conversion
                             for timestamp, price in binned_prices.iteritems()}, name="erc20_transfer")

binned_prices.name = "coin_price"
binned_gas.name = "gas_price"
df = pd.concat([binned_prices, binned_gas, binned_txn_fees], axis=1)
print(df)


#costs_etc = pd.Series(get_average_eth_like_gas("ethclassic", now - timedelta(hours=2), now, timedelta(minutes=15)), name="ETC")
#costs_bsc = pd.Series(get_average_eth_like_gas("bsc", now - timedelta(hours=2), now, timedelta(minutes=15)), name="BNB")
#costs_btc = pd.Series(get_average_btc_like_fees("bitcoin", now - timedelta(hours=2), now, timedelta(minutes=15)), name="BTC")
#costs_doge = pd.Series(get_average_btc_like_fees("dogecoin", now - timedelta(hours=2), now, timedelta(minutes=15)), name="DOGE")
#costs_ltc = pd.Series(get_average_btc_like_fees("litecoin", now - timedelta(hours=2), now, timedelta(minutes=15)), name="LTC")
#series = [costs_eth, costs_etc, costs_bsc, costs_btc, costs_doge, costs_ltc]
#df = pd.concat(series, axis=1)
#print(df)
