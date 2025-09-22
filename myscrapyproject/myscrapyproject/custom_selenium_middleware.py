from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class CustomSeleniumMiddleware:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

    def process_request(self, request, spider):
        self.driver.get(request.url)

        # WAIT for table to load (10 seconds max)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#tcGridBody tr"))
            )
        except:
            spider.logger.warning("Table rows never appeared.")

        return HtmlResponse(
            url=self.driver.current_url,
            body=self.driver.page_source,
            encoding='utf-8',
            request=request
        )

    def __del__(self):
        self.driver.quit()



