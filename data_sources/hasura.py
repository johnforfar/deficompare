import json
import re

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

import pandas as pd
import codecs

from data_sources.helpers import print_red
from data_sources.keys import hasura_graphql_url, hasura_admin_secret

hasura_client = Client(
    transport=RequestsHTTPTransport(
        url=hasura_graphql_url, headers={'content-type': 'application/json',
                                         'x-hasura-admin-secret': hasura_admin_secret}))


def insert_network_coins(df: pd.DataFrame):
    """Inserts or ignores if already present. If new data is added, put in update_columns!"""

    df_records = df.to_dict(orient='index')
    records = []
    for key, values in df_records.items():
        record = {"time": key.isoformat()}
        record.update(values)
        records.append(record)
    records_str = re.sub(r'(?<!: )"(\S*?)"', '\\1', json.dumps(records))
    query = gql(
        codecs.decode(rf"""mutation {{
            insert_network_coins(objects: {records_str},
                on_conflict: {{constraint: network_coins_pkey, update_columns: []}}) {{
                returning {{
                    time
                    name
                }}
            }}
        }}""", 'unicode_escape')
    )
    result = hasura_client.execute(query)
    print(result)
    return result
