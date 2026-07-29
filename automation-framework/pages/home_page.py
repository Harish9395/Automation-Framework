from pages.base_page import BasePage

class HomePage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def get_page_source(self):
        return self.driver.page_source
