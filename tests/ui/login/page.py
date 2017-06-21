from ..data import sign_in_message, who_are_you, who_are_you_talking_to

from ..locators import LoginLocators as LL
from libs.sel.helpers import CustomActions


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.helpers = CustomActions(self.driver)

    def is_sign_in_to_chat_on_page(self):
        return sign_in_message in self.extract_sign_in_message_text()

    def is_who_are_you_in_first_text_box(self):
        return who_are_you in self.extract_who_are_you_text()

    def is_who_are_you_talking_to_in_second_text_box(self):
        return who_are_you_talking_to in self.extract_who_are_you_talking_to_text()

    def wait_for_login_form(self):
        self.helpers.wait_for_element(LL.LOGIN_BUTTON)

    def extract_sign_in_message_text(self):
        text = self.helpers.get_text(
            LL.SIGN_IN_TEXT)
        return text

    def extract_who_are_you_text(self):
        text = self.helpers.get_attribute(
            LL.WHO_ARE_YOU, 'placeholder')
        return text

    def extract_who_are_you_talking_to_text(self):
        text = self.helpers.get_attribute(
            LL.WHO_ARE_YOU_TALKING_TO, 'placeholder')
        return text

    def type_in_first_username(self, username):
        self.helpers.fill_out_form(LL.WHO_ARE_YOU, username)

    def type_in_second_username(self, username):
        self.helpers.fill_out_form(LL.WHO_ARE_YOU_TALKING_TO, username)

    def click_login_button(self):
        self.helpers.find_and_click(LL.LOGIN_BUTTON)

    def sign_in_to_chat(self, uname_1, uname_2):
        self.type_in_first_username(uname_1)
        self.type_in_second_username(uname_2)
        self.click_login_button()
