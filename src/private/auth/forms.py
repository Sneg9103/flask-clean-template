# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l
from wtforms import (StringField, PasswordField, BooleanField, SubmitField)
from wtforms.validators import (ValidationError, DataRequired, Length, Email, EqualTo)

from private.models import User


class SignupForm(FlaskForm):
    """ Registration form """

    attributes = {
        'email': {'placeholder': _l('Type email...'), 'autocomplete': 'on'},
        'name': {'placeholder': _l('Type name...'), 'autocomplete': 'off'},
        'password': {'placeholder': _l('Type password...'), 'autocomplete': 'new-password'},
        'repeat_password': {'placeholder': _l('Repeat password...'), 'autocomplete': 'new-password'},
    }

    email = StringField(
        _l('Email'),
        validators=[
            DataRequired(),
            Email(),
            Length(min=1, max=128)
        ],
        render_kw=attributes['email']
    )
    password = PasswordField(
        _l('Password'),
        validators=[
            DataRequired(),
            Length(min=4, max=128)
        ],
        render_kw=attributes['password']
    )
    repeat_password = PasswordField(
        _l('Repeat password'),
        validators=[
            DataRequired(),
            EqualTo('password'),
            Length(min=4, max=128)
        ],
        render_kw=attributes['repeat_password']
    )
    submit = SubmitField(_l('Sign up'))

    @staticmethod
    def validate_email(form, field):
        user = User.query.filter_by(email=field.data).first()
        if user is not None:
            raise ValidationError(_l('This email is already taken. Please choose another one.'))


class SigninForm(FlaskForm):
    """ Authorization form """

    attributes = {
        'email': {'placeholder': _l('Type email...'), 'autocomplete': 'on', 'autofocus': 'on'},
        'password': {'placeholder': _l('Type password...'), 'autocomplete': 'new-password'},
    }

    email = StringField(
        _l('Email'),
        validators=[
            DataRequired(),
            Email(),
            Length(min=1, max=128)
        ],
        render_kw=attributes['email']
    )
    password = PasswordField(
        _l('Password'),
        validators=[
            DataRequired(),
            Length(min=4, max=128)
        ],
        render_kw=attributes['password']
    )
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign in'))

    @staticmethod
    def validate_email(form, field):
        user = User.query.filter_by(email=field.data).first()
        if user is None or not user.check_password(form.password.data):
            raise ValidationError(_l('Email or password is incorrect.'))


class PasswordRecoveryForm(FlaskForm):
    """ Password recovery form """

    attributes = {
        'password': {'placeholder': _l('Type new password...'), 'autocomplete': 'new-password'},
        'repeat_password': {'placeholder': _l('Repeat password...'), 'autocomplete': 'new-password'},
    }

    password = PasswordField(
        _l('Password'),
        validators=[
            DataRequired(),
            Length(min=4, max=128)
        ],
        render_kw=attributes['password']
    )
    repeat_password = PasswordField(
        _l('Repeat password'),
        validators=[
            DataRequired(),
            EqualTo('password'),
            Length(min=4, max=20)
        ],
        render_kw=attributes['repeat_password']
    )
    submit = SubmitField(_l('Update password'))
