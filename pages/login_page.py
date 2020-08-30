from .base_page import BasePage
from .locators import LoginPage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPage.EMAIL_LOGIN_FIELD), "Login email field is not presented"
        assert self.is_element_present(*LoginPage.PASSWORD_LOGIN_FIELD), "Login password field is not presented"
        assert self.is_element_present(*LoginPage.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPage.EMAIL_REGISTRATION_FIELD), "Registration email field is not presented"
        assert self.is_element_present(*LoginPage.PASSWORD_REGISTRATION_FIELD), "Registration password field is not " \
                                                                                "presented "
        assert self.is_element_present(*LoginPage.CONFIRM_PASSWORD_REGISTRATION_FIELD), "Confirm registration " \
                                                                                        "password field isn't presented"
        assert self.is_element_present(*LoginPage.REGISTRATION_BUTTON), "Registration button is not presented"
