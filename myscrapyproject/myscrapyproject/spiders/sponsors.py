import scrapy

class SponsorsSpider(scrapy.Spider):
    name = "sponsors2"
    start_urls = ["https://www.dol.gov/agencies/eta/apprenticeship/community-colleges/sponsors"]

    def parse(self, response):
        rows = response.xpath('//table//tr')
        for row in rows[1:]:
            cols = row.xpath('.//td')
            if len(cols) >= 8:
                state = cols[0].xpath('normalize-space()').get()
                institution = cols[1].xpath('normalize-space()').get()
                first_name = cols[2].xpath('normalize-space()').get()
                last_name = cols[3].xpath('normalize-space()').get()
                city = cols[4].xpath('normalize-space()').get()
                phone = cols[5].xpath('normalize-space()').get()
                email = cols[6].xpath('.//a/text()').get(default='').strip()
                website = cols[7].xpath('.//a/@href').get(default='').strip()

                yield {
                    "State": state,
                    "Institution": institution,
                    "First Name": first_name,
                    "Last Name": last_name,
                    "City": city,
                    "Phone #": phone,
                    "Email": email,
                    "Website": website
                }


