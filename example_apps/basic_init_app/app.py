# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_user import SQLAlchemyAdapter

from ext import db, user_manager
from models import User

def create_app():
    app = Flask(__name__)
    app.config['USER_APP_NAME'] = 'BASIC INIT APP'
    app.config['USER_ENABLE_EMAIL'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basic_init_app.sqlite'
    app.config['SECRET_KEY'] = 'NOT SO SECRET'
    app.config['DEBUG'] = True

    db.init_app(app)
    db_adapter = SQLAlchemyAdapter(db, User)
    user_manager.init_app(app, db_adapter)

    @app.route('/create/')
    def create():
        db.create_all()
        return 'DB TABLES CREATED'

    @app.route('/drop/')
    def drop():
        db.drop_all()
        return 'DB TABLES DROPPED'

    @app.route('/add/')
    def add():
        user = User(email='test@test.com', password=user_manager.hash_password('testm123'))
        db.session.add(user)
        db.session.commit()
        return 'USER ADDED'

    @app.route('/users/')
    def users():
        users = User.query.all()
        print(users)
        return 'USERS?'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
