from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import LocatorsMarketWatch


class MarketWatchPage(BasePage):

    def select_from_the_list_niffty_alpha_50(self):
        multi_select = self.browser.find_element(*LocatorsMarketWatch.SELECTOR_BANK)
        select = Select(multi_select)
        select.select_by_visible_text('NIFTY ALPHA 50')

    def scroll_down_to_footer_table(self):
        self.scroll_to_element(LocatorsMarketWatch.FOOTER_TABLE)

    def scroll_down_from_multi_select(self):
        self.scroll_from_element(LocatorsMarketWatch.SELECTOR_BANK, 0, 350)