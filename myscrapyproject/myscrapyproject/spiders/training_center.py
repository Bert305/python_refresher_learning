import scrapy

class TrainingCentersSpider(scrapy.Spider):
    name = "training_centers"

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.electricaltrainingalliance.org/locateaTrainingCenter/Inside",
            callback=self.parse
        )

    def parse(self, response):
        rows = response.xpath('//table[@id="tcGrid"]/tbody/tr')

        for row in rows:
            training_center = row.xpath('./td[1]//text()').get(default='').strip()
            contact_info = [text.strip() for text in row.xpath('./td[2]//text()').getall() if text.strip()]
            website = row.xpath('./td[2]//a/@href').get(default='').strip()
            training_director = [text.strip() for text in row.xpath('./td[3]//text()').getall() if text.strip()]

            yield {
                "Training Center": training_center,
                "Contact Info": contact_info,
                "Website": website,
                "Training Director": training_director
            }




