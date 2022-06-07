# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_moment import Moment
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_babel import Babel, lazy_gettext as _l
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()                               # Invoke SQLAlchemy
mail = Mail()                                   # Invoke Mail
moment = Moment()                               # Invoke Moment
migrate = Migrate()                             # Invoke Migrate
babel = Babel()                                 # Invoke Babel
limiter = Limiter(key_func=get_remote_address)  # Invoke Limiter
login = LoginManager()                          # Invoke Login Manager
login.login_view = 'auth.signin'                # Presetting Login Manager
login.login_message = _l('Please log in to access this page.')  # Presetting flash message of Login Manager
