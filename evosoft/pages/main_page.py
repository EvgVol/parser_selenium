from pages.base_page import BasePage
from pages.locators import LocatorsMainPage
from selenium.webdriver.support.ui import WebDriverWait


class MainPage(BasePage):

    def click_chart_niffty_bank(self):
        button = self.browser.find_element(*LocatorsMainPage.NIFTY_BANK)
        button.click()

    def click_to_link_pre_order_market(self):
        self.click_by_element(LocatorsMainPage.PRE_OPEN_MARKET)

    def click_to_view_all(self):
        link = self.browser.find_element(*LocatorsMainPage.VIEW_ALL)
        link.click()

    def scroll_to_chart(self):
        self.scroll_to_element(LocatorsMainPage.CHART)

    def scroll_down_from_the_nav_by_750_pixels(self):
        self.scroll_from_element(LocatorsMainPage.NIFTY_BANK, 0, 750)

    def scroll_up_from_chart(self):
        self.scroll_from_element(LocatorsMainPage.CHART, 300, 0)
