import scrapy

class SherlockSpider(scrapy.Spider):
    name = "sherlock"
    allowed_domains = ["sherlocktalent.com"]
    start_urls = ["https://www.sherlocktalent.com/job-opportunities/"]

    def parse(self, response):
        rows = response.xpath("//tbody/tr[not(contains(@class, 'header'))]")

        for row in rows:
            title = row.xpath(".//a[@class='job-title']/text()").get()
            link = row.xpath(".//a[@class='job-title']/@href").get()
            salary = row.xpath(".//td[contains(@class, 'joblist-salary')]/text()").get()
            location = row.xpath(".//td[contains(@class, 'joblist-location')]/text()").get()

            yield {
                "title": title.strip() if title else "",
                "link": response.urljoin(link) if link else "",
                "salary": salary.strip() if salary else "",
                "location": location.strip() if location else ""
            }







