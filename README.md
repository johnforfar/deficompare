# Welcome to DeFi Compare

Open and fair DeFi Comparison Tool across all Blockchains and Decentralised Finance applications.

## Questions to ask
* **What is the use-case of our MVP?**
  - Comparing transaction costs (easy)    -v
  - Comparing transaction speeds (easy) -> Those two metrics make Solana look really good.
  - Comparing swap costs? (medium - needs to be further defined: Which DEXes? Which coins/tokens?)
  - Finding cheapest route to DEX-swap any coin/token in inter-chain environment? (very hard)
* **Which data is easily available?**
  - Which coins/chains do exist: https://coinmarketcap.com/coins/
  - Blockchain data (avg. txn speed & fees):
    * https://blockchair.com/api/plans (17 different Blockchains)
    * https://tokenview.com/en/ (+100 different Blockchains)
  - Exchange rates (to convert fees into $ or €):
    * https://pro.coinmarketcap.com/ (widely used)
    * https://binance-docs.github.io/apidocs/spot/en/#websocket-market-streams (First exchange to list SOL, for free)
  - DEX data:
    * https://docs.bonfida.com/#project-serum
  - Good list of DeFi Dapps:
    * https://en.cryptonomist.ch/Defi/
    * https://apy.plasma.finance/liquidity-pools (This has Pool fees over 7 days)
    * https://zapper.fi/dashboard (Another list)
    * https://defi.instadapp.io/ (Another list)
    
## Built With
* [Python](https://www.python.org) - Python
* [Dash](https://dash.plot.ly/) - Main server and interactive components 
* [Plotly Python](https://plot.ly/python/) - Used to create the interactive plots
* [Dash DAQ](https://dash.plot.ly/dash-daq) - Styled technical components for industrial applications
* [Heroku](https://www.heroku.com) - Heroku free hosting

