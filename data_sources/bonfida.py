from data_sources.requests import retrieve_json


def get_all_pools():
    pools = retrieve_json("https://serum-api.bonfida.com/pools")
    return pools
