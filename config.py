import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test_secret_key'
    DEBUG = False
    USERS_JSON_PATH = os.path.join(os.path.dirname(__file__), 'users.json')
    TEMPLATES_AUTO_RELOAD = True
    APPLICATION_NAME = 'User Data Flask App'
    ITEMS_PER_PAGE = 10

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}