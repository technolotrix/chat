from nose.plugins.attrib import attr

from ..data import *
from page import ChatPage

from libs.sel.basedriver import BaseDriver

"""
Note:  I usually don't import * as a habit

"""

class TestChat():

    @classmethod
    def setUpClass(cls):
        cls.driver_1 = BaseDriver().driver
        cls.driver_2 = BaseDriver().driver
        cls.chat_page_1 = ChatPage(cls.driver_1)
        cls.chat_page_2 = ChatPage(cls.driver_2)
        cls.driver_1.get(BASEURL)
        cls.driver_2.get(BASEURL)

        # Log in as user1 --> user2
        cls.chat_page_1.log_in_to_chat(username_1, username_2)
        # Log in as user2 --> user1
        cls.chat_page_2.log_in_to_chat(username_2, username_1)

    def setup(self):
        # fix state if there are bugs so all tests run
        if self.chat_page_1.is_chatting_text_on_page() is False:
            self.chat_page_1.log_in_to_chat(username_1, username_2)

        if self.chat_page_2.is_chatting_text_on_page() is False:
            self.chat_page_2.log_in_to_chat(username_2, username_1)

    @classmethod
    def tearDownClass(cls):
        cls.driver_1.quit()
        cls.driver_2.quit()

    def test_chatting_message_is_on_chat_page_1(self):
        assert self.chat_page_1.is_chatting_text_on_page() is True

    def test_chatting_message_is_on_chat_page_2(self):
        assert self.chat_page_2.is_chatting_text_on_page() is True

    def test_username_1_talking_to_username_2_in_window_1(self):
        assert self.chat_page_1.is_chatting_with_text_on_page(
            username_1, username_2) is True

    def test_username_2_talking_to_username_1_in_window_2(self):
        assert self.chat_page_2.is_chatting_with_text_on_page(
            username_2, username_1) is True

    @attr(priority='critical')
    def test_send_message_as_user_1_to_user_2_shows_user_2_message(self):
        self.chat_page_1.send_message(hello_message)
        assert self.chat_page_2.is_message_sent(hello_message) is True

    @attr(priority='critical')
    def test_send_message_as_user_2_to_user_1_shows_user_1_message(self):
        self.chat_page_2.send_message(hello_2_message)
        assert self.chat_page_1.is_message_sent(hello_2_message) is True

    @attr(priority='critical')
    def test_send_message_as_user_1_to_user_2_shows_user_1_message(self):
        self.chat_page_1.send_message(hello_message)
        assert self.chat_page_1.is_message_sent(hello_message) is True

    def test_send_message_as_user_2_to_user_1_shows_user_2_message(self):
        self.chat_page_2.send_message(hello_2_message)
        assert self.chat_page_2.is_message_sent(hello_2_message) is True

    def test_say_something_placeholder_text_is_in_message_bar(self):
        assert self.chat_page_1.is_say_something_placeholder_in_message_bar() is True

    @attr(priority='critical')
    def test_send_message_as_user_1_to_user_3_does_not_show_user_2_message(self):
        driver_3 = BaseDriver().driver
        chat_page_3 = ChatPage(driver_3)
        driver_3.get(BASEURL)
        chat_page_3.log_in_to_chat(username_1, username_3)

        chat_page_3.send_message(secret_message)
        assert self.chat_page_2.is_message_sent(secret_message) is False

        driver_3.quit()

    @attr(keywords=['bug'])
    def test_send_message_that_is_too_long_does_not_break_application(self):
        self.chat_page_1.send_message(long_message)
        self.chat_page_1.send_message(hello_message)
        assert self.chat_page_2.is_message_sent(hello_message) is True

    @attr(keywords=['bug'])
    def test_send_message_with_comma_sends_message(self):
        self.chat_page_1.send_message(comma_message)
        assert self.chat_page_2.is_message_sent(comma_message) is True

    def test_new_chat_is_blank(self):
        driver_3 = BaseDriver().driver
        chat_page_3 = ChatPage(driver_3)
        driver_3.get(BASEURL)
        chat_page_3.log_in_to_chat(username_1, username_3)

        assert chat_page_3.is_chat_blank() is True

    def test_chat_message_appears_with_username_of_correct_sender(self):
        self.chat_page_1.send_message(hello_message)
        assert self.chat_page_1.is_correct_sender(username_1) is True

    @attr(keywords=['bug'])
    def test_refresh_chat_page_persists_session(self):
        self.driver_1.refresh()
        assert self.chat_page_1.is_chatting_text_on_page() is True
