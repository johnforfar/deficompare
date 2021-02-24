from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

uniswap_client = Client(transport=RequestsHTTPTransport(url="https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2"))


def get_uniswap_tvl() -> dict:
    query = gql(
        """{
            uniswapFactories(first: 1) {
                totalLiquidityUSD
            }
        }"""
    )
    return uniswap_client.execute(query)
