import json
from typing import Union
from pycoingecko import CoinGeckoAPI

import requests

"""https://pypi.org/project/pycoingecko/"""
coin_gecko = CoinGeckoAPI()


def retrieve_json(url) -> Union[list, dict, str, int, float, bool]:
    """May return a list of json objects or an object as a python dictionary,
    or any other data type depending on the called URL."""
    # TODO: Error/timeout handling?
    response = requests.request("GET", url)
    return response.json()


def retrieve_json_as_string(url) -> str:
    """A basic json dump."""
    response = requests.request("GET", url)
    return json.dumps(response.json(), sort_keys=True, indent=4)