import logging
import os


class BaseConfig:
    """Base configuration class for the application."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "test_secret_key")
    USERS_JSON_PATH = os.path.join(os.path.dirname(__file__), "users.json")
    TEMPLATES_AUTO_RELOAD = True
    APPLICATION_NAME = "User Data Flask App"
    ITEMS_PER_PAGE = int(os.environ.get("ITEMS_PER_PAGE", 10))
    HOMEPAGE_TITLE = "User List"
    USER_DETAIL_TITLE = "User Detail"
    ERROR_404_TITLE = "404 Not Found"
    ERROR_500_TITLE = "500 Internal Server Error"
    ERROR_404_MESSAGE = "The requested page could not be found."
    ERROR_500_MESSAGE = "An unexpected error has occurred. Please try again later."

    # Logging configuration
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_FILE = "logs/app.log"


class DevelopmentConfig(BaseConfig):
    """Configuration for development environment."""

    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class TestingConfig(BaseConfig):
    """Configuration for testing environment."""

    TESTING = True
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(BaseConfig):
    """Configuration for production environment."""

    DEBUG = False
    LOG_LEVEL = logging.ERROR


def get_config():
    """
    Returns the appropriate configuration based on the environment variable.
    """
    env = os.environ.get("FLASK_ENV", "development").lower()
    if env == "production":
        return ProductionConfig()
    elif env == "testing":
        return TestingConfig()
    else:
        return DevelopmentConfig()
