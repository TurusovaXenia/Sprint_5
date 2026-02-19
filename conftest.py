import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import data
import helpers
from locators import HeaderLocators, RegistrationLocators


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(data.base_url)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture(scope='function')
def existing_user(driver, wait):
    wait.until(
        EC.element_to_be_clickable(HeaderLocators.LOGIN_BUTTON)).click()

    no_account_button = wait.until(
        EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON))
    no_account_button.click()
    wait.until(EC.staleness_of(no_account_button))

    email = helpers.generate_email()
    password = data.user_password

    helpers.fill_registration_form(driver, wait, email, password)

    wait.until(
        EC.element_to_be_clickable(RegistrationLocators.CREATE_ACCOUNT_BUTTON)).click()

    wait.until(
        EC.element_to_be_clickable(HeaderLocators.LOGOUT_BUTTON),
        message="Пользователь не был авторизирован после регистрации").click()

    driver.delete_all_cookies()

    return email