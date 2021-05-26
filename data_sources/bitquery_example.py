from datetime import datetime, timedelta
import pandas as pd

from data_sources.bitquery import get_average_btc_like_fees, get_average_eth_like_gas
from data_sources.coingecko import get_historic_prices

till = datetime.now()
since = till - timedelta(days=8)
costs_eth = pd.Series(get_average_eth_like_gas("ethereum", since, till, timedelta(minutes=15)), name="avg_gas")
price_eth = pd.Series(get_historic_prices("ethereum", since, till), name="price")



#costs_etc = pd.Series(get_average_eth_like_gas("ethclassic", now - timedelta(hours=2), now, timedelta(minutes=15)), name="ETC")
#costs_bsc = pd.Series(get_average_eth_like_gas("bsc", now - timedelta(hours=2), now, timedelta(minutes=15)), name="BNB")
#costs_btc = pd.Series(get_average_btc_like_fees("bitcoin", now - timedelta(hours=2), now, timedelta(minutes=15)), name="BTC")
#costs_doge = pd.Series(get_average_btc_like_fees("dogecoin", now - timedelta(hours=2), now, timedelta(minutes=15)), name="DOGE")
#costs_ltc = pd.Series(get_average_btc_like_fees("litecoin", now - timedelta(hours=2), now, timedelta(minutes=15)), name="LTC")
#series = [costs_eth, costs_etc, costs_bsc, costs_btc, costs_doge, costs_ltc]
#df = pd.concat(series, axis=1)
#print(df)
