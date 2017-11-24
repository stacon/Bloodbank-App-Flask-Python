from app.mod_donors.models import Donor
from datetime import date

def create():
    tDonor = Donor('John', 'Smith', 'M', date(2000,10,24),1 , 'Ioniou 5', 'Thessalonki', 'Thessalonikis', 11521, '2109216977')

    for key, value in tDonor.__dict__.items():
        if not key.startswith('__') and not callable(key):
            print(key, ' : (', type(value), ') : ', value)
