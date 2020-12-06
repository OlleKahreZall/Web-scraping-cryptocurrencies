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
    name = 'fpscraper'
    def start_requests(self):
        for cryptocurrency in cryptocurrencies:
            yield SeleniumRequest(
                url = f'https://coinmarketcap.com/currencies/{cryptocurrency}/historical-data/?start=20130429&end=20201202',
                #wait_time=3,
                screenshot = True,
                callback=self.parse,
                dont_filter=True
        )
            
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

            for i in range(len(data_points)):
                if 7*i >= len(data_points):
                    break
                else:
                    date.append(data_points[7*i])


                if 7*i+1 >= len(data_points):
                    break
                else:
                    open.append(data_points[7*i+1])

                    
                if 7*i+2 >= len(data_points):
                    break
                else:
                    high.append(data_points[7*i+2])

                    
                if 7*i+3 >= len(data_points):
                    break
                else:
                    low.append(data_points[7*i+3])

                    
                if 7*i+4 >= len(data_points):
                    break
                else:
                    close.append(data_points[7*i+4])

                    
                if 7*i+5 >= len(data_points):
                    break
                else:
                    volume.append(data_points[7*i+5].replace('\u00a0',''))


                if 7*i+6 >= len(data_points):
                    break
                else:
                    market_cap.append(data_points[7*i+6].replace('\u00a0',''))

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