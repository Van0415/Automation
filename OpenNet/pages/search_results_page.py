from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    STREAMER_CARDS = (By.TAG_NAME, "article")

    def scroll_down(self, times: int = 2, pixels: int = 900):
        super().scroll_down(times=times, pixels=pixels)

    def get_streamer_links(self):
        cards = self.find_all(self.STREAMER_CARDS)
        return [card.find_element(By.TAG_NAME, "a") for card in cards]

    def select_streamer(self, index: int = 0) -> str:
        links = self.get_streamer_links()
        chosen = links[index]
        identifier = chosen.text.strip() or chosen.get_attribute("href")
        self.click_element(chosen)
        return identifier
