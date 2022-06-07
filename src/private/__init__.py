# -*- coding: utf-8 -*-
import os
import logging
from logging.handlers import (SMTPHandler, RotatingFileHandler)

from flask import Flask

from config.settings import DevelopmentConfig
from config.instances import (db, mail, moment, migrate, login, limiter, babel)


def create_app(config=None):
    """Create the WSGI app using the factory pattern

    Args:
        :param config: override DevelopmentConfig modes.
    Returns:
        :return: Flask app
    """

    app = Flask(__name__, instance_path=f'/files',
                static_folder=f'../public/static',
                template_folder=f'../public/templates')

    if config:
        app.config.from_object(config)
    else:
        app.config.from_object(DevelopmentConfig)

    register_logging(app)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    """Register all app instances/extensions

    Args:
        :param app: Flask application instance
    Returns:
        :return: None
    """

    db.init_app(app)                # Inject SQLAlchemy into the app
    mail.init_app(app)              # Inject Mail into the app
    moment.init_app(app)            # Inject Mail into the app
    migrate.init_app(app, db)       # Inject Migrate into the app
    babel.init_app(app)             # Inject translation lib into the app
    limiter.init_app(app)           # Inject Limiter for requests into the app
    login.init_app(app)             # Inject Login Manager into the app


def register_blueprints(app):
    """Register all app blueprints: `errors`, `main` etc.

    Args:
        :param app: Flask application instance
    Returns:
        :return: None
    """

    with app.app_context():
        import sys
        import os 
        sys.path.append(os.path.abspath(os.path.join(__file__, '../')))
        from config.urls import urls
        rb = app.register_blueprint
        [rb(blueprint) for blueprint in urls.values()]


def register_logging(app):
    """Logging and mail notification logic

    Args:
        :param app: Flask application instance
    Returns:
        :return: None
    """

    if not app.debug:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'], subject=f'{__name__} Failure',
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler(f'logs/{__name__}.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info({__name__})


__version__ = "1.0.0"
