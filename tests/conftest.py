import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
    browser.config.driver_options = driver_options

    yield

    browser.quit()
