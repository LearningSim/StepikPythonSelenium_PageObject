from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose lang")


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")

    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)
    yield browser

    #sleep(5)
    print("\nquit browser..")
    browser.quit()
