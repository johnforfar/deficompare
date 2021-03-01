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

import pandas as pd
import time

from polling_manager import PollingManager

from threading import Thread

from constants import SOLANA_TOKEN_CODE, ETHERIUM_TOKEN_CODE, UNISWAP_EXCHANGE_CODE, SERUM_EXCHANGE_CODE, \
    POLLING_DELAY_SECONDS, DASHBOARD_REFRESH_SECONDS
from database import SQLLiteDatabase
from postgres_database import PostgresDatabase
from token_metrics_service import TokenMetricsService

import plotly.express as px
from apscheduler.schedulers.blocking import BlockingScheduler

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

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

@app.callback(Output('control-chart-live', 'figure'),
        [Input('graph-update', 'n_intervals')])
def build_fee_graph(n):
    df_token_1 = "SOL"
    df_token_2 = "ETH"

    df_token_1_data = token_metrics_service.get_df_by_token(SOLANA_TOKEN_CODE)
    df_token_2_data = token_metrics_service.get_df_by_token(ETHERIUM_TOKEN_CODE)

    # Create graph plots
    token_1_plot = go.Scatter(
        x=df_token_1_data['datetime'],
        y=df_token_1_data['avg_tx_price'],
        mode='lines+markers',
        name='SOL Fees'
    )
    token_2_plot = go.Scatter(
        x=df_token_2_data['datetime'],
        y=df_token_2_data['avg_tx_price'],
        mode='lines+markers',
        name='ETH Fees'
    )
    neo_graph_df = [token_1_plot, token_2_plot]

    fee_graph_title = 'Fee Comparison of ' + df_token_1 + ' and ' + df_token_2 + " in USD"

    return {
        "data": neo_graph_df,
        "layout": {
            "paper_bgcolor": "rgba(0,0,0,0)",
            "plot_bgcolor": "rgba(0,0,0,0)",
            "xaxis": dict(
                showline=False, showgrid=False, zeroline=False
            ),
            "yaxis": dict(
                showgrid=False, showline=False, zeroline=False
            ),
            "legend": dict(
                orientation="h"
            ),
            "autosize": True,
            "title": fee_graph_title,
        },
    }

def serve_layout():
    df_token_1 = "SOL"
    df_token_2 = "ETH"

    # fake token selector
    all_tokens = ["SOL", "ETH", "ADA"]

    fee_graph_title = 'Fee Comparison of ' + df_token_1 + ' and ' + df_token_2 + " in USD"

    return html.Div(
    id="big-app-container",
    children=[
            build_banner(),
            html.Div(
                id="app-container",
                children=[
                    # Main app
                    html.Div(
                        id="app-content",
                        children=[
                            html.Div(
                                id="control-chart-container",
                                className="twelve columns",
                                children=[
                                    generate_section_banner(fee_graph_title),
                                    dcc.Graph(
                                        id="control-chart-live",
                                        animate=True
                                    ),
                                    dcc.Interval(
                                        id='graph-update',
                                        interval=1000*DASHBOARD_REFRESH_SECONDS,
                                        n_intervals=0
                                    ),
                                    html.Div([
                                        html.P("Fake Checklist"),
                                        dcc.Checklist(
                                            id="checklist",
                                            options=[{"label": x, "value": x}
                                                     for x in all_tokens],
                                            value=all_tokens[:2],
                                            labelStyle={'display': 'inline-block'}
                                        ),
                                    ])
                                ],
                            )
                        ],
                    ),
                ],
            ),
        ],
    )


app.layout = serve_layout


# Running the server
if __name__ == "__main__":
    app.run_server(debug=False, port=8050)





