"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import time
import allure
import pytest
from allure_commons.types import Severity
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'artyomzhoy')
@allure.feature('Главная страница GitHub')
@allure.story('Соотношение сторон браузера под DESKTOP')
@allure.link('https://github.com', name='GitHub.')
def test_github_desktop(browser_size):
    web_browser, ids = browser_size
    if 'mobile' in ids:
        pytest.skip('Соотношение сторон не для десктопа.')
    open_main_page('')
    click_sign_in_desktop()


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'artyomzhoy')
@allure.feature('Главная страница GitHub')
@allure.story('Соотношение сторон браузера под MOBILE')
@allure.link('https://github.com', name='GitHub.')
def test_github_mobile(browser_size):
    web_browser, ids = browser_size
    if 'desktop' in ids:
        pytest.skip('Соотношение сторон не для мобильных устройств.')
    open_main_page('')
    click_sign_in_mobile()


@allure.step('Открытие главной страницы')
def open_main_page(page):
    browser.open(page)


@allure.step('Нажатие Sign In - DESKTOP')
def click_sign_in_desktop():
    browser.element('.HeaderMenu-link--sign-in').click()
    time.sleep(5)


@allure.step('Нажатие Sign In - MOBILE')
def click_sign_in_mobile():
    browser.element('.flex-column [aria-label="Toggle navigation"]').click()
    browser.element('a.HeaderMenu-link--sign-in').click()
    time.sleep(5)
