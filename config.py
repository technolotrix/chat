import os


class Config(object):
    LOCAL_SELENIUM = False

class LocalConfig(Config):
    LOCAL_SELENIUM = True

configs = {
    'local': LocalConfig,
    'prod': Config
    }

BROWSER = os.environ.get('BROWSER')
APP_SETTINGS = configs.get(os.environ.get('TARGET'))
