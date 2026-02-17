from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color

from locators import RegistrationLocators
import data

def generate_email(domain='test.com'):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return f'test_{timestamp}@{domain}'

def get_hex_color(wait, locator):
    element = wait.until(EC.visibility_of_element_located(locator))
    rgba = element.value_of_css_property('border-color')
    return Color.from_string(rgba).hex.upper()

def has_error_class(wait, locator):
    element = wait.until(EC.visibility_of_element_located(locator))
    error_class = element.get_attribute('class')
    return error_class

def fill_registration_form(driver, email):
    driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys(data.user_password)
    driver.find_element(*RegistrationLocators.REPEAT_PASSWORD_FIELD).send_keys(data.user_password)