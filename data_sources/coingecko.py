from datetime import datetime
from typing import Union

import pandas as pd

from pycoingecko import CoinGeckoAPI

from data_sources.helpers import print_red

"""https://pypi.org/project/pycoingecko/"""
coin_gecko = CoinGeckoAPI()


def get_price(cg_id: str) -> Union[None, float]:
    try:
        return coin_gecko.get_price(cg_id, 'usd')[cg_id]['usd']
    except Exception as Arguments:
        print_red(f"Unsucessful call in coin_gecko.get_price: {Arguments}")
        return None


def get_historic_prices(cg_id: str, since: datetime, till: datetime) -> Union[None, pd.Series]:
    try:
        response = coin_gecko.get_coin_market_chart_range_by_id(cg_id, 'usd', int(since.timestamp()), int(till.timestamp()))
        return pd.Series({datetime.fromtimestamp(item[0]/1000, tz=since.tzinfo): item[1] for item in response['prices']})
    except Exception as Arguments:
        print_red(f"Unsucessful call in coin_gecko.get_historic_prices: {Arguments}")
        return None
