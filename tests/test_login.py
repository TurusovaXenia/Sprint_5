from selenium.webdriver.support import expected_conditions as EC

import data
import helpers
from locators import AuthorizationLocators, HeaderLocators, HomePageLocators


class TestLogin:

    def test_login_user_success(self, driver, wait, existing_user):
        wait.until(
            EC.visibility_of_element_located(HeaderLocators.LOGIN_BUTTON)).click()

        helpers.fill_login_form(driver, wait, existing_user, data.user_password)

        wait.until(
            EC.element_to_be_clickable(AuthorizationLocators.SIGNIN_BUTTON)).click()

        wait.until(
            EC.invisibility_of_element_located(AuthorizationLocators.CONTAINER),
            message="Окно входа в систему не закрылось после нажатия кнопки 'Войти'")

        wait.until(
            EC.visibility_of_element_located(HomePageLocators.CONTAINER),
            message="Не выполнен переход на главную страницу после входа в систему")

        user_name_field = wait.until(
            EC.visibility_of_element_located(HeaderLocators.USER_NAME_FIELD),
            message="Вход не завершен: имя пользователя не появилось в хедере")

        assert user_name_field.text == data.exp_user_name, \
            f"Ожидаемое имя пользователя - '{data.exp_user_name}', но получено '{user_name_field.text}'"

        assert driver.find_element(*HeaderLocators.USER_AVATAR).is_displayed(), \
            "Аватар пользователя не отображается в хедере"