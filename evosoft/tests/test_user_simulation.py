import time
from pages.main_page import MainPage
from pages.market_watch_page import MarketWatchPage


class TestUserSimulation:
    """Тестируем действия пользователя на сайте."""

    def test_user_go_to_main_page(self, browser):
        LINK = 'https://www.nseindia.com/'
        page = MainPage(browser, LINK)
        page.open()
        page.should_be_correct_url(LINK)

    def test_user_can_scroll_down_page(self, browser):
        page = MainPage(browser, browser.current_url)
        page.scroll_to_chart()

    def test_user_can_select_graffic_niffty_bank(self, browser):
        page = MainPage(browser, browser.current_url, timeout=3)
        page.scroll_up_from_chart()
        page.click_chart_niffty_bank()
        time.sleep(1)

    def test_user_can_view_all_by_top_5_stocks_niffty_bank(self, browser):
        page = MainPage(browser, browser.current_url, timeout=5)
        time.sleep(3)
        page.scroll_down_from_the_nav_by_750_pixels()
        page.click_to_view_all()

    def test_user_can_select_niffty_alpha_50(self, browser):
        market_page = MarketWatchPage(browser, browser.current_url, timeout=5)
        check_link = "https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%20BANK"
        market_page.should_be_correct_url(check_link)
        market_page.select_from_the_list_niffty_alpha_50()
        time.sleep(2)

    def test_user_can_scroll_through_the_table_to_the_end(self, browser):
        market_page = MarketWatchPage(browser, browser.current_url, timeout=5)
        market_page.scroll_down_from_multi_select()
