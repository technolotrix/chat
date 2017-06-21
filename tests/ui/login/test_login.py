from nose.plugins.attrib import attr

from ..data import *
from ..chat.page import ChatPage
from page import LoginPage

from libs.sel.basedriver import BaseDriver


class TestLogin():

    def setup(self):
        self.driver = BaseDriver().driver
        self.chat_page = ChatPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.driver.get(BASEURL)
        self.login_page.wait_for_login_form()

    def teardown(self):
        self.driver.quit()

    def test_sign_in_message_is_on_page(self):
        assert self.login_page.is_sign_in_to_chat_on_page()

    def test_who_are_you_text_is_in_first_text_box(self):
        assert self.login_page.is_who_are_you_in_first_text_box()

    def test_who_are_you_talking_to_text_is_in_second_text_box(self):
        assert self.login_page.is_who_are_you_talking_to_in_second_text_box()

    @attr(priority='critical')
    def test_sign_in_to_chat_different_user_names_displays_chat_window(self):
        self.login_page.sign_in_to_chat(username_1, username_2)
        assert self.chat_page.is_chatting_text_on_page()

    def test_cannot_sign_in_to_chat_with_blank_first_username(self):
        self.login_page.sign_in_to_chat('', username_2)
        assert not self.chat_page.is_chatting_text_on_page()

    def test_cannot_sign_in_to_chat_with_blank_second_username(self):
        self.login_page.sign_in_to_chat(username_1, '')
        assert not self.chat_page.is_chatting_text_on_page()

    def test_cannot_sign_in_to_chat_with_both_usernames_blank(self):
        self.login_page.sign_in_to_chat('', '')
        assert not self.chat_page.is_chatting_text_on_page()

    @attr(keywords=['bug'])
    def test_cannot_sign_in_to_chat_with_duplicate_username(self):
        self.login_page.sign_in_to_chat(username_1, username_1)
        assert not self.chat_page.is_chatting_text_on_page()

