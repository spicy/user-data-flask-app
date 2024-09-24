from flask import Flask, render_template
from config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.config['TEMPLATES_AUTO_RELOAD'] = app.config.get('TEMPLATES_AUTO_RELOAD', True)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html', app_name=app.config['APPLICATION_NAME']), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html', app_name=app.config['APPLICATION_NAME']), 500

    return app