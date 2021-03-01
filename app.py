import os
import pathlib

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import plotly.graph_objs as go
import plotly.offline as pyo
import dash_daq as daq

#remove when launch
import dash_auth

import pandas as pd
import time

from polling_manager import PollingManager

import multiprocessing

from constants import SOLANA_TOKEN_CODE, ETHERIUM_TOKEN_CODE, UNISWAP_EXCHANGE_CODE, SERUM_EXCHANGE_CODE, POLLING_DELAY_SECONDS
from database import SQLLiteDatabase
from postgres_database import PostgresDatabase
from token_metrics_service import TokenMetricsService

import plotly.express as px


#remove when launch
USERNAME_PASSWORD_PAIRS = [
['defi', 'etherium']
]

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

#remove when launch
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)

server = app.server
app.config["suppress_callback_exceptions"] = True
app.title = 'DeFi Compare'

## Pull new API call data
try:
    use_postgres = os.environ['USE_POSTGRES']
    if bool(use_postgres):
        db = PostgresDatabase()
    else:
        db = SQLLiteDatabase()
except:
        db = SQLLiteDatabase()

token_metrics_service = TokenMetricsService(db=db)
sol_df_token = token_metrics_service.get_df_by_token(SOLANA_TOKEN_CODE)
print(f"Solana Token Data:{sol_df_token}")

eth_df_token = token_metrics_service.get_df_by_token(ETHERIUM_TOKEN_CODE)
print(f"Ethereum Token Data:{eth_df_token}")

## page header, about pop-up and logo
def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H5("DeFi Compare (BETA)"),
                    html.H6("A DeFi Dapp & Blockchain Comparison Tool"),
                ],
            ),
            #html.Div(
            #    id="banner-button",
            #    children=[daq.StopButton(id="stop-button", size=160, n_clicks=0)],
            #),
            html.Div(
                id="banner-logo",
                children=[
                    #html.Button(
                    #    id="learn-more-button", children="LEARN MORE", n_clicks=0
                    #),
                    "This is the banner",
                    html.Img(id="logo", src=app.get_asset_url("defi-hackathon.png")),
                ],
            ),
        ],
    )

def generate_section_banner(title):
    return html.Div(className="section-banner", children=title)

def build_fee_graph(df_token):
    print("hell yeah")
    return html.Div(
        id="control-chart-container",
        className="twelve columns",
        children=[
            generate_section_banner("Latency Chart"),
            dcc.Graph(
                id="control-chart-live",
                figure=go.Figure(
                    {
                        "data": [
                            {
                                "x": df_token['datetime'],
                                "y": df_token['avg_tx_price'],
                                "mode": "lines+markers",
                                "name": "Solana!",
                            }
                        ],
                        "layout": {
                            "paper_bgcolor": "rgba(0,0,0,0)",
                            "plot_bgcolor": "rgba(0,0,0,0)",
                            "xaxis": dict(
                                showline=False, showgrid=False, zeroline=False
                            ),
                            "yaxis": dict(
                                showgrid=False, showline=False, zeroline=False
                            ),
                            "autosize": True,
                        },
                    }
                ),
            ),
        ],
    )

app.layout = html.Div(
    id="big-app-container",
    children=[
        build_banner(),
        html.Div(
            id="app-container",
            children=[
                #build_tabs(),
                # Main app
                html.Div(
                    id="app-content",
                    children=[
                        "Main text 1  ",
                        build_fee_graph(sol_df_token),
                        #px.line(sol_df_token, x="datetime", y="avg_tx_price", line_shape="spline", render_mode="svg"),
                        "Main text 2  "
                    ],
                ),
            ],
        ),
    ],
)


def worker():
    """worker thread for running the polling and database updates"""

    try:
        use_postgres = os.environ['USE_POSTGRES']
        if bool(use_postgres):
            db = PostgresDatabase()
        else:
            db = SQLLiteDatabase()
    except:
        db = SQLLiteDatabase()

    polling_manager = PollingManager(db)
    while True:
        # Main loop for polling APIs
        polling_manager.poll()
        time.sleep(POLLING_DELAY_SECONDS)

# Running the server
if __name__ == "__main__":
    # Entry point for polling process
    p = multiprocessing.Process(target=worker, args=())
    p.start()

    app.run_server(debug=True, port=8050)