from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from config import settings
from pages.base_page import BasePage


class TwitchHomePage(BasePage):
    SEARCH_ICON = (By.CSS_SELECTOR, 'a[href="/directory"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[data-a-target="tw-input"]')
    # After typing, Twitch narrows the directory grid down to a single
    # matching category suggestion with this href pattern.
    CATEGORY_SUGGESTION = (By.CSS_SELECTOR, 'a[href^="/directory/category/"]')

    def load(self):
        self.open(settings.BASE_URL)

    def open_search(self):
        self.click(self.SEARCH_ICON)
        try:
            self.wait_for_url_contains("/directory")
        except TimeoutException:
            self.click(self.SEARCH_ICON)
            self.wait_for_url_contains("/directory")

    def search_for(self, term: str = settings.SEARCH_TERM):
        self.type_text(self.SEARCH_INPUT, term)
        self.click(self.CATEGORY_SUGGESTION)
