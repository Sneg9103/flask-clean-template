# -*- coding: utf-8 -*-
from flask import Blueprint

error_bp = Blueprint('errors', __name__)

from . import handlers