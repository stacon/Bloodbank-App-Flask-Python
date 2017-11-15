from app import db

class Base(db.Model):

    __abstract__            = True

    id                      = db.Column(db.Integer, primary_key=True)
    date_created            = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified           = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class User(Base):

    __tablename__           = 'users'
    username                = db.Column('username', db.String(15), nullable=False, unique=True)
    password                = db.Column('password', db.String(80), nullable=False)
    privileges_level        = db.Column('privileges_level', db.Integer, nullable=False)
    soft_deleted            = db.Column('soft_deleted', db.TIMESTAMP(timezone=False), nullable=True)

    def __init__(self, username, password, privileges_level):
        self.username = username
        self.password = password
        self.privileges_level = privileges_level

    def __repr__(self):
        return '<Username %r>' % (self.username)