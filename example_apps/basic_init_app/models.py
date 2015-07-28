# -*- coding: utf-8 -*-
from datetime import datetime

from flask_user import UserMixin

from ext import db

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), default=None)
    password = db.Column(db.String(255), nullable=False, default='')
    email = db.Column(db.String(255), nullable=True, unique=True)
    confirmed_at = db.Column(db.DateTime, default=datetime.utcnow())
    reset_password_token = db.Column(db.String(100), nullable=False, server_default='')
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')
