# Welcome to Defi/Chain Compare
We want to create a platform where the user can look for the cheapest and/or fastest way to transfer cash and/or swap coins/tokens in a decentralized fashion.
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
    
# Methods
## Web Scraping
Web scraping is a very powerful tool to learn for any data professional. With web scraping the entire internet becomes your database. In this repository how to parse a web page into a data file (csv) using a Python package called BeautifulSoup Two ways to extract data from a website:

### Use the API of the website (Best way) The data on the websites are unstructured,
Sadly, not all websites provide an API

### Web Scraping: Web scraping is an automated method used to extract useful information from the websites focuses on the transformation of unstructured data (HTML format) on the web into structured data.
**STEPS**: To extract data using web scraping with python,you need to follow these basic steps:
* Find the URL that you want to scrape
* Check wheather is it legal to scrap from that website Goto www.URL/robots.txt if you are using Scrapy you no need to worry because it automatically allow only Legal links. in Settings.py ROBOTSTXT_OBEY=False
* Inspecting the Website
* Find the data you want to extract
* Write the code
* Run the code and extract the data
* Store the data in the required format

### Need of Web Scraping
* **Price Comparison**: Services such as ParseHub use web scraping to collect data from online shopping websites and use it to compare the prices of products.
* **Email address gathering**: Many companies that use email as a medium for marketing, use web scraping to collect email ID and then send bulk emails.
* **travel recommendation**: Scraping a few travel recommendation sites, pull out comments about various do to things and see which property is getting a lot of positive responses from the users! The list of use cases is endless.
* **Social Media Scraping**: Web scraping is used to collect data from Social Media websites such as Twitter to find out what’s trending.
* **Research and Development**: Web scraping is used to collect a large set of data (Statistics, General Information, Temperature, etc.) from websites, which are analyzed and used to carry out Surveys or for R&D.
* **Job listings**: Details regarding job openings, interviews are collected from different websites and then listed in one place so that it is easily accessible to the user.

### Is Web Scraping legal?
To know whether a website allows web scraping or not, you can look at the website’s “robots.txt” file. You can find this file by appending “/robots.txt” to the URL that you want to scrape.

## Built With
* [Dash](https://dash.plot.ly/) - Main server and interactive components 
* [Plotly Python](https://plot.ly/python/) - Used to create the interactive plots
* [Dash DAQ](https://dash.plot.ly/dash-daq) - Styled technical components for industrial applications

## Requirements
We suggest you to create a separate virtual environment running Python 3 for this app, and install all of the required dependencies there. Run in Terminal/Command Prompt:

```
git clone https://github.com/plotly/dash-sample-apps.git
cd dash-sample-apps/apps/dash-manufacture-spc-dashboard/
python3 -m virtualenv venv
```
In UNIX system: 

```
source venv/bin/activate
```
In Windows: 

```
venv\Scripts\activate
```

To install all of the required packages to this environment, simply run:

```
pip install -r requirements.txt
```

and all of the required `pip` packages, will be installed, and the app will be able to run.


## How to use this app

Run this app locally by:
```
python app.py
```
Open http://0.0.0.0:8050/ in your browser, you will see a live-updating dashboard.

Click on **Learn more** button to learn more about how this app works.

## What does this app show

Click on buttons in `Parameter` column to visualize details of trendline on the bottom panel.

Click `Start` button, trends are updated every two seconds to simulate real-time measurements. The Sparkline on top panel and Control chart on bottom panel show Shewhart process control using mock data. Data falling outside of control limit are signals indicating 'Out of Control(OOC)', and will 
trigger alerts instantly for a detailed checkup. 

Operators may stop measurement by clicking `Stop` button, and edit specification parameters for selected process line(metrics) in Specification Tab.

## Resources and references
* [Shewhart statistical process control](https://en.wikipedia.org/wiki/Shewhart_individuals_control_chart)
* [Dash User Guide](https://dash.plot.ly/)
