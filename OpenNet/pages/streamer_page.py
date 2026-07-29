from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class StreamerPage(BasePage):
    VIDEO_PLAYER = (By.CSS_SELECTOR, '[data-a-target="video-player"], video')

    # Pop-ups Twitch may show before the stream finishes loading.
    COOKIE_BANNER_ACCEPT = (By.CSS_SELECTOR, 'button[data-a-target="consent-banner-accept"]')
    MATURE_CONTENT_ACCEPT = (By.CSS_SELECTOR, 'button[data-a-target="player-overlay-mature-accept"]')
    # Generic fallback for any other confirm/close dialog Twitch may A/B test.
    GENERIC_DIALOG_ACCEPT = (
        By.CSS_SELECTOR,
        '[role="dialog"] button[data-a-target*="accept" i], '
        '[role="dialog"] button[aria-label*="close" i]',
    )

    def dismiss_known_popups(self):
        self.dismiss_popup_if_present(self.COOKIE_BANNER_ACCEPT)
        self.dismiss_popup_if_present(self.MATURE_CONTENT_ACCEPT)
        self.dismiss_popup_if_present(self.GENERIC_DIALOG_ACCEPT)

    def wait_until_loaded(self):
        self.dismiss_known_popups()
        self.find(self.VIDEO_PLAYER)
        # A pop-up can appear right as the player mounts, so check again.
        self.dismiss_known_popups()

    def capture_screenshot(self, name: str = "streamer_page") -> str:
        return self.take_screenshot(name)
