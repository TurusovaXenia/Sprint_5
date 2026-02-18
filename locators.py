from selenium.webdriver.common.by import By


class RegistrationLocators:
    CONTAINER = (By.CSS_SELECTOR, "form[class^='popUp_shell']")
    NO_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "div[class^='popUp_buttonRow'] button[type='button']")
    EMAIL_FIELD = (By.NAME, "email")
    EMAIL_ERROR = (By.XPATH, "(.//form[contains(@class, 'popUp_shell')]//span)[1]")
    EMAIL_FIELD_WRAPPER = (By.XPATH, "//input[@name='email']/..")
    PASSWORD_FIELD = (By.NAME, "password")
    PASSWORD_FIELD_WRAPPER = (By.XPATH, "//input[@name='password']/..")
    REPEAT_PASSWORD_FIELD = (By.NAME, "submitPassword")
    REPEAT_PASSWORD_FIELD_WRAPPER = (By.XPATH, "//input[@name='submitPassword']/..")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "div[class^='popUp_buttonRow'] button[type='submit']")

class AuthorizationLocators:
    CONTAINER = (By.CSS_SELECTOR, "form[class^='popUp_shell']")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    SIGNIN_BUTTON = (By.CSS_SELECTOR, "div[class^='popUp_buttonRow'] button[type='submit']")

class HeaderLocators:
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    CREATE_NOTICE_BUTTON = (By.XPATH, ".//button[text()='Разместить объявление']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[contains(@class, 'spanGlobal')]")
    USERNAME_FIELD = (By.CSS_SELECTOR, "div[class^='header'] h3")
    USER_AVATAR = (By.CLASS_NAME, "circleSmall")

class NoticeLocators:
    NAME_FIELD = (By.NAME, "name")
    DESCRIPTION_FIELD = (By.NAME, "description")
    PRICE_FIELD = (By.NAME, "price")
    CATEGORY_DROPDOWN_ARROW_BUTTON = (By.XPATH,
                                      "(.//div[contains(@class, 'dropDownMenu_input')])[1]/button")
    SELECTED_CATEGORY_ITEM = (By.XPATH,
                              "(.//div[contains(@class, 'dropDownMenu_dropMenu')])[1]//button[contains(@class, 'dropDownMenu_btn')][4]")
    CITY_DROPDOWN_ARROW_BUTTON = (By.XPATH, "(.//div[contains(@class, 'dropDownMenu_input')])[2]/button")
    SELECTED_CITY_ITEM = (By.XPATH,
                          "(.//div[contains(@class, 'dropDownMenu_dropMenu')])[2]//button[contains(@class, 'dropDownMenu_btn')][6]")
    SELECTED_CONDITION = (By.CSS_SELECTOR, "input[value='Б/У']")
    POST_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

class MainPageLocators:
    CONTAINER = (By.CSS_SELECTOR, "div[class^='homePage']")
    NAME_FIELD = (By.NAME, "name")
    CATEGORY_DROPDOWN_ARROW_BUTTON = (By.XPATH,
                                      "(.//div[contains(@class, 'dropDownMenu_input')])[1]/button")
    SELECTED_CATEGORY_ITEM = (By.XPATH,
                              "(.//div[contains(@class, 'dropDownMenu_dropMenu')])[1]//button[contains(@class, 'dropDownMenu_btn')][4]")
    CITY_DROPDOWN_ARROW_BUTTON = (By.XPATH, "(.//div[contains(@class, 'dropDownMenu_input')])[2]/button")
    SELECTED_CITY_ITEM = (By.XPATH,
                          "(.//div[contains(@class, 'dropDownMenu_dropMenu')])[2]//button[contains(@class, 'dropDownMenu_btn')][6]")
    PRICE_FIELD = (By.NAME, "price")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")