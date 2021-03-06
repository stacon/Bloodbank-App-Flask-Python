from app import db

class Base(db.Model):

    __abstract__            = True

    id                      = db.Column(db.Integer, primary_key=True)
    date_created            = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified           = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Bloodtype(Base):
    __tablename__           = 'bloodtypes'
    name                    = db.Column('name', db.String(3), nullable=False, unique=True)
    milliliters_available   = db.Column('milliliters_available',db.Integer, nullable=False)
    transactions            = db.relationship('Transaction', backref='bloodtype', lazy='dynamic')
    donors                  = db.relationship('Donor', backref='bloodtype', lazy='dynamic')

    def __init__(self, name, milliliters_available=0):
        self.name = name
        self.milliliters_available = milliliters_available

    def __repr__(self):
        return str(self.name)

    @property
    def liters(self):
        return str("{0:.2f}".format(self.milliliters_available/1000))

    def increase(self, amount):
        self.milliliters_available += amount
        db.session.commit()

    def decrease(self, amount):
        self.milliliters_available -= amount
        db.session.commit()