class BaseConfig(object):
	DEBUG = False
	TESTING = False

class Development(BaseConfig):
	DEBUG = True
	TESTING = True

class Production(BaseConfig):
	DEBUG = False

class Testing(BaseConfig):
	TESTING = True

