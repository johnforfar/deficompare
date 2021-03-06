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
import numpy as np
import time
import datetime

from polling_manager import PollingManager

from threading import Thread

from constants import SOLANA_TOKEN_CODE, ETHERIUM_TOKEN_CODE, UNISWAP_EXCHANGE_CODE, SERUM_EXCHANGE_CODE, \
    POLLING_DELAY_SECONDS, DASHBOARD_REFRESH_SECONDS
from database import SQLLiteDatabase
from postgres_database import PostgresDatabase
from token_metrics_service import TokenMetricsService
from exchange_metrics_service import ExchangeMetricsService

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
        db = PostgresDatabase()    #comment out for local testing
        #db = SQLLiteDatabase()      #enable for local testing
    else:
        db = SQLLiteDatabase()
except:
        db = SQLLiteDatabase()

token_metrics_service = TokenMetricsService(db=db)
exchange_metrics_service = ExchangeMetricsService(db=db)

##== PAGE HEADER =========================================================================================================

def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H5("DeFi Compare (ALPHA)"),
                    html.H6("An open and fair DeFi comparison tool across all blockchains and decentralised finance applications"),
                ],
            ),
            html.Div(
                id="banner-logo",
                children=[
                    html.Label(['DeFi Hackathon Project > ', html.A(' VOTE NOW ', href='https://airtable.com/shrsx1ltpQfTt9wT6')]),
                    html.Label([' | ', html.A(' Twitter ', href='https://twitter.com/solanablog/')]),
                    html.Label([' | ', html.A(' Discord ', href='https://discord.gg/mrpPmnJJ')]),              
                    html.Img(id="logo", src=app.get_asset_url("defi-compare-logo_wide.png")),
                ],
            ),
        ],
    )

def generate_section_banner(title):
    return html.Div(className="section-banner", children=title)

##== PAGE HEADER =========================================================================================================

def build_dapp_table():
    df_symbol_1 = "SRM"
    df_symbol_2 = "UNI"

    df_exch_1_data = exchange_metrics_service.get_df_by_exchange(SERUM_EXCHANGE_CODE)
    df_exch_2_data = exchange_metrics_service.get_df_by_exchange(UNISWAP_EXCHANGE_CODE)

    print(df_exch_1_data)
    print(df_exch_2_data)

    df_exch_1_data_tailed = df_exch_1_data.tail(1)
    df_exch_2_data_tailed = df_exch_2_data.tail(1)

    df_exch_1_data_tailed.loc[:,"id"] = "SRM"
    df_exch_2_data_tailed.loc[:,"id"] = "UNI"

    df_exch_data_tailed = df_exch_1_data_tailed.append(df_exch_2_data_tailed)
    print(df_exch_data_tailed)

    return html.Div([
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} 
                for i in df_exch_data_tailed.columns],
            data=df_exch_data_tailed.to_dict('records'),
            style_cell=dict(textAlign='left'),
            style_header=dict(backgroundColor="black"),
            style_data=dict(backgroundColor="gray")
        )
    ])

##== FEE GRAPH =========================================================================================================

@app.callback(Output('fee-graph-live', 'figure'),
        [Input('fee-graph-update', 'n_intervals')])
