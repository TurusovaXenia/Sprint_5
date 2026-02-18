from selenium.webdriver.support import expected_conditions as EC

import data
import helpers
from locators import AuthorizationLocators, HeaderLocators


class TestLogout:

    def test_logout_user_success(self, driver, wait, existing_user):
        wait.until(
            EC.visibility_of_element_located(HeaderLocators.LOGIN_BUTTON)).click()

        helpers.fill_login_form(driver, wait, existing_user, data.user_password)

        wait.until(
            EC.element_to_be_clickable(AuthorizationLocators.SIGNIN_BUTTON)).click()

        wait.until(
            EC.element_to_be_clickable(HeaderLocators.LOGOUT_BUTTON)).click()

        wait.until(
            EC.invisibility_of_element_located(HeaderLocators.USER_NAME_FIELD)), \
            "Имя пользователя все еще отображается в хедере"

        assert len(driver.find_elements(*HeaderLocators.USER_AVATAR)) == 0, \
            "Аватар пользователя все еще отображается в хедере"

        assert wait.until(
            EC.visibility_of_element_located(HeaderLocators.LOGIN_BUTTON)), \
            "Кнопка для входа не отображается в хедере"