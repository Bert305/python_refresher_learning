import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://facultyaffairs.miami.edu/resources/school-college-contacts/department-chairs/index.html']

    def parse(self, response):
        self.log(response.css('title::text').get())
        
        # activate the shell to test the spider --> scrapy shell https://example.com
        # fetch command --> fetch('https://example.com')
        # view command --> view(response)
        # double check 200 response code --> response.status or response
        # find class --> response.css('.class_name')
        # find id --> response.css('#id_name')
        # save into variable --> variable = response.css('.class_name')
        # find count --> len(variable)
        # find 1st element --> response.css('.class_name::text').get()
        # find all classes --> response.css('.class_name::text').getall()
        # find all ids --> response.css('#id_name::text').getall()
        # run file --> scrapy crawl example
        # export json --> scrapy crawl example -o output.json
        # export csv --> scrapy crawl example -o output.csv
        # export xml --> scrapy crawl example -o output.xml

