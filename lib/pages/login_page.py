"""login_page.py - Contains all classes and its method related to Login page."""
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Login page that contains method related to Login page."""
    def should_be_login_page(self):
        self.should_be_login_url()
        print("login page")
        self.should_be_login_form()
        print("It is login form")
        self.should_be_register_form()
        print("It is reg form")

    def should_be_login_url(self):
        """Checks current url address."""
        assert "login" in self.browser.current_url, "This is wrong url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN_FIELD), "Login email field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN_FIELD), "Login password field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTRATION_FIELD), "Registration email field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTRATION_FIELD), "Registration password field is not " \
                                                                                "presented "
        assert self.is_element_present(*LoginPageLocators.CONFIRM_PASSWORD_REGISTRATION_FIELD), "Confirm registration " \
                                                                                        "password field isn't presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is not presented"
