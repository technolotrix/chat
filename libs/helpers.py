import os

import selenium

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.switch_to import SwitchTo

from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException as Stale

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from libs.sel.basedriver import WAIT


class CustomActions():

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        try:
            element = self.driver.find_element(*locator)
        except (NoSuchElementException, ElementNotVisibleException, Stale) as e:
            return False
        return element

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

    def hover_over_element(self, locator):
        element = self.find(locator)

        if element:
            hover = ActionChains(self.driver).move_to_element(element)
            hover.click_and_hold(element)
            hover.perform()
            hover.release(element)

    def get_css_property(self, locator, css_property):
        return str(self.find(locator).value_of_css_property(str(css_property)))

    def execute_js(self, script, option=''):
        self.driver.execute_script(str(script), option)

    def move_to_offset_and_click(self, x, y):
        actions = ActionChains(self.driver)
        actions.move_by_offset(x, y)
        actions.click()
        actions.perform()

    def scroll_to(self, x, y):
        self.driver.execute_script("window.scrollTo({0}, {1});".format(x, y))

    def return_coordinates(self, locator):
        element = self.find(locator)

        if element:
            try:
                loc = element.location
            except ElementNotVisibleException:
                return {}
            return loc
        return {}

    def get_text(self, locator):
        element = self.find(locator)

        if element:
            try:
                text = element.text
            except ElementNotVisibleException:
                return ''
            return text
        return ''

    def extract_attribute(self, locator, attribute):
        element = self.find(locator)
        if element:
            try:
                attr = element.get_attribute(attribute)
            except ElementNotVisibleException:
                return ''
            return attr
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

    def wait_for_not_element(self, locator):
        self.driver.implicitly_wait(0)
        wait = WebDriverWait(self.driver, WAIT)

        try:
            wait.until_not(lambda s: s.find_element(*locator).is_displayed())
        except (TimeoutException, ElementNotVisibleException, Stale) as e:
            return False
        else:
            return True
        finally:
            self.driver.implicitly_wait(WAIT)

    def wait_for_element_to_be_visible(self, locator):
        try:
            WebDriverWait(self.driver, 12).until(EC.visibility_of_element_located(locator))
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException, ElementNotVisibleException) as e:
            print("Element {0} is not visible after wait. Error message: {1}".format(locator, e))
            return False
        else:
            return True

    def wait_for_element_to_be_clickable(self, locator):
        try:
            WebDriverWait(self.driver, 12).until(EC.element_to_be_clickable(locator))
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException, ElementNotVisibleException) as e:
            print("Element {0} is not found after wait, so it cannot be clicked. Error message: {1}".format(locator, e))
            return False
        else:
            return True

    def is_in_view(self, locator):
        try:
            WebDriverWait(self.driver, 2).until(wait_for_element_to_be_in_view(locator))
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException, ElementNotVisibleException) as e:
            print("Element {0} is not visible in the viewport after wait. Error message: {1}".format(locator, e))
            return False
        else:
            return True
