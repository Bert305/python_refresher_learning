import scrapy
# cd into the project directory
class HialeahJobsSpider(scrapy.Spider):
    name = "hialeah_jobs" # name for the spider in the terminal
    allowed_domains = ["hialeahfl.gov"]
    start_urls = ["https://www.hialeahfl.gov/Jobs.aspx"]

    def parse(self, response):
        # Loop through all job links
        for job in response.css("a[id^='jobTitle_']"):
            title = job.css("::text").get().strip()
            link = response.urljoin(job.attrib["href"])

            # Send request to job detail page
            yield scrapy.Request(
                url=link,
                callback=self.parse_detail,
                meta={"title": title, "application_link": link}
            )

    def parse_detail(self, response):
        title = response.meta["title"]
        application_link = response.meta["application_link"]

        # You may need to update these selectors depending on the page structure
        description = response.css("div#JobDetails *::text").getall()
        description = " ".join([d.strip() for d in description if d.strip()])

        # Default static location if not listed
        location = "Hialeah, FL"

        yield {
            "title": title,
            "description": description,
            "location": location,
            "application_link": application_link
        }


# scrapy crawl hialeah_jobs -o jobs2.csv
