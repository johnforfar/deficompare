# Welcome to DeFi Compare

An open and fair DeFi Comparison tool across all Blockchains and Decentralised Finance applications.

**PROBLEM:** Some of the fastest Blockchain DeFi applications are not represented at other DeFi Comparison sites.  

**SOLUTION:** Build a simple comparison tool for the upcoming DeFi masses that fairly represents all DeFi blockchains and their respective applications. Metrics that will be represented are transaction costs, transactions speeds, DEX swap costs, decentralised user reviews, more to come. (see Roadmap)

## Built With
* [Python](https://www.python.org) - Python
* [Dash](https://dash.plot.ly/) - Main server and interactive components 
* [Plotly Python](https://plot.ly/python/) - Used to create the interactive plots
* [Dash DAQ](https://dash.plot.ly/dash-daq) - Styled technical components for industrial applications
* [Heroku](https://www.heroku.com) - Heroku free hosting

## Data Sources
To ensure highest standards of trustlessness, we aim to use as much subgraphs by https://thegraph.com/ as possible. Further ahead the roadmap lies the implementation of a subgraph of our own, for comparing useful key metrics of DEXes and other DeFi protocols across chains.
  - Coin/Token prices:
    * By CoinGecko: https://www.coingecko.com/en/api
  - Ethereum gas prices and block times:
    * https://docs.ethgasstation.info/gas-price
  - Solana lamports consumption and block times:
    * https://app.swaggerhub.com/apis-docs/V2261/solanabeach-backend_api/0.0.1
  - DEX data:
    * Serum: https://docs.bonfida.com/#project-serum
    * Uniswap: https://thegraph.com/explorer/subgraph/uniswap/uniswap-v2

## Initial Contributors
* [Johnny (SOLX)](https://solana.blog) - SOL X - Run a blog about the Solana ecosystem and excited to bring decentralised applications to the masses!
* [Dipfit](https://twitter.com/dipfit1) - Developer, scientist, scholar, dancer, yogi
* [Crushing Codes](https://github.com/crushingcodes) - Mad coding wizard

## Roadmap

* Binance Smart Chain (BSC) support
* More listed DEXes from Ethereum, Solana and BSC
* Migrating data retrieval into public subgraph
* Comparison of lending protocols, other DeFi protocol categories
