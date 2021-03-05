# A place to keep all the important constants in one spot for now


# General
DB_NAME = 'db.db'
TOKEN_METRICS_SUFFIX = '_token_metrics'
EXCHANGE_METRICS_SUFFIX = '_exchange_metrics'
POLLING_DELAY_SECONDS = 180
DASHBOARD_REFRESH_SECONDS = 30
# BASED on 4 tables, this will bring limit to 8000
DB_TABLE_LIMIT = 2000
# This should never be above the table limit
DB_RESTRICTION_DELETE_COUNT = 100

# TODO store a copy of token and exchange codes in a db table

# Token codes
ETHERIUM_TOKEN_CODE = 'eth'
SOLANA_TOKEN_CODE = 'sol'


TOKEN_CODES = [ETHERIUM_TOKEN_CODE, SOLANA_TOKEN_CODE]

# Exchange codes
UNISWAP_EXCHANGE_CODE = 'uni'
SERUM_EXCHANGE_CODE = 'srm'

DEX_SYMBOLS = [UNISWAP_EXCHANGE_CODE, SERUM_EXCHANGE_CODE]

