"""locators.py - contains all classes with page locators"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """Class that contains list of Main page locators."""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    """Class that contains list of Login page locators."""

    EMAIL_LOGIN_FIELD = (By.CSS_SELECTOR, "input[name='login-username']")
    PASSWORD_LOGIN_FIELD = (By.CSS_SELECTOR, "input[name='login-password']")
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//button[@type = 'submit']/preceding-sibling::p/a")
    LOGIN_BUTTON = (By.XPATH, ".//button[@name= 'login_submit']")
    EMAIL_REGISTRATION_FIELD = (By.XPATH, ".//input[@name= 'registration-email']")
    PASSWORD_REGISTRATION_FIELD = (By.XPATH, ".//input[@name= 'registration-password1']")
    CONFIRM_PASSWORD_REGISTRATION_FIELD = (By.XPATH, ".//input[@name= 'registration-password2']")
    REGISTRATION_BUTTON = (By.XPATH, ".//button[@name= 'registration_submit']")


class ProductPageLocators:
    """Class that contains list of Product page locators."""

    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOKS_NAME = (By.CSS_SELECTOR, "div#content_inner div.row h1")
    BOOKS_PRICE = (By.CSS_SELECTOR, "div#content_inner div.row p.price_color")
    MSG1 = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(1)")
    MSG2 = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(2)")
    MSG3 = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(3)")

