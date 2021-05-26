from datetime import datetime, timedelta
from typing import Union

import pandas as pd
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

from data_sources import keys
from data_sources.helpers import print_red

bitquery_client = Client(
    transport=RequestsHTTPTransport(
        url="https://graphql.bitquery.io",
        headers={"X-API-KEY": keys.bitquery_api_key}))


def get_intervals(since, till, interval):
    num_intervals = int((till - since) / interval)
    return [since + interval * i for i in range(num_intervals + 1)]


def get_average_btc_like_fees(network: str, since: datetime, till: datetime = datetime.now(),
                              interval: timedelta = timedelta(minutes=5)) -> Union[None, pd.Series]:
    intervals = get_intervals(since, till, interval)
    query_str = "{{bitcoin(network: {} ) {{".format(network)
    interval_keys = [f"t{i}" for i in range(len(intervals) - 1)]
    for i, key in enumerate(interval_keys):
        query_str += "{}: transactions(time: {{ since: \"{}\", till: \"{}\" }}) {{ avgFee: feeValue(calculate: average) }}\n".format(
            key, intervals[i].isoformat(), intervals[i + 1].isoformat())
    query_str += "}}"

    try:
        query = gql(query_str)
        result = bitquery_client.execute(query)['bitcoin']
        return pd.Series({str(intervals[i + 1]): transactions_data[0]['avgFee']
                          for i, transactions_data in enumerate(result.values())})
    except Exception as e:
        print_red("Unsucessful call in graphcalls.get_average_btc_like_fees()")
        print(e)
        return None


def get_average_eth_like_gas(network: str, since: datetime, till: datetime = datetime.now(),
                             interval: timedelta = timedelta(minutes=5)) -> Union[None, pd.Series]:
    intervals = get_intervals(since, till, interval)
    query_str = "{{ethereum(network: {} ) {{".format(network)
    interval_keys = [f"t{i}" for i in range(len(intervals) - 1)]
    for i, key in enumerate(interval_keys):
        query_str += "{}: transactions(time: {{ since: \"{}\", till: \"{}\" }}) {{ gasPrice }}\n".format(
            key, intervals[i].isoformat(), intervals[i + 1].isoformat())
    query_str += "}}"

    try:
        query = gql(query_str)
        result = bitquery_client.execute(query)['ethereum']
        # timestamp : gas_price
        return pd.Series({intervals[i + 1]: int(transactions_data[0]['gasPrice'])
                          for i, transactions_data in enumerate(result.values())})
    except Exception as e:
        print_red("Unsucessful call in graphcalls.get_average_eth_like_gas()")
        print(e)
        return None
