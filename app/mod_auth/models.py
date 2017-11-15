from app import db

class Base(db.Model):

    __abstract__            = True

    id                      = db.Column(db.Integer, primary_key=True)
    date_created            = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified           = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class User(Base):

    __tablename__           = 'users'
    id                      = db.Column('id', db.Integer, primary_key=True)
    username                = db.Column('username', db.String(15), nullable=False, unique=True)
    password                = db.Column('password', db.String(80), nullable=False)
    priviledges_level       = db.Column('priviledges_level', db.Integer, nullable=False)
    soft_deleted            = db.Column('soft_deleted', db.TIMESTAMP(timezone=False), nullable=True)

    def __init__(self, username, password, priviledges_level):
        self.username = username
        self.password = password
        self.priviledges_level = priviledges_level

    def __repr__(self):
        return '<Username %r>' % (self.username)

        # class Bloodtype(db.Model):
#     __tablename__           = 'bloodtypes'
#     id                      = db.Column('id', db.Integer, primary_key=True)
#     name                    = db.Column('name', db.String(3), nullable=False)
#     milliliters_available   = db.Column('milliliters_available',db.Integer, nullable=False)
#     transactions            = db.relationship('Transaction', backref='bloodtype', lazy='dynamic')
#     donors                  = db.relationship('Donors', backref='bloodtype', lazy='dynamic')
#
# class Donor(db.Model):
#     __tablename__           = 'donors'
#     id                      = db.Column('id', db.Integer, primary_key=True)
#     first_name              = db.Column('first_name', db.String(30), nullable=False )
#     last_name               = db.Column('last_name', db.String(30), nullable=False)
#     gender                  = db.Column('gender', db.String(3), nullable=False)
#     dob                     = db.Column('dob', db.Date, nullable=False)
#     bloodtype_id            = db.Column('bloodtype_id', db.Integer, db.ForeignKey('bloodtypes.id'), nullable=True)
#     address                 = db.Column('address', db.String(20), nullable=False)
#     city                    = db.Column('city', db.String(20), nullable=False)
#     state                   = db.Column('state', db.String(20), nullable=False)
#     zip_code                = db.Column('zip_code', db.String(7), nullable=False)
#     contact_number          = db.Column('contact_number', db.String(20), nullable=False)
#     milliliters_deposited   = db.Column('milliliters_deposited', db.Integer, nullable=True)
#     milliliters_withdrawn   = db.Column('milliliters_withdrawn', db.Integer, nullable=True)
#     soft_deleted            = db.Column('soft_deleted', db.TIMESTAMP(timezone=False), nullable=True)
#     transactions            = db.relationship('Transaction', backref='donor', lazy='dynamic')
#
# class Transaction(db.Model):
#     __tablename__ = 'transactions'
#     id                      = db.Column('id', db.Integer, primary_key=True)
#     donor_id                = db.Column('donor_id', db.Integer, db.ForeignKey('donors.id'), nullable=False)
#     transaction_type        = db.Column('transaction_type', db.CHAR(1), nullable=False)
#     bloodtype_id            = db.Column('bloodtype_id', db.Integer, db.ForeignKey('bloodtypes.id'), nullable=True)
#     created_at              = db.Column('created_at', db.TIMESTAMP(timezone=False), nullable=False)
#     soft_deleted            = db.Column('soft_deleted', db.TIMESTAMP(timezone=False), nullable=True)