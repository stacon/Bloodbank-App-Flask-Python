from app import db
from datetime import date
from app.mod_transactions.models import Transaction
from app.mod_bloodtypes.models import Bloodtype

class Base(db.Model):

    __abstract__            = True

    id                      = db.Column(db.Integer, primary_key=True)
    date_created            = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified           = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Donor(Base):
    __tablename__           = 'donors'
    first_name              = db.Column('first_name', db.String(30), nullable=False )
    last_name               = db.Column('last_name', db.String(30), nullable=False)
    gender                  = db.Column('gender', db.String(3), nullable=False)
    dob                     = db.Column('dob', db.Date, nullable=False)
    bloodtype_id            = db.Column('bloodtype_id', db.Integer, db.ForeignKey('bloodtypes.id'), nullable=True)
    address                 = db.Column('address', db.String(20), nullable=False)
    city                    = db.Column('city', db.String(20), nullable=False)
    state                   = db.Column('state', db.String(20), nullable=False)
    zip_code                = db.Column('zip_code', db.String(7), nullable=True)
    contact_number          = db.Column('contact_number', db.String(20), nullable=False)
    milliliters_donated     = db.Column('milliliters_donated', db.Integer, nullable=True)
    milliliters_withdrawn   = db.Column('milliliters_withdrawn', db.Integer, nullable=True)
    soft_deleted            = db.Column('soft_deleted', db.TIMESTAMP(timezone=False), nullable=True)
    transactions            = db.relationship('Transaction', backref='donor', lazy='dynamic')

    def __init__(self, first_name, last_name, gender, dob, bloodtype_id, address, city, state, zip_code, contact_number):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.dob = dob
        self.bloodtype_id = bloodtype_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.contact_number = contact_number

    @property
    def age(self):
        return str(int(((date.today() - self.dob).days) / 365 ))

