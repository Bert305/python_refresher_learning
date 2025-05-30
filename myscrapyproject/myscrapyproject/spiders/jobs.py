import scrapy

class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["dashboard.workforce.miami"]
    start_urls = [
        "https://dashboard.workforce.miami/companies"
    ]

    def parse(self, response):
        # Extract all company names inside the specific <h3> tag
        company_names = response.css('h3.font-semibold::text').getall()

        for name in company_names:
            yield {"company_name": name.strip()}
