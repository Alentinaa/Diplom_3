import pytest
from selenium import webdriver
from urls import URLs


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('start-maximized')
        browser = webdriver.Chrome(options=chrome_options)
    browser.get(URLs.BASE_URL)
    yield browser
    browser.quit()

