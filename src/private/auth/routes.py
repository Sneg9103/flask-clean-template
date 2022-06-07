# -*- coding: utf-8 -*-
import random

from flask import (render_template, redirect, url_for, flash, request)
from flask_login import (current_user, login_required, logout_user, login_user)
from flask_babel import lazy_gettext as _l
from werkzeug.urls import url_parse

from private.decorators import unauthorized

from .. import db
from ..models import (User, Right)

from . import bp
from .forms import (SigninForm, SignupForm)


@bp.before_request
def before_request():
    global data
    data = {
        'counter_cache': random.randrange(0, 10**10),
        'endpoint': request.url_rule.endpoint,
        'title': '',
    }


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/signin', methods=['GET', 'POST'])
@unauthorized
def signin():
    global data
    sign_in = SigninForm()

    if sign_in.validate_on_submit():
        user = User.query.filter_by(email=sign_in.email.data).first()
        login_user(user, remember=True)
        if current_user.is_authenticated:
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('main.index')
            flash(_l(f'Welcome! You\'re authorized'), 'success')

            return redirect(next_page)

        return redirect(url_for('auth.login'))

    # Compound all data for view
    data = dict(data, **{
        'sign_in': sign_in,
    })

    return render_template("auth/signin.html", data=data)


@bp.route('/signup', methods=['GET', 'POST'])
@unauthorized
def signup():
    global data
    sign_up = SignupForm()

    

    if sign_up.validate_on_submit():
        # Add a user to the database
        user = User(email=sign_up.email.data, name=sign_up.name.data)
        developer = Right.query.filter_by(code=999).first()
        user.rights.append(developer)
        user.set_password(sign_up.password.data)
        db.session.add(user)
        db.session.commit()

        # Auto authorization user
        new_user = User.query.filter_by(email=sign_up.email.data).first()
        login_user(new_user, remember=True)
        if current_user.is_authenticated:
            # Use custom next page or default
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('main.index')
            flash(_l('Congratulations, you\'ve passed!'), 'success')

            return redirect(next_page)

        return redirect(url_for('auth.signin'))

    # Compound all data for view
    data = dict(data, **{
        'sign_up': sign_up,
    })

    return render_template("auth/signup.html", data=data)


@bp.route('/logout', methods=['GET'])
@login_required
def logout():
    flash(_l(f'You are logged out'), 'input_success')
    logout_user()

    return redirect(url_for('main.index'))
