"""Central configuration for the WAP (Web App) test framework.

Keeping every environment/tunable value in one module means test and page
files never hardcode URLs, timeouts or device names — changing the target
environment or device is a one-line edit here.
"""
import os

# --- Application under test -------------------------------------------------
BASE_URL = "https://www.twitch.tv"
SEARCH_TERM = "StarCraft II"

# --- Mobile emulation ---------------------------------------------------
# Any device name supported by Chrome DevTools' built-in device list.
MOBILE_DEVICE = "iPhone 12 Pro"

# --- Waits -------------------------------------------------------------
DEFAULT_TIMEOUT = 15
POPUP_TIMEOUT = 2

# --- Artifacts -----------------------------------------------------------
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOT_DIR = os.path.join(ROOT_DIR, "reports", "screenshots")
