from locators import LoginLocators as LL
from libs.helpers import CustomActions


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.helpers = CustomActions(self.driver)

    def is_sign_in_to_chat_on_page(self):
        return data.sign_in_message in self.extract_sign_in_message_text()

    def is_who_are_you_in_first_text_box(self):
        return data.who_are_you in self.extract_who_are_you_text()

    def is_who_are_you_talking_to_in_second_text_box(self):
        return data.who_are_you in self.extract_who_are_you_talkign_to_text()

    def extract_sign_in_message_text(self):
        text = self.helpers.get_text(
            LL.SIGN_IN_TEXT)
        return text

    def extract_who_are_you_text(self):
        text = self.helpers.get_text(
            LL.WHO_ARE_YOU)
        return text

    def extract_who_are_you_talking_to_text(self):
        text = self.helpers.get_text(
            LL.WHO_ARE_YOU_TALKING_TO)
        return text
