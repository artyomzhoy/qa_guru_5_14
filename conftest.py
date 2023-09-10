import os

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils import attach


@pytest.fixture(scope='function',
                autouse=True,
                params=[(1920, 1080), (1600, 900), (1366, 768), (375, 667), (667, 375), (480, 800)],
                ids=['desktop', 'desktop', 'desktop', 'mobile', 'mobile', 'mobile'])
def browser_size(request):
    size = request.param
    ids = request.node.callspec.id

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": '100.0',
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = size[0]
    browser.config.window_height = size[1]

    yield browser, ids

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.close()
