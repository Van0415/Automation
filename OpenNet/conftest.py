"""Shared pytest fixtures for the WAP test framework."""
import os

import pytest

from config import settings
from utils.driver_factory import create_mobile_driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Stash the outcome of each test phase on the item for use in fixtures."""
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture
def driver(request):
    """Yield a Chrome WebDriver running the mobile emulator, quitting after
    the test and capturing a failure screenshot if the test failed."""
    drv = create_mobile_driver()
    yield drv

    if getattr(request.node, "rep_call", None) is not None and request.node.rep_call.failed:
        os.makedirs(settings.SCREENSHOT_DIR, exist_ok=True)
        failure_path = os.path.join(settings.SCREENSHOT_DIR, f"FAILED_{request.node.name}.png")
        drv.save_screenshot(failure_path)

    drv.quit()
