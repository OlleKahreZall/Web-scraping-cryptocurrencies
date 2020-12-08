## [Web scraping project - extracting data from the 100 biggest cryptocurrencies](https://github.com/OlleKahreZall/Web-scraping-cryptocurrencies)

* In this project, I have scraped the 100 biggest cryptocurrencies based on their market cap from coinmarketcap.com. 
* The web-crawling framework Scrapy was used. In additon, the portable framework Selenium was used since the web pages were dynamic.
* Information such as the daily volume, market cap, values when the stock market opened/closed, etc., for each cryptocurrency have been extracted. 
* This spider has fetched each cryptocurrency's data from its first day were documented on the stock market (according to coinmarketcap.com) to the 2nd of December. 
* In total, more than 800 000 data points have been extracted.

I used google crhome as web browser and the selenium_scrapy module in this project. Thus, the following were inserted in the settings.py file (which is generated when the spider is constructed):

``
`code`
from shutil import which 
  
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver') 
SELENIUM_DRIVER_ARGUMENTS=['--headless'] 

DOWNLOADER_MIDDLEWARES = { 
     'scrapy_selenium.SeleniumMiddleware': 800
     } 
``
sds
