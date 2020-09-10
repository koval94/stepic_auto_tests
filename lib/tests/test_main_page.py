from lib.pages.login_page import LoginPage
from lib.pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    print(f"Page is: {browser.current_url}")
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
