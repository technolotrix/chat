from selenium.webdriver.common.by import By


class LoginLocators(object):
        """
        QA best practice prefers IDs, but I have found that adding
        id elements is not always easy to implement/accepted by developers

        """

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