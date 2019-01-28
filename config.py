import datetime

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    JWT_EXPIRATION_DELTA = datetime.timedelta(minutes=10)
    JWT_AUTH_URL_RULE = '/login'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class TestingConfig(BaseConfig):
    DEBUG=True
    TESTING = True

