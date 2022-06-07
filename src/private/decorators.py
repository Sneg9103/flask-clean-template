# -*- coding: utf-8 -*-

from functools import wraps

from flask import (abort, redirect, url_for, flash)
from flask_login import current_user
from flask_babel import lazy_gettext as _l


def permit(right_code, code_error=404):
    """Check if a user has permission to view the page.

    Args:
        :param right_code: a specific right access;
        :param code_error: default 404 error.
    Returns:
        :return: If the permit isn't allowed return an error, otherwise a callback Function.
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # throw an error if a user has no right permit.
            if right_code not in [right.code for right, in current_user.rights]:
                abort(code_error)

            return f(*args, **kwargs)

        return decorated_function

    return decorator


def unauthorized(f):
    """Allow see a view page only for unauthorized users.

    Returns:
        :return: Redirect statement if a user is authorized, otherwise a callback Function.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Run through a list of permit codes
        if current_user.is_authenticated:
            flash(_l(f'You were authorized'), 'input_success')
            return redirect(url_for('main.index'))

        return f(*args, **kwargs)

    return decorated_function
