# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix=f'/auth')

from ..auth import routes
