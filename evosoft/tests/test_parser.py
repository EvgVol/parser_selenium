from pages.main_page import MainPage
from pages.pre_open_market_page import PreOpenManagePage
from pages.locators import LocatorsMainPage


class TestParserDataOnTheSite:
    """Тестируем работу парсера на сайте."""

    def test_user_should_go_to_site(self, browser):
        LINK = 'https://www.nseindia.com/'
        page = MainPage(browser, LINK)
        page.open()
        page.should_be_correct_url(LINK)

    def test_user_should_move_to_marker_data(self, browser):
        page = MainPage(browser, browser.current_url)
        page.move_to_element(LocatorsMainPage.MARKET_DATA)

    def test_user_should_click_to_pre_order_market(self, browser):
        LINK = "https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market"
        page = MainPage(browser, browser.current_url)
        page.click_to_link_pre_order_market()
        market_page = PreOpenManagePage(browser,
                                        browser.current_url,
                                        timeout=5)
        market_page.should_be_correct_url(LINK)

    def test_user_should_parse_data_from_table(self, browser):
        market_page = PreOpenManagePage(browser,
                                        browser.current_url,
                                        timeout=15)
        market_page.scroll_to_table()
        market_page.parser_data()
