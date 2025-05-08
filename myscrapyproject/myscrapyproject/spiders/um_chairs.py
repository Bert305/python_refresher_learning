
import scrapy

class UmChairsSpider(scrapy.Spider):
    name = "um_chairs"
    allowed_domains = ["facultyaffairs.miami.edu"]
    start_urls = [
        "https://facultyaffairs.miami.edu/resources/school-college-contacts/department-chairs/index.html"
    ]

    def parse(self, response):
        # Each row is 3 <td> tags in a row: dept, name, email
        rows = response.xpath('//table//tr')
        for row in rows:
            cells = row.xpath('./td')
            if len(cells) == 3:
                yield {
                    'department': cells[0].xpath('normalize-space(string())').get(),
                    'chair_name': cells[1].xpath('.//a/text()').get(),
                    'chair_email': cells[2].xpath('.//a/text()').get()
                }
                
                
     # export csv file in terminal --> scrapy crawl um_chairs -o um_chairs.csv
     # export json file in terminal --> scrapy crawl um_chairs -o um_chairs.json           
