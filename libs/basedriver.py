from config import APP_SETTINGS
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# For remote execution, if needed.  Not used in this code test, however.
COMMAND_EXECUTOR = 'http://hub:4444/wd/hub'
# I usually do not hard-code this here,
# but there is not much need for complex configuration
BASEURL = 'https://simple-chat-asapp.herokuapp.com/'
VALID_BROWSERS = ("chrome", "firefox", "phantomjs")
# For resizing the browser window, if desired.
SIZE = (900, 760)
WAIT = 3


class BaseDriver():

    def __init__(self):

        self.browser = APP_SETTINGS.BROWSER
        # To run tests on your local machine
        self.run_local = APP_SETTINGS.LOCAL_SELENIUM

        if self.browser not in VALID_BROWSERS:
            raise Exception(
                "Invalid browser!  Allowed types are {0}".format(VALID_BROWSERS))

        self.make_driver(self.browser)

    def make_local_driver(self, browser):
        drivers = {
            'firefox': webdriver.Firefox,
            'chrome': webdriver.Chrome,
            'phantomjs': webdriver.PhantomJS
            }

        return drivers.get(browser)()

    def make_remote_driver(self, browser):
        drivers = {
            'firefox': {
                'desired_capabilities': DesiredCapabilities.FIREFOX,
                },
            'chrome': {
                'desired_capabilities': DesiredCapabilities.CHROME,
                },
            'phantomjs': {
                'desired_capabilities': DesiredCapabilities.PHANTOMJS,
                }
            }

        driver = drivers.get(browser)
        driver['command_executor'] = COMMAND_EXECUTOR

        return webdriver.Remote(driver)

    def set_window_size(self, wait=WAIT, size=None):
        self.driver.implicitly_wait(WAIT)
        if size and isinstance(size, tuple):
            self.driver.set_window_size(size)

    def make_driver(self, browser, size=None):
        if self.run_local:
            self.make_local_driver()
        else:
            self.make_remote_driver()

        self.set_window_size()
