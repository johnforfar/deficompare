from typing import Union

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from data_sources.apicalls import print_red

uniswap_client = Client(transport=RequestsHTTPTransport(url="https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2"))


def get_uniswap_tvl() -> Union[None, float]:
    try:
        query = gql(
            """{
                uniswapFactories(first: 1) {
                    totalLiquidityUSD
                }
            }"""
        )
        return uniswap_client.execute(query)['data']['uniswapFactory']['totalLiquidityUSD']
    except Exception:
        print_red(Exception)
        return None
