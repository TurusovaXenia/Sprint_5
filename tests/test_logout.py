from selenium.webdriver.support import expected_conditions as EC

import helpers
from locators import HeaderLocators, AuthorizationLocators
import data

class TestLogout:

    def test_logout_user_success(self, driver, wait, existing_user):
        wait.until(
            EC.visibility_of_element_located(HeaderLocators.LOGIN_BUTTON)).click()

        helpers.fill_login_form(driver, wait, existing_user, data.user_password)

        driver.find_element(*AuthorizationLocators.SIGNIN_BUTTON).click()

        wait.until(
            EC.visibility_of_element_located(HeaderLocators.LOGOUT_BUTTON)).click()

        assert wait.until(
            EC.invisibility_of_element_located(HeaderLocators.USERNAME_FIELD)), \
            "Имя пользователя все еще отображается в хедере"

        assert wait.until(
            EC.invisibility_of_element_located(HeaderLocators.USER_AVATAR)), \
            "Аватар пользователя все еще отображается в хедере"

        assert wait.until(
            EC.visibility_of_element_located(HeaderLocators.LOGIN_BUTTON)), \
            "Кнопка для входа не отображается в хедере"