from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class User(Base, UserMixin):
    __tablename__ = 'users'
    username = db.Column('username', db.String(30), nullable=False, unique=True)
    password = db.Column('password', db.String(128), nullable=False)
    privileges_level = db.Column('privileges_level', db.Integer, nullable=False)
    soft_deleted = db.Column('soft_deleted', db.TIMESTAMP(timezone=False), nullable=True)

    def __init__(self, username, password, privileges_level):
        self.username = username
        self.password = password
        self.privileges_level = privileges_level

    def __repr__(self):
        return '<Username: {}>'.format(self.username)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@property
def password(self):
    """
    Prevent pasword from being accessed
    """
    raise AttributeError('password is not a readable attribute.')


@password.setter
def password(self, password):
    """
    Set password to a hashed password
    """
    self.password_hash = generate_password_hash(password)


def verify_password(self, password):
    """
    Check if hashed password matches actual password
    """
    return check_password_hash(self.password_hash, password)


@property
def is_admin(self):
    if self.privileges_level > 50:
        return True
    else:
        return False