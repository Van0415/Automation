from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import settings


def create_mobile_driver(device_name: str = settings.MOBILE_DEVICE) -> webdriver.Chrome:
    """Return a Chrome WebDriver running Chrome's built-in mobile emulator."""
    options = Options()
    options.add_experimental_option("mobileEmulation", {"deviceName": device_name})
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0)  # explicit waits only, see pages/base_page.py
    return driver
