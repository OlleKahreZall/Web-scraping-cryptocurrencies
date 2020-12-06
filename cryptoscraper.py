import scrapy
from scrapy_selenium import SeleniumRequest
import pandas as pd

#### 10 first cryptocurrencies
#//tbody//td[@style='text-align:left']/a[@class='cmc-link']/@href

#### the rest (90 of them)
#//tbody//td[@style='text-align: left;']/a[@class='cmc-link']/@href

df =  pd.read_excel('cryptocurrency_top-100.xlsx')
cryptocurrencies_unfiltered = df['cryptocurrency'].tolist()
global cryptocurrencies
cryptocurrencies = []
for i in cryptocurrencies_unfiltered:
    cryptocurrencies.append(i.split('/')[2])


class FpscraperSpider(scrapy.Spider):
    name = 'cryptoscraper'
    #Request the url
    def start_requests(self):
        for cryptocurrency in cryptocurrencies:
            yield SeleniumRequest(
                url = f'https://coinmarketcap.com/currencies/{cryptocurrency}/historical-data/?start=20130429&end=20201202',
                #wait_time=3, # Set amount of time to wait between requests.
                callback=self.parse,
                dont_filter=True # The request should be filtered by the scheduler.
        )
    # Scrape the web page        
    def parse(self, response):
            data_points = []
            date = []
            open = []
            high = []
            low = []
            close = []
            volume = []
            market_cap = []

            for data_point in response.xpath("//div[@class='sc-1yv6u5n-0 gCAyTd cmc-table']//td"):
                data_points.append(data_point.xpath(".//div/text()").get()) 

            # Each cryptocurrency has a table with the same structure. In each if statement, 
            # each column is fetched from the web page.

            for i in range(len(data_points)):

                # Fetch the date.
                if 7*i >= len(data_points):
                    break
                else:
                    date.append(data_points[7*i])

                # Fetch the open values.
                if 7*i+1 >= len(data_points):
                    break
                else:
                    open.append(data_points[7*i+1])

                # Fetch the highest values.    
                if 7*i+2 >= len(data_points):
                    break
                else:
                    high.append(data_points[7*i+2])

                # Fetch the lowest values.    
                if 7*i+3 >= len(data_points):
                    break
                else:
                    low.append(data_points[7*i+3])

                # Fetch the closed values.    
                if 7*i+4 >= len(data_points):
                    break
                else:
                    close.append(data_points[7*i+4])

                # Fetch the volumes.    
                if 7*i+5 >= len(data_points):
                    break
                else:
                    volume.append(data_points[7*i+5].replace('\u00a0',''))

                # Fetch the market cap.
                if 7*i+6 >= len(data_points):
                    break
                else:
                    market_cap.append(data_points[7*i+6].replace('\u00a0',''))

                # With this yield statement, a csv file can be produced directly.
                yield {
                    'date' : date[i],
                    'open' : open[i],
                    'high' : high[i],
                    'low' : low[i],
                    'close' : close[i],
                    'volume' : volume[i],
                    'market_cap' : market_cap[i],
                    'cryptocurrency': response.request.url.split('/')[4]
                    }