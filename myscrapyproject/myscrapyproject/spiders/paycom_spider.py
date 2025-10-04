import scrapy


class PaycomSpider(scrapy.Spider):
    name = "paycom"
    allowed_domains = ["paycomonline.net"]
    start_urls = [
        "https://www.paycomonline.net/v4/ats/web.php/jobs?jobSearchSettingsId=22561&clientkey=32845297BC28AB21BFFD7C682F3E1551#"
    ]

    def parse(self, response):
        job_cards = response.xpath("//a[contains(@class, 'JobListing__container')]")
        
        for card in job_cards:
            title = card.xpath(".//span[contains(@class, 'jobTitle')]/text()").get()
            link = card.xpath("./@href").get()
            location = card.xpath("./following-sibling::span[contains(@class, 'jobLocation')]/text()").get()
            description = card.xpath("./following-sibling::span[contains(@class, 'jobDescription')]/text()").get()

            yield {
                "title": title.strip() if title else "",
                "link": response.urljoin(link),
                "location": location.strip() if location else "",
                "description": description.strip() if description else "",
            }
