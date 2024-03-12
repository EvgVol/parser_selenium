from selenium.webdriver.common.by import By


class LocatorsMainPage:
    """Локаторы на главной таблице."""

    MARKET_DATA = (By.XPATH, "//*[@id='link_2']")
    PRE_OPEN_MARKET = (By.XPATH, "//*[@id='main_navbar']/ul/li[3]/div/div[1]/div/div[1]/ul/li[1]/a")
    CHART = (By.ID, "tab1_container")
    NIFTY_BANK = (By.ID, "tabList_NIFTYBANK")
    NAVIGATOR = (By.CSS_SELECTOR, "#nse-indices > nav > div > div")
    VIEW_ALL = (By.CSS_SELECTOR, "#tab4_gainers_loosers > div.link-wrap > a")


class LocatorsPreOpenMarket:
    """Локаторы на странице Pre-Open Market."""

    TABLE = (By.XPATH, "//*[@id='livePreTable']/tbody")
    ROWS = (By.CSS_SELECTOR, "tr[class]")
    NAME = (By.XPATH, "td[2]/a")
    PRICE = (By.XPATH, "td[7]")


class LocatorsMarketWatch:
    """Локаторы на странице Market Watch."""

    SELECTOR_BANK = (By.ID, "equitieStockSelect")
    FOOTER_TABLE = (By.XPATH, "//*[@id='equityStockTable']/tbody/tr[51]")
