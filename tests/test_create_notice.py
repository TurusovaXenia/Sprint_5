from selenium.webdriver.support import expected_conditions as EC

import helpers
from locators import HeaderLocators, AuthorizationLocators, NoticePageLocators, ProfilePageLocators, HomePageLocators
import data


class TestCreateNotice:

    def test_create_notice_unauthorized_user_shows_login_popup(self, driver, wait):
        driver.find_element(*HeaderLocators.CREATE_NOTICE_BUTTON).click()

        assert wait.until(
            EC.visibility_of_element_located(AuthorizationLocators.CONTAINER)), \
            "Окно для входа в систему не отображается"

        title = driver.find_element(*AuthorizationLocators.CONTAINER_TITLE)

        assert title.text == 'Чтобы разместить объявление, авторизуйтесь', \
            f"Ожидаемый заголовок окна - 'Чтобы разместить объявление, авторизуйтесь', но получено '{title.text}'"

    def test_create_notice_success(self, driver, wait, existing_user):
        wait.until(
            EC.visibility_of_element_located(HeaderLocators.LOGIN_BUTTON)).click()

        helpers.fill_login_form(driver, wait, existing_user, data.user_password)

        sign_in_button = driver.find_element(*AuthorizationLocators.SIGNIN_BUTTON)
        sign_in_button.click()
        wait.until(EC.staleness_of(sign_in_button))

        wait.until(
            EC.element_to_be_clickable(HeaderLocators.CREATE_NOTICE_BUTTON)).click()

        notice_name = helpers.generate_notice_name()
        wait.until(
            EC.visibility_of_element_located(NoticePageLocators.NAME_FIELD)).send_keys(notice_name)

        driver.find_element(*NoticePageLocators.DESCRIPTION_FIELD).send_keys(data.notice_description)
        driver.find_element(*NoticePageLocators.PRICE_FIELD).send_keys(data.notice_price)

        driver.find_element(*NoticePageLocators.CATEGORY_DROPDOWN_ARROW_BUTTON).click()
        driver.find_element(*NoticePageLocators.SELECTED_CATEGORY_ITEM).click()

        driver.find_element(*NoticePageLocators.CITY_DROPDOWN_ARROW_BUTTON).click()
        driver.find_element(*NoticePageLocators.SELECTED_CITY_ITEM).click()

        driver.find_element(*NoticePageLocators.SELECTED_CONDITION).click()
        driver.find_element(*NoticePageLocators.POST_BUTTON).click()

        wait.until(
            EC.visibility_of_element_located(HomePageLocators.CONTAINER))

        wait.until(
            EC.element_to_be_clickable(HeaderLocators.USER_AVATAR)).click()

        wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.CONTAINER))

        created_notice_name = wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.CREATED_NOTICE_NAME))

        assert created_notice_name.text == notice_name