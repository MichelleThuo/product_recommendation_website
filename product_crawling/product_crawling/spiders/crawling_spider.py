from scrapy.spiders import CrawlerSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
  #Name of the crawler
  name = "mycrawler"
  #List of domains to be accepted for crawling and scraping
  allowed_domains = ["kilimall.co.ke"]
  #Defines the first website to be crawled ie acts as a starting point
  start_urls = ["https://www.kilimall.co.ke/"]
  
  #Web crawling
  #Defines rules for additional links
  rules = (
    Rule(LinkExtractor(allow="new/commoditysearch")),
    Rule(LinkExtractor(allow="new", deny="commoditysearch")), callback="parse_item")
  )
  
  #Web scrapping
  #parse_item method handles all instances by second rule
  def parse_item(self, response):
    yield{
      "product_description": response.css("").get(),
      "price": response.css("").get(),
      "image": response.css("").get(),
      "rating": response.css("").get(),
      "availability": response.css("").get(),
    }
  
  
