import logging
import os

from flask import Flask, render_template

from config import get_config


def setup_logging(app):
    """
    Set up logging for the application.
    """
    log_file = app.config.get("LOG_FILE")
    if log_file:
        log_dir = os.path.dirname(log_file)
        os.makedirs(log_dir, exist_ok=True)

    logging.basicConfig(
        level=app.config["LOG_LEVEL"],
        format=app.config["LOG_FORMAT"],
        filename=log_file,
    )
    logger = logging.getLogger(__name__)

    app.logger.handlers = []
    app.logger.propagate = False
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(app.config["LOG_LEVEL"])

    return logger


def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)
    config = get_config()
    app.config.from_object(config)

    logger = setup_logging(app)
    app.config["TEMPLATES_AUTO_RELOAD"] = app.config.get("TEMPLATES_AUTO_RELOAD", False)

    # Avoid circular imports
    from .routes import main_bp

    app.register_blueprint(main_bp)

    @app.errorhandler(404)
    def not_found_error(error):
        """
        Handle 404 Not Found errors.
        """
        app.logger.error("404 error occurred")
        return render_template("404.html", config=app.config), 404

    @app.errorhandler(500)
    def internal_error(error):
        """
        Handle 500 Internal Server errors.
        """
        app.logger.error("500 error occurred", exc_info=True)
        return render_template("500.html", config=app.config), 500

    logger.info(f"Application created with {config.__class__.__name__} configuration")
    return app
