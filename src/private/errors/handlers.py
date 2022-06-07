# -*- coding: utf-8 -*-
from flask import render_template
from flask_babel import lazy_gettext as _l, gettext as _

from ..models import db

from . import error_bp


@error_bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    data = {
        'message': _l('<p>An unexpected error has occurred. The administrator has been notified.</p> '
                      '<p>Sorry for the inconvenience!</p>'),
        'title': {'error': '500'}
    }

    return render_template('errors/500.html', data=data), 500


@error_bp.app_errorhandler(400)
def handle_bad_request(error):
    data = {
        'message': _l('Wrong file format!'),
        'title': {'error': '400'}
    }

    return render_template('errors/400.html', data=data), 400


@error_bp.app_errorhandler(404)
def not_found_error(error):
    data = {
        'message': _l('The page not found!'),
        'title': {'error': '404'}
    }

    return render_template('errors/404.html', data=data), 404


@error_bp.app_errorhandler(413)
def handle_bad_request(error):
    data = {
        'message': _l('Too large file!'),
        'title': {'error': '413'}
    }

    return render_template('errors/413.html', data=data), 413
