import os
import settings

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    BROWSER = 'chrome'
    LOCAL_SELENIUM = False

class LocalConfig(Config):
    DEBUG = True
    BROWSER = 'chrome'
    LOCAL_SELENIUM = True
