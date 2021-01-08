# Web scraping project - extracting data from the top 100 biggest cryptocurrencies

* In this project, I have scraped the 100 biggest cryptocurrencies based on their market cap from [coinmarketcap.com](https://coinmarketcap.com/). 
* The web-crawling framework Scrapy was used. In addition, the portable framework Selenium was used since the web pages were dynamic.
* Information such as the daily volume, market cap, highest/lowest value for each cryptocurrency have been extracted. 
* This spider has fetched each cryptocurrency's data from its first day were documented on the cryptocurrency market (according to [coinmarketcap.com](https://coinmarketcap.com/)) to the 2nd of December. 
* In total, more than 800 000 data points have been extracted.

I used google chrome as web browser and the selenium_scrapy module in this project. Thus, the following were inserted in the settings.py file (which is generated when the spider is constructed):

```
from shutil import which 
  
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver') 
SELENIUM_DRIVER_ARGUMENTS=['--headless'] 

DOWNLOADER_MIDDLEWARES = { 
     'scrapy_selenium.SeleniumMiddleware': 800
     } 
```
The web pages are scraped by using the script [cryptoscraper](https://github.com/OlleKahreZall/Portfolio/blob/main/cryptoscraper.py) (see the file for more details). All the data collected from the web pages were stored in the csv file'cryptocurrencies_top-100.csv'.

Furthermore, preprocessing of the data is done in the ipynb file data-cleaning_visualization.ipynb. In addition, this script is also used to visualize the historical data of the three largest cryptocurrencies with respect to their market cap (December 2020). The figures below show the value (when the market closes), volume and the market cap for each cryptocurrency.

![](https://github.com/OlleKahreZall/Portfolio/blob/gh-pages/Images/close.png)
![](https://github.com/OlleKahreZall/Portfolio/blob/gh-pages/Images/volume.png)
![](https://github.com/OlleKahreZall/Portfolio/blob/gh-pages/Images/market_cap.png)


## Upcoming project

As of January 2021, the price of bitcoin has drastically increased since December 2020: from approximately 19,000$ to 38,000$. The next step in this project is to use different predictive models, such as time series forecasting and recurrent neural networks, to evaluate their predictions for different cryptocurrencies, but especially for bitcoin. 

More information will be provided soon!
