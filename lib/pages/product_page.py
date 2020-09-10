"""product_page.py - module that contains classes and methods related to Product page."""

import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Class that contains methods of Login page ."""

    def add_product_to_basket(self):
        """Adds product to basket."""

        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_btn.click()
        time.sleep(2)
        self.solve_quiz_and_get_code()

    def should_be_product_details_page(self):
        assert self.is_element_present(*ProductPageLocators.BOOKS_NAME), "Book's name is not present"
        assert self.is_element_present(*ProductPageLocators.BOOKS_PRICE), "Book's price is not present"
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "\"Add to basket\" button is not " \
                                                                                   "clickable or not present "

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOKS_PRICE).text

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOKS_NAME).text

    def get_text_of_success_msg(self):
        return self.browser.find_element(*ProductPageLocators.MSG1).text

    def get_text_of_price_msg(self):
        return self.browser.find_element(*ProductPageLocators.MSG3).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MSG1), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MSG1, timeout=60), \
            "Success message is not disappeared , but should be"
