import selenium

from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException as Stale

from selenium.webdriver.support.ui import WebDriverWait

from libs.sel.basedriver import WAIT


class CustomActions():

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        try:
            element = self.driver.find_element(*locator)
        except (NoSuchElementException, ElementNotVisibleException, Stale) as e:
            return
        return element

    def find_all(self, locator):
        try:
            elements = self.driver.find_elements(*locator)
        except (NoSuchElementException, ElementNotVisibleException, Stale) as e:
            return []
        return elements

    def find_and_click(self, locator):
        element = self.find(locator)

        if element:
            element.click()
        return element

    def send_keys(self, locator, keys):
        locator = self.find(locator)
        locator.send_keys(keys)

    def fill_out_form(self, locator, text):
        element = self.find(locator)
        if element:
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        element = self.find(locator)

        if element:
            try:
                text = element.text
            except ElementNotVisibleException:
                return ''
            return text
        return ''

    def get_attribute(self, locator, attr):
        element = self.find(locator)

        if element:
            try:
                text = element.get_attribute(attr)
            except ElementNotVisibleException:
                return ''
            return text
        return ''

    def wait_for_element(self, locator):
        self.driver.implicitly_wait(0)
        wait = WebDriverWait(self.driver, WAIT)

        try:
            wait.until(lambda s: s.find_element(*locator).is_displayed())
        except (TimeoutException, ElementNotVisibleException, Stale) as e:
            return False
        else:
            return True
        finally:
            self.driver.implicitly_wait(WAIT)
