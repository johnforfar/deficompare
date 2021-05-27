from datetime import datetime, timedelta, timezone
import pandas as pd
import numpy as np

from data_sources.bitquery import get_average_btc_like_fees, get_average_eth_like_gas
from data_sources.coingecko import get_historic_prices

tz = timezone(timedelta(hours=2))

bitquery_to_cg_ids = {"ethereum": "ethereum",
                      "ethclassic": "ethereum-classic",
                      "bsc": "binancecoin",
                      "bitcoin": "bitcoin",
                      "litecoin": "litecoin",
                      "bitcash": "bitcoin-cash",
                      "dash": "dash",
                      "cardano": "cardano",
                      "dogecoin": "dogecoin"}


def get_eth_price_and_fees(since=None, till=None, interval=None):
    return _get_eth_like_price_gas_fees("ethereum", since, till, interval)


def get_bsc_price_and_fees(since=None, till=None, interval=None):
    return _get_eth_like_price_gas_fees("bsc", since, till, interval)


def get_etc_price_and_fees(since=None, till=None, interval=None):
    return _get_eth_like_price_gas_fees("ethclassic", since, till, interval)


def get_btc_price_and_fees(since=None, till=None, interval=None):
    return _get_btc_like_price_gas_fees("bitcoin", since, till, interval)


def get_ltc_price_and_fees(since=None, till=None, interval=None):
    return _get_btc_like_price_gas_fees("litecoin", since, till, interval)


def get_bch_price_and_fees(since=None, till=None, interval=None):
    return _get_btc_like_price_gas_fees("bitcash", since, till, interval)


def get_dash_price_and_fees(since=None, till=None, interval=None):
    return _get_btc_like_price_gas_fees("dash", since, till, interval)


def get_ada_price_and_fees(since=None, till=None, interval=None):
    return _get_btc_like_price_gas_fees("cardano", since, till, interval)


def get_doge_price_and_fees(since=None, till=None, interval=None):
    return _get_btc_like_price_gas_fees("dogecoin", since, till, interval)


def _get_eth_like_price_gas_fees(network, since=None, till=None, interval=None):
    if interval is None:
        interval = timedelta(minutes=15)
    if till is None:
        till = datetime.now(tz=tz)
    if since is None:
        since = till - timedelta(minutes=15)

    gas_prices = get_average_eth_like_gas(network, since - interval, till, interval)
    usd_prices = get_historic_prices(bitquery_to_cg_ids[network], since, till)

    binned_prices = usd_prices.resample(interval).mean().interpolate()
    binned_gas = gas_prices.resample(interval).mean().interpolate()
    binned_txn_fees = pd.Series({timestamp: price * (binned_gas[timestamp] / 1e9) * 65000  # GWEI <-> ETH conversion
                                 for timestamp, price in binned_prices.iteritems()}, name="erc20_transfer")

    binned_prices.name = "coin_price"
    binned_gas.name = "gas_price"
    df = pd.concat([binned_prices, binned_gas, binned_txn_fees], axis=1)
    df.name = network
    return df


def _get_btc_like_price_gas_fees(network, since=None, till=None, interval=None):
    if interval is None:
        interval = timedelta(minutes=60)
    if till is None:
        till = datetime.now(tz=tz)
    if since is None:
        since = till - timedelta(minutes=60)

    coin_fees = get_average_btc_like_fees(network, since - interval, till, interval)
    usd_prices = get_historic_prices(bitquery_to_cg_ids[network], since, till)

    binned_prices = usd_prices.resample(interval).mean().interpolate()
    binned_fees = coin_fees.resample(interval).mean().interpolate()
    binned_txn_fees = pd.Series({timestamp: price * binned_fees[timestamp]  # GWEI <-> ETH conversion
                                 for timestamp, price in binned_prices.iteritems()}, name="transaction_cost")

    binned_prices.name = "coin_price"
    binned_fees.name = "coin_fee"
    df = pd.concat([binned_prices, binned_fees, binned_txn_fees], axis=1)
    df.name = network
    return df

#print(get_eth_price_and_fees())
#print(get_bnb_price_and_fees())
#print(get_etc_price_and_fees())
#print(get_btc_price_and_fees())
#print(get_ltc_price_and_fees())
#print(get_bch_price_and_fees())
#print(get_dash_price_and_fees())
#print(get_ada_price_and_fees())
#print(get_doge_price_and_fees())

# costs_etc = pd.Series(get_average_eth_like_gas("ethclassic", now - timedelta(hours=2), now, timedelta(minutes=15)), name="ETC")
# costs_bsc = pd.Series(get_average_eth_like_gas("bsc", now - timedelta(hours=2), now, timedelta(minutes=15)), name="BNB")
# costs_btc = pd.Series(get_average_btc_like_fees("bitcoin", now - timedelta(hours=2), now, timedelta(minutes=15)), name="BTC")
# costs_doge = pd.Series(get_average_btc_like_fees("dogecoin", now - timedelta(hours=2), now, timedelta(minutes=15)), name="DOGE")
# costs_ltc = pd.Series(get_average_btc_like_fees("litecoin", now - timedelta(hours=2), now, timedelta(minutes=15)), name="LTC")
# series = [costs_eth, costs_etc, costs_bsc, costs_btc, costs_doge, costs_ltc]
# df = pd.concat(series, axis=1)
# print(df)
