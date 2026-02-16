from selenium.webdriver.common.by import By


class RegistrationLocators:
    LOGIN_BUTTON = (By.XPATH, ".//div[contains(@class,'header_flexRow')]//button[text()='Вход и регистрация']")
    NO_ACCOUNT_BUTTON = (By.XPATH, ".//div[contains(@class,'popUp_buttonRow')]//button[text()='Нет аккаунта']")
    EMAIL_FIELD = (By.XPATH, ".//form[.//h1[text() = 'Зарегистрироваться']]//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, ".//form[.//h1[text() = 'Зарегистрироваться']]//input[@name='password']")
    REPEAT_PASSWORD_FIELD = (By.XPATH, ".//form[.//h1[text() = 'Зарегистрироваться']]//input[@name='submitPassword']")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "div[class^='popUp_buttonRow'] button[type='submit']")

class AuthorizationLocators:
    SIGNIN_BUTTON = (By.XPATH, ".//div[contains(@class,'popUp_buttonRow')]//button[text()='Войти']")
    EMAIL_FIELD = (By.XPATH, ".//form[.//h1[text() = 'Войти']]//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, ".//form[.//h1[text() = 'Войти']]//input[@name='password']")
    LOGOUT_BUTTON = (By.XPATH, ".//div[contains(@class,'header')]//button[contains(@class, 'spanGlobal')]")

class NoticeLocators:
    CREATE_NOTICE_BUTTON = (By.XPATH, ".//div[contains(@class,'header_flexRow')]//button[text()='Разместить объявление']")
    NAME_FIELD = (By.XPATH, ".//div[contains(@class,'createListingPage')]//input[@name='name']")
    DESCRIPTION_FIELD = (By.XPATH, ".//div[contains(@class,'createListingPage')]//textarea[@name='description']")
    PRICE_FIELD = (By.XPATH, ".//div[contains(@class,'createListingPage')]//input[@name='price']")
    CATEGORY_DROPDOWN_ARROW_BUTTON = (By.XPATH,
                                      "(.//div[contains(@class,'createListingPage')]//div[contains(@class, 'dropDownMenu_input')])[1]/button")
    SELECTED_CATEGORY_ITEM = (By.XPATH,
                              "(.//div[contains(@class,'createListingPage')]//div[contains(@class, 'dropDownMenu_dropMenu')])[1]//button[contains(@class, 'dropDownMenu_btn')][4]")
    CITY_DROPDOWN_ARROW_BUTTON = (By.XPATH, "(.//div[contains(@class,'createListingPage')]//div[contains(@class, 'dropDownMenu_input')])[2]/button")
    SELECTED_CITY_ITEM = (By.XPATH,
                          "(.//div[contains(@class,'createListingPage')]//div[contains(@class, 'dropDownMenu_dropMenu')])[2]//button[contains(@class, 'dropDownMenu_btn')][6]")
    SELECTED_CONDITION = (By.XPATH, ".//div[contains(@class,'createListingPage')]//input[@value='Б/У']")
    POST_BUTTON = (By.CSS_SELECTOR, "div[class^='createListingPage'] button[type='submit']")

class SearchLocators:
    NAME_FIELD = (By.XPATH, ".//div[contains(@class,'homePage')]//input[@name='name']")
    CATEGORY_DROPDOWN_ARROW_BUTTON = (By.XPATH,
                                      "(.//div[contains(@class,'homePage')]//div[contains(@class, 'dropDownMenu_input')])[1]/button")
    SELECTED_CATEGORY_ITEM = (By.XPATH,
                              "(.//div[contains(@class,'homePage')]//div[contains(@class, 'dropDownMenu_dropMenu')])[1]//button[contains(@class, 'dropDownMenu_btn')][4]")
    CITY_DROPDOWN_ARROW_BUTTON = (By.XPATH, "(.//div[contains(@class,'homePage')]//div[contains(@class, 'dropDownMenu_input')])[2]/button")
    SELECTED_CITY_ITEM = (By.XPATH,
                          "(.//div[contains(@class,'homePage')]//div[contains(@class, 'dropDownMenu_dropMenu')])[2]//button[contains(@class, 'dropDownMenu_btn')][6]")
    PRICE_FIELD = (By.XPATH, ".//div[contains(@class,'homePage')]//input[@name='price']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "div[class^='homePage'] button[type='submit']")