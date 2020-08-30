from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    EMAIL_LOGIN_FIELD = (By.CSS_SELECTOR, "input[name='login-username']")
    PASSWORD_LOGIN_FIELD = (By.CSS_SELECTOR, "input[name='login-password']")
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//button[@type = 'submit']/preceding-sibling::p/a")
    LOGIN_BUTTON = (By.XPATH, ".//button[@name= 'login_submit']")
    EMAIL_REGISTRATION_FIELD = (By.XPATH, ".//input[@name= 'registration-email']")
    PASSWORD_REGISTRATION_FIELD = (By.XPATH, ".//input[@name= 'registration-password1']")
    CONFIRM_PASSWORD_REGISTRATION_FIELD = (By.XPATH, ".//input[@name= 'registration-password2']")
    REGISTRATION_BUTTON = (By.XPATH, ".//button[@name= 'registration_submit']")
