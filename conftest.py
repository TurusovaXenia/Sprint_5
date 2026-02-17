import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import RegistrationLocators, HeaderLocators

import data
import helpers

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(data.test_url)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture
def existing_user(driver, wait):
    driver.find_element(*HeaderLocators.LOGIN_BUTTON).click()

    no_account_button = wait.until(
        EC.visibility_of_element_located(RegistrationLocators.NO_ACCOUNT_BUTTON))
    no_account_button.click()
    wait.until(EC.staleness_of(no_account_button))

    email = helpers.generate_email()
    helpers.register_user(driver, wait, email)

    wait.until(
        EC.visibility_of_element_located(HeaderLocators.LOGOUT_BUTTON)).click()

    driver.delete_all_cookies()

    return email