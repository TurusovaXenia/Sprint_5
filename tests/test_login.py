from selenium.webdriver.support import expected_conditions as EC

import helpers
from locators import HeaderLocators, AuthorizationLocators, MainPageLocators
import data

class TestLogin:

    def test_login_user_success(self, driver, wait, existing_user):
        wait.until(
            EC.visibility_of_element_located(HeaderLocators.LOGIN_BUTTON)).click()

        helpers.fill_login_form(driver, wait, existing_user, data.user_password)

        driver.find_element(*AuthorizationLocators.SIGNIN_BUTTON).click()

        #проверка исчезновения окна логина
        wait.until(
            EC.invisibility_of_element_located(AuthorizationLocators.CONTAINER))

        # проверка перехода на главную страницу по уникальному элементу страницы
        wait.until(
            EC.visibility_of_element_located(MainPageLocators.CONTAINER))

        user_name_field = wait.until(
            EC.visibility_of_element_located(HeaderLocators.USERNAME_FIELD))

        user_avatar = wait.until(
            EC.visibility_of_element_located(HeaderLocators.USER_AVATAR))

        assert user_name_field.text == 'User.', f"Ожидаемое имя пользователя - 'User.', но получено '{user_name_field.text}'"
        assert user_avatar.is_displayed()