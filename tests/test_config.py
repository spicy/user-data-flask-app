from config import get_config, DevelopmentConfig, TestingConfig, ProductionConfig
import os

def test_development_config():
    os.environ['FLASK_ENV'] = 'development'
    config = get_config()
    assert isinstance(config, DevelopmentConfig)
    assert config.DEBUG is True

def test_testing_config():
    os.environ['FLASK_ENV'] = 'testing'
    config = get_config()
    assert isinstance(config, TestingConfig)
    assert config.TESTING is True

def test_production_config():
    os.environ['FLASK_ENV'] = 'production'
    config = get_config()
    assert isinstance(config, ProductionConfig)
    assert config.DEBUG is False