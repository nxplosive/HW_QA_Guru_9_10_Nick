from selene import browser
from selenium import webdriver
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
   browser.config.base_url = 'https://demoqa.com/automation-practice-form'
   driver_options = webdriver.ChromeOptions()
   driver_options.add_argument('--headless')
   browser_config.driver_options = driver_options
   browser_config.timeout = 2
   browser_config.window_width = 1920
   browser_config.window_height = 1080

   yield

   browser.quit()