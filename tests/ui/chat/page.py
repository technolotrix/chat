from ..data import *

from ..locators import ChatLocators as CL
from ..login.page import LoginPage

from libs.sel.helpers import CustomActions


class ChatPage():

    def __init__(self, driver):
        self.driver = driver
        self.helpers = CustomActions(self.driver)
        self.login = LoginPage(self.driver)

    def is_chatting_text_on_page(self):
        return chatting_text in self.extract_chatting_text()

    def is_chatting_with_text_on_page(self, first_user, second_user):
        message = chatting_with_text.format(first_user, second_user)
        return message in self.extract_chatting_with_text()

    def is_say_something_placeholder_in_message_bar(self):
        return say_something_text in self.extract_say_something_text()

    def is_message_sent(self, message):
        return message in self.extract_newest_message()

    def is_chat_blank(self):
        return [] == self.extract_all_messages()

    def is_correct_sender(self, username):
        return '{0}:'.format(username) in self.extract_sender_username()

    def extract_chatting_text(self):
        text = self.helpers.get_text(
            CL.CHATTING_TEXT)
        return text

    def extract_chatting_with_text(self):
        text = self.helpers.get_text(
            CL.CHATTING_WITH_TEXT)
        return text

    def extract_say_something_text(self):
        text = self.helpers.get_attribute(
            CL.ENTER_TEXT, 'placeholder')
        return text

    def extract_all_messages(self):
        all_messages = self.helpers.find_all(CL.MESSAGE)
        return all_messages

    def extract_newest_message(self):
        all_messages = self.extract_all_messages()
        last_message_text = CL.MESSAGE_TEXT[1].format(
            len(all_messages)) # nth child uses index(1)

        new_tuple = (CL.MESSAGE_TEXT[0], last_message_text)
        return self.helpers.get_text(new_tuple)

    def extract_sender_username(self):
        all_messages = self.helpers.find_all(CL.MESSAGE)
        last_message_username = CL.MESSAGE_FROM[1].format(
            len(all_messages)) # nth child uses index(1)

        new_tuple = (CL.MESSAGE_FROM[0], last_message_username)
        return self.helpers.get_text(new_tuple)

    def log_in_to_chat(self, user1, user2):
        self.login.sign_in_to_chat(user1, user2)

    def send_message(self, message):
        self.helpers.fill_out_form(CL.ENTER_TEXT, message)
        self.helpers.find_and_click(CL.SEND_BUTTON)
        self.helpers.wait_for_element(CL.MESSAGE)
