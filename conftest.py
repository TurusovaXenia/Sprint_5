import pytest
from selenium import webdriver

import data

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(data.test_url)
    yield driver
    driver.quit()