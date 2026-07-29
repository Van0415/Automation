from config import settings
from pages.home_page import TwitchHomePage
from pages.search_results_page import SearchResultsPage
from pages.streamer_page import StreamerPage


class TestTwitchStreamerSearch:
    def test_search_starcraft_and_screenshot_streamer(self, driver):
        home_page = TwitchHomePage(driver)
        home_page.load()
        home_page.open_search()
        home_page.search_for(settings.SEARCH_TERM)

        results_page = SearchResultsPage(driver)
        results_page.scroll_down(times=2)
        selected_streamer = results_page.select_streamer(index=0)

        streamer_page = StreamerPage(driver)
        streamer_page.wait_until_loaded()
        screenshot_path = streamer_page.capture_screenshot("starcraft2_streamer")

        assert selected_streamer, "Expected to select a streamer from the results"

