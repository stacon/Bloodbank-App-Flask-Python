from app import db

class Base(db.Model):

    __abstract__            = True

    id                      = db.Column(db.Integer, primary_key=True)
    date_created            = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified           = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Transaction(Base):
    __tablename__ = 'transactions'
    donor_id                = db.Column('donor_id', db.Integer, db.ForeignKey('donors.id'), nullable=False)
    transaction_type        = db.Column('transaction_type', db.CHAR(1), nullable=False)
    bloodtype_id            = db.Column('bloodtype_id', db.Integer, db.ForeignKey('bloodtypes.id'), nullable=True)
    soft_deleted            = db.Column('soft_deleted', db.TIMESTAMP(timezone=False), nullable=True)

    def __init__(self, donor_id, transaction_type, bloodtype_id):
        self.donor_id = donor_id
        self.transaction_type = transaction_type
        self.bloodtype_id = bloodtype_id

    def __repr__(self):
        return '<ID: %r>' % (self.id)
