from typing import Callable, Tuple
from dataclasses import dataclass

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


@dataclass
class BasePage:
    browser: Callable
    url: str
    timeout: int | float = 1

    def __post_init__(self):
        self.browser.implicitly_wait(self.timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_correct_url(self, link: str):
        assert self.browser.current_url == link, (
            "The current page URL does not match the expected URL"
        )

    def move_to_element(self, locator: Tuple[str, str]):
        hoverable = self.browser.find_element(*locator)
        ActionChains(self.browser).move_to_element(hoverable).perform()

    def click_by_element(self, locator: Tuple[str, str]):
        element = self.browser.find_element(*locator)
        assert element.is_displayed(), (
            "The element is not displayed on the page."
        )
        self.browser.execute_script(
            'return arguments[0].scrollIntoView(true)', element
        )
        element.click()

    def is_element_present(self, locator: Tuple[str, str], message: str):
        assert self.browser.find_element(*locator).is_displayed(), message

    def scroll_down_to_element(self, locator: Tuple[str, str]):
        element = self.browser.find_element(*locator)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView(true)', element
        )

    def scroll_from_element(self,
                            locator: Tuple[str, str],
                            count_px_up: int,
                            count_px_down: int):
        element = self.browser.find_element(*locator)
        assert element.is_displayed(), (
            "The element is not displayed on the page."
        )
        scroll_origin = ScrollOrigin.from_element(element)
        ActionChains(self.browser).scroll_from_origin(scroll_origin,
                                                      count_px_up,
                                                      count_px_down).perform()

    def scroll_to_element(self, locator: Tuple[str, str]):
        element = self.browser.find_element(*locator)
        assert element.is_displayed(), (
            "The element is not displayed on the page."
        )
        ActionChains(self.browser).scroll_to_element(element).perform()
