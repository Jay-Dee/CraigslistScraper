import scrapy
from ..items import CraigslistcrawlerItem


class ComputersSpider(scrapy.Spider):
    name = 'computers'
    allowed_domains = ['https://london.craigslist.org/d/computers/search/sya']
    start_urls = ['https://london.craigslist.org/d/computers/search/sya']

    def parse(self, response):
        allAds = response.css("li.result-row")

        for ad in allAds:
            date = ad.css("time.result-date::attr(title)").get()
            title = ad.css("a.result-title.hdrlnk::text").get()
            price = ad.css("span.result-price::text").get()
            link = ad.css("a::attr(href)").get()

            print("====NEW COMPUTER===")
            print(date)
            print(title)
            print(price)
            print(link)

            print("\n")

            items = CraigslistcrawlerItem()
            items['date'] = date
            items['title'] = title
            items['price'] = price
            items['link'] = link

            yield items
