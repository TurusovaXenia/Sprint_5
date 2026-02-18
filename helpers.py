from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color

from locators import RegistrationLocators, AuthorizationLocators, HeaderLocators

def generate_email(domain='test.com'):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return f'test_{timestamp}@{domain}'

def get_element_error_state(wait, locator):
    element = wait.until(EC.visibility_of_element_located(locator))
    error_class = element.get_attribute('class')

    rgba = element.value_of_css_property('border-color')
    hex_color = Color.from_string(rgba).hex.upper()

    return {
        "error_class": error_class,
        "color": hex_color,
    }

def open_registration_form(wait):
    wait.until(
        EC.element_to_be_clickable(HeaderLocators.LOGIN_BUTTON)).click()

    no_account_button = wait.until(
        EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON))
    no_account_button.click()
    wait.until(EC.staleness_of(no_account_button))

def fill_registration_form(driver, wait, email, password):
    wait.until(
        EC.visibility_of_element_located(RegistrationLocators.EMAIL_FIELD))
    driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*RegistrationLocators.REPEAT_PASSWORD_FIELD).send_keys(password)

def fill_login_form(driver, wait, email, password):
    wait.until(
        EC.visibility_of_element_located(AuthorizationLocators.EMAIL_FIELD))
    driver.find_element(*AuthorizationLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*AuthorizationLocators.PASSWORD_FIELD).send_keys(password)

def generate_notice_name():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return f'Набор_{timestamp}'