from nose.tools import assert_true

from libs.basedriver import BaseDriver

from page import LoginPage#, ChatPage
from data import BASEURL

URL = BASEURL

class TestNav():

    @classmethod
    def setUpClass(self):
        self.driver = BaseDriver().driver
        #self.chat_page = ChatPage(self.driver)
        self.login_page = LoginPage(self.driver)

        # Given I am on the Login Page
        self.driver.get(URL)

    def test_login_as_user_1_talking_to_user_2(self):
        # when I type user 1 in box 1
        # and I type in user 2 in box 2
        # and I click Login
        # then I am logged in
        # and I see the chat box
