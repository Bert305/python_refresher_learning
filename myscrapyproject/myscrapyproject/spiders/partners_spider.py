import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.http import HtmlResponse
import time


class PartnersSpider(scrapy.Spider):
    name = "partners"
    start_urls = ["https://apprenticeshipsfortech.org/partners"]

    def __init__(self, *args, **kwargs):
        super(PartnersSpider, self).__init__(*args, **kwargs)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def closed(self, reason):
        self.driver.quit()

    def start_requests(self):
        for url in self.start_urls:
            self.driver.get(url)
            time.sleep(5)  # wait for JS to render
            body = self.driver.page_source
            response = HtmlResponse(
                url=self.driver.current_url,
                body=body,
                encoding='utf-8'
            )
            yield from self.parse(response)

    def parse(self, response):
        for partner in response.css("div.view-content > div"):
            name = partner.css("h2::text").get(default="").strip()
            description = partner.css("p::text").get(default="").strip()
            website = partner.css("a.ext::attr(href)").get(default="").strip()

            occupation = partner.css("div.field__item::text").getall()
            occupation = "; ".join([occ.strip() for occ in occupation if occ.strip()])

            state = partner.xpath(".//div[contains(text(), 'State:')]/following-sibling::div[1]/text()").get(default="").strip()
            city = partner.xpath(".//div[contains(text(), 'City or Region:')]/following-sibling::div[1]/text()").get(default="").strip()
            category = partner.xpath(".//div[contains(text(), 'Partner Category:')]/following-sibling::div[1]/text()").get(default="").strip()

            yield {
                "Company Name": name,
                "Description": description,
                "Website Link": website,
                "Occupation": occupation,
                "State": state,
                "City or Region": city,
                "Partner Category": category
            }



