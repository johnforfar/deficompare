import requests
import json
from metrics import Metrics


class EtheriumMetrics(Metrics):
    def __init__(self):
        self.url = "https://ethgasstation.info/api/ethgasAPI.json"

    def retrieve_json(self):
        response = requests.request("GET", self.url)
        return json.dumps(response.json(), sort_keys=True, indent=4)

    def get_fuel_price(self):
        pass

    def get_delay(self):
        pass

    def get_roi(self):
        pass