from app import db, login_manager
from flask_login import UserMixin


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class User(Base, UserMixin):
    __tablename__ = 'users'
    username = db.Column('username', db.String(30), nullable=False, unique=True)
    password = db.Column('password', db.String(80), nullable=False)
    privileges_level = db.Column('privileges_level', db.Integer, nullable=False)
    soft_deleted = db.Column('soft_deleted', db.TIMESTAMP(timezone=False), nullable=True)

    def __init__(self, username, password, privileges_level):
        self.username = username
        self.password = password
        self.privileges_level = privileges_level

    def __repr__(self):
        return '<Username %r>' % (self.username)

@login_manager.user_loader
def load_user(user_id):
    return  User.query.get(int(user_id))
