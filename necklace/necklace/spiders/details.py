import scrapy

class DetailSpider(scrapy.Spider):
    name = 'details'

    start_urls = [
        'https://www.houseofindya.com/zyra/necklace/cat'
    ]

    def parse(self, response):
        for detail in response.xpath("//ul[@id='JsonProductList']/li"):
            yield {
                'description' : detail.xpath(".//div[@class='catgName']/p/text()").extract_first(),
                'image urls' : detail.xpath(".//div[@class='catgItem']/img/@data-original").extract_first(),
                'price' : detail.xpath(".//div[@class='catgName']/span/text()").extract_first()
            }

# Command to generate output
# In CSV - scrapy crawl details -o data.csv
# In Json - scrapy crawl details -o data.json
