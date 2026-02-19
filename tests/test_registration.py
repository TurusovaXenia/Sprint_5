import pytest
from selenium.webdriver.support import expected_conditions as EC

import data
import helpers
from locators import HeaderLocators, HomePageLocators, RegistrationLocators


class TestRegistration:

    def test_register_new_user_success(self, driver, wait):
        helpers.open_registration_form(wait)

        helpers.fill_registration_form(driver, wait, helpers.generate_email(), data.user_password)

        wait.until(
            EC.element_to_be_clickable(RegistrationLocators.CREATE_ACCOUNT_BUTTON)).click()

        wait.until(
            EC.invisibility_of_element_located(RegistrationLocators.CONTAINER),
            message="Окно регистрации не закрылось после клика на кнопку 'Создать аккаунт'")

        wait.until(
            EC.visibility_of_element_located(HomePageLocators.CONTAINER),
            message='Не выполнен переход на главную страницу после регистрации')

        user_name_field = wait.until(
            EC.visibility_of_element_located(HeaderLocators.USER_NAME_FIELD),
            message="Регистрация не завершена: имя пользователя не появилось в хедере")

        assert user_name_field.text == data.exp_user_name, \
            f"Ожидаемое имя пользователя - '{data.exp_user_name}', но получено '{user_name_field.text}'"

        assert driver.find_element(*HeaderLocators.USER_AVATAR).is_displayed(), \
            "Аватар пользователя не отображается в хедере"

    @pytest.mark.parametrize(
        "invalid_email",
        [
            data.email_invalid_no_at,
            data.email_invalid_no_dot,
            data.email_invalid_chars
        ],
        ids=[
            "missing_at", "missing_dot", "special_chars"]
    )
    def test_register_user_email_invalid_shows_error(self, driver, wait, invalid_email):
        helpers.open_registration_form(wait)

        wait.until(
            EC.visibility_of_element_located(RegistrationLocators.EMAIL_FIELD)).send_keys(invalid_email)

        wait.until(
            EC.element_to_be_clickable(RegistrationLocators.CREATE_ACCOUNT_BUTTON)).click()

        message = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.EMAIL_ERROR))

        assert message.text == data.exp_error_message_email, \
            f"Ожидаемое сообщение '{data.exp_error_message_email}', но получено'{message.text}'"

        fields_to_check = [
            RegistrationLocators.EMAIL_FIELD_WRAPPER,
            RegistrationLocators.PASSWORD_FIELD_WRAPPER,
            RegistrationLocators.REPEAT_PASSWORD_FIELD_WRAPPER
        ]

        for locator in fields_to_check:
            actual_error_state = helpers.get_element_error_state(wait, locator)

            assert data.exp_error_input_class in actual_error_state['error_class'], \
                f"Поле {locator} не имеет класс {data.exp_error_input_class}"

            assert actual_error_state['color'] == data.exp_error_color_hex, \
                f"Поле {locator} не выделено {data.exp_error_color_hex} цветом, текущий цвет - {actual_error_state['color']}"

    def test_register_duplicate_user_shows_error(self, driver, wait, existing_user):
        helpers.open_registration_form(wait)

        helpers.fill_registration_form(driver, wait, existing_user, data.user_password)

        wait.until(
            EC.element_to_be_clickable(RegistrationLocators.CREATE_ACCOUNT_BUTTON)).click()

        message = wait.until(
            EC.visibility_of_element_located(RegistrationLocators.EMAIL_ERROR))

        assert message.text == data.exp_error_message_email, \
            f"Ожидаемое сообщение '{data.exp_error_message_email}', но получено '{message.text}'"

        fields_to_check = [
            RegistrationLocators.EMAIL_FIELD_WRAPPER,
            RegistrationLocators.PASSWORD_FIELD_WRAPPER,
            RegistrationLocators.REPEAT_PASSWORD_FIELD_WRAPPER
        ]

        for locator in fields_to_check:
            actual_error_state = helpers.get_element_error_state(wait, locator)

            assert data.exp_error_input_class in actual_error_state['error_class'], \
                f"Поле {locator} не имеет класс {data.exp_error_input_class}"

            assert actual_error_state['color'] == data.exp_error_color_hex, \
                f"Поле {locator} не выделено {data.exp_error_color_hex} цветом, текущий цвет - {actual_error_state['color']}"