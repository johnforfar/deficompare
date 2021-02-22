import json
from typing import Union

import requests


def retrieve_json(url) -> Union[dict, list]:
    """May return a list of json objects or an object as a python dictionary, depending on the called URL."""
    response = requests.request("GET", url)
    return response.json()


def retrieve_json_as_string(url) -> str:
    """A basic json dump."""
    response = requests.request("GET", url)
    return json.dumps(response.json(), sort_keys=True, indent=4)