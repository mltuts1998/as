import scrapy 
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    name = "spyder"

    def start_requests(self):
        urls = [
            'https://gramuser.com/search/jhabar+singh+bhati'
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.css("td div::text")
        mi = {}
        del page[0]
        del page[0]
        arr = []
        for i in range(0, len(page), 3):
            arr.append(str(page[i])[80:-2])
        print(arr)


process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()