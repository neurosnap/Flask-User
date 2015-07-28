# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_user import SQLAlchemyAdapter, UserManager

db = SQLAlchemy()
#db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager()
