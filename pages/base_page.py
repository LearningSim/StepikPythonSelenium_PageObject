from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, browser, url):
        self.url = url
        self.browser: WebDriver = browser

    def open(self):
        self.browser.get(self.url)
