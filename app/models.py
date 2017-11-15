from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/o_bloodbank'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__           = 'users'
    id                      = db.Column('id', db.Integer, primary_key=True)
    username                = db.Column('username', db.String(15), nullable=False)
    password                = db.Column('password', db.String(80), nullable=False)
    priviledges_level       = db.Column('priviledges_level', db.Integer, nullable=False)
    soft_deleted            = db.Column('soft_deleted', db.TIMESTAMP(timezone=False), nullable=True)

class Bloodtype(db.Model):
    __tablename__           = 'bloodtypes'
    id                      = db.Column('id', db.Integer, primary_key=True)
    name                    = db.Column('name', db.String(3), nullable=False)
    milliliters_available   = db.Column('milliliters_available',db.Integer, nullable=False)

class Donor(db.Model):
    __tablename__           = 'donors'
    id                      = db.Column('id', db.Integer, primary_key=True)
    first_name              = db.Column('first_name', db.String(30), nullable=False )
    last_name               = db.Column('last_name', db.String(30), nullable=False)
    gender                  = db.Column('gender', db.String(3), nullable=False)
    dob                     = db.Column('dob', db.Date, nullable=False)
    bloodtype_id            = db.Column('bloodtype_id', db.Integer, nullable=True)
    address                 = db.Column('address', db.String(20), nullable=False)
    city                    = db.Column('city', db.String(20), nullable=False)
    state                   = db.Column('state', db.String(20), nullable=False)
    zip_code                = db.Column('zip_code', db.String(7), nullable=False)
    contact_number          = db.Column('contact_number', db.String(20), nullable=False)
    milliliters_deposited   = db.Column('milliliters_deposited', db.Integer, nullable=True)
    milliliters_withdrawn   = db.Column('milliliters_withdrawn', db.Integer, nullable=True)
    soft_deleted            = db.Column('soft_deleted', db.TIMESTAMP(timezone=False), nullable=True)

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id                      = db.Column('id', db.Integer, primary_key=True)
    donor_id                = db.Column('donor_id', db.Integer, nullable=False)
    transaction_type        = db.Column('transaction_type', db.CHAR(1), nullable=False)
    bloodtype_id            = db.Column('bloodtype_id', db.Integer, nullable=True)
    created_at              = db.Column('created_at', db.TIMESTAMP(timezone=False), nullable=False)
    soft_deleted            = db.Column('soft_deleted', db.TIMESTAMP(timezone=False), nullable=True)