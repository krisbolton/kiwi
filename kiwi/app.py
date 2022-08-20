from flask import Flask, render_template

from kiwi.blueprints.page import page
from kiwi.extensions import debug_toolbar


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    error_templates(app)
    app.register_blueprint(page)

    return app


def extensions(app):
	"""
	Register extensions.
	
	:param app: Flask application instance.
	:return: None
	"""
	debug_toolbar.init_app(app)
	
	return None


def error_templates(app):
    """
    Register error pages

    :param app: Flask app instance
    :return: None
    """

    def render_status(status):
        """
         Render a template for specific status

         :param status: Status
         :type status: str
         :return: None
         """

        code = getattr(status, 'code', 500)
        return render_template('errors/{0}.html'.format(code)), code

    for error in [404, 500]:
        app.errorhandler(error)(render_status)

    return None
