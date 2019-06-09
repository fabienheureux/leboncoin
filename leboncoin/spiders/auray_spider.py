
import scrapy


class AuraySpider(scrapy.Spider):
    name = "auray"

    def start_requests(self):
        urls = [
						'https://www.leboncoin.fr/recherche/?category=9&text=maison&locations=Auray_56400,Le%20Bono_56400,Brech_56400,Plouharnel_56340,Ploemel_56400,Carnac_56340&real_estate_type=1&price=min-350000'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        for ad in response.css('li[data-qa-id="aditem_container"]'):
            yield {
                'title': ad.css('span[data-qa-id="aditem_title"]::text').get(),
                'price': int(ad.css('div[data-qa-id="aditem_price"] span span[itemprop="priceCurrency"]::text').get().replace(" ", ""))
            }

