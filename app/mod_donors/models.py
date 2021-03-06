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
    insurance_number        = db.Column('insurance_number', db.String(30), nullable=False, unique=True)
    first_name              = db.Column('first_name', db.String(30), nullable=False)
    last_name               = db.Column('last_name', db.String(30), nullable=False)
    gender                  = db.Column('gender', db.String(3), nullable=False)
    dob                     = db.Column('dob', db.Date, nullable=False)
    bloodtype_id            = db.Column('bloodtype_id', db.Integer, db.ForeignKey('bloodtypes.id'), nullable=True)
    address                 = db.Column('address', db.String(20), nullable=False)
    city                    = db.Column('city', db.String(20), nullable=False)
    state                   = db.Column('state', db.String(20), nullable=False)
    zip_code                = db.Column('zip_code', db.String(7), nullable=True)
    contact_number          = db.Column('contact_number', db.String(20), nullable=False)
    milliliters_donated     = db.Column('milliliters_donated', db.Integer, nullable=True, default=0)
    milliliters_withdrawn   = db.Column('milliliters_withdrawn', db.Integer, nullable=True, default=0)
    transactions            = db.relationship('Transaction', backref='donor', lazy='dynamic')

    def __repr__(self):
        return '<First name: {}, Last name: {}>'.format(self.first_name, self.last_name)

    def __init__(self, insurance_number, first_name, last_name, gender, dob, bloodtype_id, address, city, state, zip_code, contact_number):
        self.insurance_number = insurance_number
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


    def donate(self, amount):
        self.milliliters_donated += amount
        db.session.commit()


    def withdraw(self, amount):
        self.milliliters_withdrawn += amount
        db.session.commit()

    @property
    def age(self):
        return str(int((date.today() - self.dob).days / 365))

