import pytest
from pages.web_driver import WebDriver


@pytest.fixture(scope="class", params=["chrome"])
def browser(request):
    driver = WebDriver.open_browser(request.param)
    yield driver
    WebDriver.close_browser()
