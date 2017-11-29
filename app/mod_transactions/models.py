from app import db
from app.mod_bloodtypes.models import Bloodtype

class Base(db.Model):

    __abstract__            = True

    id                      = db.Column(db.Integer, primary_key=True)
    date_created            = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified           = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Transaction(Base):
    __tablename__           = 'transactions'
    donor_id                = db.Column('donor_id', db.Integer, db.ForeignKey('donors.id'), nullable=False)
    type                    = db.Column('transaction_type', db.CHAR(1), nullable=False)
    bloodtype_id            = db.Column('bloodtype_id', db.Integer, db.ForeignKey('bloodtypes.id'), nullable=True)
    milliliters             = db.Column('milliliters', db.Integer, nullable=False)
    soft_deleted            = db.Column('soft_deleted', db.TIMESTAMP(timezone=False), nullable=True)

    def __init__(self, donor_id, type, bloodtype_id, milliliters, donor):
        self.donor_id = donor_id
        self.type = type
        self.bloodtype_id = bloodtype_id
        self.milliliters = milliliters
        self.donor = donor

        # Update inventory
        if type == 'D':
            bloodtype = Bloodtype.query.filter_by(id=bloodtype_id).first()
            bloodtype.increase(milliliters)
            donor.donate(milliliters)
        elif type == 'W':
            bloodtype = Bloodtype.query.filter_by(id=bloodtype_id).first()
            bloodtype.decrease(milliliters)
            donor.withdraw(milliliters)

    def __repr__(self):
        return '<ID: %r>' % (self.id)
