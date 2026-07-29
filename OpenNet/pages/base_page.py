import os

from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import settings


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.DEFAULT_TIMEOUT)

    # --- navigation -----------------------------------------------------
    def open(self, url):
        self.driver.get(url)

    # --- element lookup / interaction -----------------------------------
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.click_element(self.find_clickable(locator))

    def click_element(self, element):
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def wait_for_url_contains(self, fragment: str, timeout: int = None):
        timeout = timeout if timeout is not None else settings.DEFAULT_TIMEOUT
        WebDriverWait(self.driver, timeout).until(EC.url_contains(fragment))

    def type_text(self, locator, text):
        field = self.find(locator)
        field.clear()
        field.send_keys(text)

    # --- scrolling --------------------------------------------------------
    def scroll_down(self, times: int = 1, pixels: int = 900):
        for _ in range(times):
            self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    # --- pop-ups / modals ---------------------------------------------------
    def dismiss_popup_if_present(self, locator, timeout: int = None) -> bool:
        timeout = timeout if timeout is not None else settings.POPUP_TIMEOUT
        try:
            close_button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            close_button.click()
            return True
        except TimeoutException:
            return False

    # --- artifacts --------------------------------------------------------
    def take_screenshot(self, name: str) -> str:
        os.makedirs(settings.SCREENSHOT_DIR, exist_ok=True)
        path = os.path.join(settings.SCREENSHOT_DIR, f"{name}.png")
        self.driver.save_screenshot(path)
        return path
