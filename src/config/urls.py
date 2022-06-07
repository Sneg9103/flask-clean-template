# -*- coding: utf-8 -*-
from private.errors import error_bp as errors
from private.main import bp as main
from private.auth import bp as auth
from private.api import bp as api

urls = {
    'errors': errors,
    'main': main,
    'auth': auth,
    'api': api
}
