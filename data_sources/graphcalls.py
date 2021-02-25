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
        result = uniswap_client.execute(query)
        return float(result['uniswapFactories'][0]['totalLiquidityUSD'])
    except Exception:
        print_red("Unsucessful call to https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2)")
        return None
