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
                      #"cardano": "cardano",
                      "dogecoin": "dogecoin"}

eth_likes = ["ethereum", "ethclassic", "bsc"]
btc_likes = ["bitcash", "litecoin", "bitcash", "dash", "cardano", "dogecoin"]


def get_prices_and_fees(name, since=None, till=None, interval=None):
    print(f"Getting {network} prices and fees...")
    if name in eth_likes:
        return _get_eth_like_price_gas_fees(name, since, till, interval)
    elif name in btc_likes:
        return _get_btc_like_price_gas_fees(name, since, till, interval)
    else:
        print(f"{name} does not exist.")
        return None


def _get_eth_like_price_gas_fees(network, since=None, till=None, interval=None):
    if interval is None:
        interval = timedelta(minutes=15)
    if till is None:
        till = datetime.now(tz=tz)
    if since is None:
        since = till - timedelta(minutes=15)

    gas_prices = get_average_eth_like_gas(network, since - interval, till, interval)
    usd_prices = get_historic_prices(bitquery_to_cg_ids[network], since, till)
    if gas_prices is None or usd_prices is None:
        return None

    binned_prices = usd_prices.resample(interval).mean().interpolate()
    binned_gas = gas_prices.resample(interval).mean().interpolate()
    binned_txn_fees = pd.Series({timestamp: price * (binned_gas[timestamp] / 1e9) * 65000  # GWEI <-> ETH conversion
                                 for timestamp, price in binned_prices.iteritems()}, name="avg_txn_price")

    binned_prices.name = "avg_price"
    df = pd.concat([binned_prices, binned_txn_fees], axis=1)
    df.name = network
    return df.assign(name=network)


def _get_btc_like_price_gas_fees(network, since=None, till=None, interval=None):
    if interval is None:
        interval = timedelta(minutes=60)
    if till is None:
        till = datetime.now(tz=tz)
    if since is None:
        since = till - timedelta(minutes=60)

    coin_fees = get_average_btc_like_fees(network, since - interval, till, interval)
    usd_prices = get_historic_prices(bitquery_to_cg_ids[network], since, till)
    if coin_fees is None or usd_prices is None:
        return None

    binned_prices = usd_prices.resample(interval).mean().interpolate()
    binned_fees = coin_fees.resample(interval).mean().interpolate()
    binned_txn_fees = pd.Series({timestamp: price * binned_fees[timestamp]  # GWEI <-> ETH conversion
                                 for timestamp, price in binned_prices.iteritems()}, name="avg_txn_price")

    binned_prices.name = "avg_price"
    df = pd.concat([binned_prices, binned_txn_fees], axis=1)
    df.name = network
    return df.assign(name=network)

from data_sources.hasura import insert_network_coins

now = datetime.now(tz=tz)
till = now
since = till - timedelta(hours=12)
interval = timedelta(minutes=15)

for network in bitquery_to_cg_ids.keys():
    df = get_prices_and_fees(network, since, till, interval)
    if df is None:
        continue
    insert_network_coins(df)
