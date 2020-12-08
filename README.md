# Web scraping project - extracting data from the top 100 biggest cryptocurrencies

* In this project, I have scraped the 100 biggest cryptocurrencies based on their market cap from [coinmarketcap.com](https://coinmarketcap.com/). 
* The web-crawling framework Scrapy was used. In addition, the portable framework Selenium was used since the web pages were dynamic.
* Information such as the daily volume, market cap, highest/lowest value for each cryptocurrency have been extracted. 
* This spider has fetched each cryptocurrency's data from its first day were documented on the cryptocurrency market (according to [coinmarketcap.com](https://coinmarketcap.com/)) to the 2nd of December. 
* In total, more than 800 000 data points have been extracted.

I used google crhome as web browser and the selenium_scrapy module in this project. Thus, the following were inserted in the settings.py file (which is generated when the spider is constructed):

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

Furthermore, the ipynb file [data-cleaning_visualization.ipynb](https://github.com/OlleKahreZall/Portfolio/blob/main/data-cleaning_visualization.ipynb) was used to pre-process the data. It was also used to visualize the currently top 3 rated cryptocurrencies and their historical data. The figures below are generated by this script, which show the value (when the market closes), volume and the market cap for the respective cryptocurrency. 

![](https://github.com/OlleKahreZall/Portfolio/blob/main/Images/close.png)
![](https://github.com/OlleKahreZall/Portfolio/blob/main/Images/volume.png)
![](https://github.com/OlleKahreZall/Portfolio/blob/main/Images/market_cap.png)


## Upcoming project

Next step is to analyze the data more deeply. Is there an overall correlation between the cryptocurrencies? Or are there any outliers that are not affected by the fluctuations on the market? And is it possible to make predictions out of this data?

To answer these questions, using different machine learning techniques would be necessary to use. Since a lot of data is considered here, a first step would be to narrow down the project and start with studying only a few cryptocurrencies. In this case, using supervised machine learning techniques such as multiple linear regression, regression trees or multivariate regression can be used to investigate if there exist patterns between the cryptocurrencies. If it that is the case, a more in-depth analysis would be necessary for all the data. If that is not the case, unsupervised machine learning techniques, such as different clustering methods (for example k-means or DBSCAN), would be an option.
