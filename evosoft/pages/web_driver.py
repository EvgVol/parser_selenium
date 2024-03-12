from selenium import webdriver


class WebDriver:
    _driver = None

    @classmethod
    def open_browser(cls, browser_name):
        if cls._driver is None:
            if browser_name == "chrome":
                cls._driver = webdriver.Chrome()
            elif browser_name == "firefox":
                cls._driver = webdriver.Firefox()
            else:
                raise ValueError(
                    "Unsupported browser name. Use 'chrome' or 'firefox'."
                )
        return cls._driver

    @classmethod
    def close_browser(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
