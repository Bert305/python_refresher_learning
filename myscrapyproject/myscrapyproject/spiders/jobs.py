import scrapy
# cd into the project directory
class JobsSpider(scrapy.Spider):
    name = "jobs" # name for the spider in the terminal
    allowed_domains = ["dashboard.workforce.miami"]
    start_urls = [
        "https://dashboard.workforce.miami/companies"
    ]

    def parse(self, response):
        # Extract all company names inside the specific <h3> tag
        company_names = response.css('h3.font-semibold::text').getall()

        for name in company_names:
            yield {"company_name": name.strip()}
            
            
            
            # scrapy crawl jobs -o jobs5.csv
