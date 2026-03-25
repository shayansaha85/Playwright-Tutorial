from playwright.sync_api import Page

class DuckDuckGoSearchPage:
      URL = 'https://start.duckduckgo.com'
      def __init__(self, page: Page) -> None:
            self.page = page
            self.search_button = page.locator('xpath=/html/body/div/div/main/div/div[2]/div[1]/div/div[2]/form/div/div[1]/div/div/button[2]')
            self.search_input = page.locator('xpath=/html/body/div/div/main/div/div[2]/div[1]/div/div[2]/form/div/div[1]/div/input')
      
      def load(self) -> None:
            self.page.goto(self.URL)
      
      def search(self, phrase: str) -> None:
            self.search_input.fill(phrase)
            self.search_button.click()