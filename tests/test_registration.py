import pytest
from selenium.webdriver.support import expected_conditions as EC

import helpers
from locators import RegistrationLocators, HeaderLocators, MainPageLocators
import data


class TestRegistration:

    def test_register_user_success(self, driver, wait):
        driver.find_element(*HeaderLocators.LOGIN_BUTTON).click()

        no_account_button = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.NO_ACCOUNT_BUTTON))
        no_account_button.click()
        wait.until(EC.staleness_of(no_account_button))

        helpers.fill_registration_form(driver, wait, helpers.generate_email())

        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        #проверка исчезновения окна регистрации
        wait.until(
            EC.invisibility_of_element_located(RegistrationLocators.CONTAINER))

        #проверка перехода на главную страницу по уникальному элементу страницы
        wait.until(
            EC.visibility_of_element_located(MainPageLocators.CONTAINER))

        user_name_field = wait.until(
            EC.visibility_of_element_located(HeaderLocators.USERNAME_FIELD))
        assert user_name_field.text == 'User.', f"Ожидаемое имя пользователя - 'User.', но получено '{user_name_field.text}'"
        assert driver.find_element(*HeaderLocators.USER_AVATAR).is_displayed()

    @pytest.mark.parametrize("invalid_email",
        [data.email_without_at, data.email_without_dot, data.email_with_special_chars]
    )
    def test_register_user_email_invalid_shows_error(self, driver, wait, invalid_email):
        driver.find_element(*HeaderLocators.LOGIN_BUTTON).click()

        no_account_button = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.NO_ACCOUNT_BUTTON))
        no_account_button.click()
        wait.until(EC.staleness_of(no_account_button))

        wait.until(
            EC.visibility_of_element_located(RegistrationLocators.EMAIL_FIELD)).send_keys(invalid_email)

        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        message = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.EMAIL_ERROR))

        assert message.text == 'Ошибка', f"Ожидаемое сообщение 'Ошибка', но получено'{message.text}'"

        fields_to_check = [
            RegistrationLocators.EMAIL_FIELD_WRAPPER,
            RegistrationLocators.PASSWORD_FIELD_WRAPPER,
            RegistrationLocators.REPEAT_PASSWORD_FIELD_WRAPPER
        ]

        for locator in fields_to_check:
            actual_error_class = helpers.has_error_class(wait, locator)
            actual_hex_color = helpers.get_hex_color(wait, locator)

            assert 'input_inputError' in actual_error_class, f'Поле {locator} не имеет класс inputError'
            assert actual_hex_color == data.error_color, f'Поле {locator} не выделено красным цветом, текущий цвет - {actual_hex_color}'

    def test_register_duplicate_user_shows_error(self, driver, wait, existing_user):
        wait.until(
            EC.visibility_of_element_located(HeaderLocators.LOGIN_BUTTON)).click()

        no_account_button = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.NO_ACCOUNT_BUTTON))
        no_account_button.click()

        wait.until(EC.staleness_of(no_account_button))

        helpers.fill_registration_form(driver, wait, existing_user)

        driver.find_element(*RegistrationLocators.CREATE_ACCOUNT_BUTTON).click()

        message = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.EMAIL_ERROR))

        assert message.text == 'Ошибка', f"Ожидаемое сообщение 'Ошибка', но получено '{message.text}'"

        fields_to_check = [
            RegistrationLocators.EMAIL_FIELD_WRAPPER,
            RegistrationLocators.PASSWORD_FIELD_WRAPPER,
            RegistrationLocators.REPEAT_PASSWORD_FIELD_WRAPPER
        ]

        for locator in fields_to_check:
            actual_error_class = helpers.has_error_class(wait, locator)
            actual_hex_color = helpers.get_hex_color(wait, locator)

            assert 'input_inputError' in actual_error_class, f'Поле {locator} не имеет класс inputError'
            assert actual_hex_color == data.error_color, f'Поле {locator} не выделено красным цветом, текущий цвет - {actual_hex_color}'