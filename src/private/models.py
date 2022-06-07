# -*- coding: utf-8 -*-
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import (generate_password_hash, check_password_hash)

from config.instances import (db, login)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), index=True, unique=True)

    rights = db.relationship('Right', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User: {self.email}>'

class Right(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, index=True, default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Right: {self.user.email}>'