def build_fee_graph(n):
    df_token_1 = "SOL"
    df_token_2 = "ETH"

    df_token_1_data = token_metrics_service.get_df_by_token(SOLANA_TOKEN_CODE)
    df_token_2_data = token_metrics_service.get_df_by_token(ETHERIUM_TOKEN_CODE)

    # Create graph plots
    token_1_fee_plot = go.Scatter(
        x=df_token_1_data['datetime'],
        y=df_token_1_data['avg_tx_price'],
        mode='lines+markers',
        name='SOL Fees'
    )
    token_2_fee_plot = go.Scatter(
        x=df_token_2_data['datetime'],
        y=df_token_2_data['avg_tx_price'],
        mode='lines+markers',
        name='ETH Fees'
    )
    fee_graph_df = [token_1_fee_plot, token_2_fee_plot]

    fee_graph_title = 'Fee Comparison of ' + df_token_1 + ' and ' + df_token_2 + " in USD"

    return {
        "data": fee_graph_df,
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

##== LATENCY GRAPH =========================================================================================================

@app.callback(Output('time-graph-live', 'figure'),
        [Input('time-graph-update', 'n_intervals')])
def build_time_graph(n):
    df_token_1 = "SOL"
    df_token_2 = "ETH"

    df_token_1_data = token_metrics_service.get_df_by_token(SOLANA_TOKEN_CODE)
    df_token_2_data = token_metrics_service.get_df_by_token(ETHERIUM_TOKEN_CODE)

    # Create graph plots
    token_1_time_plot = go.Scatter(
        x=df_token_1_data['datetime'],
        y=df_token_1_data['avg_tx_time'],
        mode='lines+markers',
        name='SOL Latency'
    )
    token_2_time_plot = go.Scatter(
        x=df_token_2_data['datetime'],
        y=df_token_2_data['avg_tx_time'],
        mode='lines+markers',
        name='ETH Latency'
    )
    time_graph_df = [token_1_time_plot, token_2_time_plot]

    time_graph_title = 'Latency Comparison of ' + df_token_1 + ' and ' + df_token_2 + " in Seconds"

    return {
        "data": time_graph_df,
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
            "title": time_graph_title,
        },
    }

##== MAIN PAGE =========================================================================================================

def serve_layout():
    df_token_1 = "SOL"
    df_token_2 = "ETH"

    # Mock-up blockchain selector
    all_tokens = ["Solana", "Ethereum", "Cardano", "Binance Smart Chain"]

    fee_graph_title = 'Fee Comparison of ' + df_token_1 + ' and ' + df_token_2 + " in USD"
    time_graph_title = 'Latency Comparison of ' + df_token_1 + ' and ' + df_token_2 + " in Seconds"

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
                                id="select-blockchain", #top-section-container
                                #className="twelve columns",
                                children=[
                                    generate_section_banner("Select Blockchain to Compare"),
                                    html.P("By selecting your blockchains to compare, you will see comparison data such as transaction fees, transaction delays, user experience ratings and a list of DeFi application stats. (More features coming soon)"),
                                    html.Div([
                                        dcc.Checklist(
                                            id="blockchain-checklist",
                                            options=[
                                                {"label": "Solana", "value": "SOL", "disabled": False},
                                                {"label": "Ethereum", "value": "ETH", "disabled": False},
                                                {"label": "Cardano", "value": "ADA", "disabled": True},
                                                {"label": "Binance Smart Chain", "value": "BSC", "disabled": True}
                                            ],
                                            value=all_tokens[:2],
                                            labelStyle={'display': 'inline-block'}
                                        ),
                                    ]),
                                ]
                            ),
                            html.Div(
                                id="tabs", 
                                className="tabs",
                                children=[
                                    dcc.Tabs(
                                        id="app-tabs",
                                        className="custom-tabs",
                                        children=[
                                            dcc.Tab(
                                                label='Blockchain Fees', 
                                                className="custom-tab", 
                                                selected_className="custom-tab--selected", 
                                                children=[
                                                    html.Div(
                                                        id="fee-graph-container",
                                                        #className="twelve columns",
                                                        children=[
                                                            generate_section_banner(fee_graph_title),
                                                            dcc.Graph(
                                                                id="fee-graph-live",
                                                                animate=True
                                                            ),
                                                            dcc.Interval(
                                                                id='fee-graph-update',
                                                                interval=1000*DASHBOARD_REFRESH_SECONDS,
                                                                n_intervals=0
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),    
                                            dcc.Tab(
                                                label='Blockchain Latency',
                                                className="custom-tab", 
                                                selected_className="custom-tab--selected", 
                                                children=[
                                                    html.Div(
                                                        id="time-graph-container",
                                                        #className="twelve columns",
                                                        children=[
                                                            generate_section_banner(time_graph_title),
                                                            dcc.Graph(
                                                                id="time-graph-live",
                                                                animate=True
                                                            ),
                                                            dcc.Interval(
                                                                id='time-graph-update',
                                                                interval=1000*DASHBOARD_REFRESH_SECONDS,
                                                                n_intervals=0
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    generate_section_banner("DeFi Application Comparison Table"),
                    build_dapp_table(),
                ],
            ),
        ],
    )
            


app.layout = serve_layout


# Running the server
if __name__ == "__main__":
    app.run_server(debug=False, port=8050)





