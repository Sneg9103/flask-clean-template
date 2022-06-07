# -*- coding: utf-8 -*-
import random

from flask import (request, current_app, render_template)
from flask_login import (current_user, login_required)

from .. import db

from . import bp

global data


@bp.before_request
def before_request():
    global data
    data = {
        'counter_cache': random.randrange(0, 10**10),
        'endpoint': request.url_rule.endpoint,
        'title': '',
    }

@bp.get('/')
def index():
    global data

    return render_template("main/index.html", data=data)
