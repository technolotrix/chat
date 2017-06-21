from selenium.webdriver.common.by import By

"""
QA best practice prefers to use element IDs
for Selenium locators

"""


class LoginLocators(object):
    SIGN_IN_TEXT = (
        By.CSS_SELECTOR, '#content > div > h1')

    WHO_ARE_YOU = (
        By.CSS_SELECTOR, '#content > div > form > div:nth-child(1) > \
            input[type="text"]')

    WHO_ARE_YOU_TALKING_TO = (
        By.CSS_SELECTOR, '#content > div > form > div:nth-child(2) > \
            input[type="text"]')

    LOGIN_BUTTON = (
        By.CSS_SELECTOR, '#content > div > form > div:nth-child(3) > \
            button')


class ChatLocators(object):
    CHATTING_TEXT = (
       By.CSS_SELECTOR, '#content > div > h1')

    CHATTING_WITH_TEXT = (
        By.CSS_SELECTOR, '#content > div > h4')

    CHAT_WINDOW = (
       By.CSS_SELECTOR, '#chatBox')

    MESSAGE = (
        By.CSS_SELECTOR, '#chatBox > div.message')

    MESSAGE_FROM = (
       By.CSS_SELECTOR, '#chatBox > div:nth-child({}) > span.from')

    MESSAGE_TEXT = (
       By.CSS_SELECTOR, '#chatBox > div:nth-child({}) > span.text')

    ENTER_TEXT = (
       By.CSS_SELECTOR, '#content > div > form > input[type="text"]')

    SEND_BUTTON = (
       By.CSS_SELECTOR, '#content > div > form > button')
