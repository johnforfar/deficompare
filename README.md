# Welcome to DeFi Compare

The trusted DeFi comparison tool for the next one billion users.

**WEBSITE:**
[DeFi.Compare](https://defi.compare) - The Official Defi Compare Website !!!

**PROBLEM:** Existing DeFi comparison sites are too complex, technical and not suitable for those new to DeFi. There is a missing gap between CeFi & DeFi onboarding & education. 

**SOLUTION:** Build a simple comparison tool for the upcoming DeFi masses that fairly represents all DeFi blockchains and their respective applications. Metrics that will be represented are transaction costs, transactions speeds, DEX swap costs, decentralised user reviews, more to come. (see Roadmap)

## Built With
* [Python](#) - Python
* [React](#) - React front end
* [Hasura & Timescale](#) - Database - Hasura & Timescale

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
* [Johnny (SOLX)](https://github.com/solx-ventures/) - Huge Solana fan, NFT & gamer
* [MHHukiewitz](https://github.com/MHHukiewitz) - Developer, scientist
* [Crushing Codes](https://github.com/crushingcodes) - Mad coding wizard

## Roadmap

* Binance Smart Chain (BSC) support
* More listed DEXes from Ethereum, Solana and BSC
* Migrating data retrieval into public subgraph
* Comparison of lending protocols, other DeFi protocol categories
