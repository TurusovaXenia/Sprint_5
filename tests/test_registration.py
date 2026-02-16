from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import helpers
from locators import RegistrationLocators, HeaderLocators, MainPageLocators
import data


class TestRegistration:

    def test_registration_success(self, driver):
        driver.get(data.test_url)
        driver.find_element(*RegistrationLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegistrationLocators.NO_ACCOUNT_BUTTON))

        driver.find_element(*RegistrationLocators.NO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegistrationLocators.EMAIL_FIELD))

        driver.find_element(*RegistrationLocators.EMAIL_FIELD).send_keys(helpers.generate_email())
        driver.find_element(*RegistrationLocators.PASSWORD_FIELD).send_keys(data.user_password)
        driver.find_element(*RegistrationLocators.REPEAT_PASSWORD_FIELD).send_keys(data.user_password)
        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HeaderLocators.USERNAME_FIELD))

        assert driver.find_element(*HeaderLocators.USERNAME_FIELD).text == 'User.'
        assert driver.find_element(*HeaderLocators.USER_AVATAR).is_displayed()
        assert driver.find_element(*MainPageLocators.SEARCH_BUTTON).is_displayed()


