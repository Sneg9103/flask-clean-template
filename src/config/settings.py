
# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

_basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(_basedir, '.env'))


class Main:
    """Main settings"""

    FLASK_APP = os.environ.get('FLASK_APP') or 'manage.py'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class Captcha:
    """Captcha settings"""

    # RECAPTCHA_USE_SSL = False
    # RECAPTCHA_PUBLIC_KEY = 'go to recaptcha and get public key'
    # RECAPTCHA_PRIVATE_KEY = 'go to recaptcha and get private key'
    # RECAPTCHA_OPTIONS = {'theme': 'white'}


class Payment:
    """Payment settings"""


class Mail:
    """Mail settings"""

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = int(os.environ.get("MAIL_USE_TLS"))
    MAIL_USE_SSL = int(os.environ.get("MAIL_USE_SSL"))
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SUPPRESS_SEND = int(os.environ.get("MAIL_SUPPRESS_SEND"))
    ADMINS = [os.environ.get("ADMIN")] or ['email']


class Database:
    """Database settings"""

    db_credentials = {
        'user': os.environ.get("POSTGRES_USER"),
        'password': os.environ.get("POSTGRES_PASSWORD"),
        'host': os.environ.get("POSTGRES_HOST"),
        'port': os.environ.get("POSTGRES_PORT"),
        'db': os.environ.get("POSTGRES_DB")
    }
    SQLALCHEMY_DATABASE_URI = f'postgresql://' \
                              f'{db_credentials["user"]}' \
                              f':{db_credentials["password"]}' \
                              f'@{db_credentials["host"]}' \
                              f':{db_credentials["port"]}' \
                              f'/{db_credentials["db"]}' \
                              f'?client_encoding=utf8'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Search:
    """Database settings"""

    ELASTICSEARCH_URL = os.environ.get('DEV_ELASTICSEARCH_URL')


class Page:
    """Pages settings"""

    NOTIFICATION_PER_PAGE = 10
    ACCOUNTS_PER_PAGE = 12
    MAX_PHOTOS = 5 # etc.


class File:
    """Files settings

    Compose allowed file extensions;
    Server side size limit for file upload;
    Default path for file upload.
    """

    #: This contains document-like files.
    DOCUMENTS = list('.pdf'.split())
    #: This contains basic image types that are viewable from most browsers.
    IMAGES = list('.jpg .jpe .jpeg .png'.split())
    #: Add every one of the types to main collection.
    ALLOWED_EXTENSIONS = DOCUMENTS + IMAGES
    #: Size limit for uploaded files.
    MAX_CONTENT_LENGTH = 1024 * 1024 * 40
    #: Size limit for uploaded file.
    MAX_LENGTH_BY_FILE = 1024 * 1024 * 1
    #: Storage path for files.
    UPLOAD_PATH = os.path.join(_basedir, os.path.join('src', 'files'))
    FILES_PER_REQUEST = 10

class Languages:
    """Languages settings"""

    LANGUAGES = ['en']


class Collection(Main, Captcha, Database, Search, Payment, Mail, Page, File, Languages):
    """Collection Flask config variables."""
    pass


class ProductionConfig(Collection):
    """Main config"""

    ENV = 'production'
    DEBUG = False
    TESTING = False  # enable error catching during request handling.
    SECRET_KEY = os.environ.get('PRODUCTION_SECRET_KEY') or 'abs_#&*)_secret-key'


class DevelopmentConfig(Collection):
    """Main config"""

    ENV = 'development'
    DEBUG = True
    TESTING = True  # disable error catching during request handling.
    SECRET_KEY = os.environ.get('DEVELOPMENT_SECRET_KEY') or '!Dev-abs_#&*)_secret-key'
