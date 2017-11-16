from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
import re
from app.mod_bloodtypes.models import Bloodtype
from app import db

mod_bloodtypes = Blueprint('inventory', __name__, url_prefix='/inventory')

@mod_bloodtypes.route('/')
def index():
    return render_template('bloodtypes/index.html')

@mod_bloodtypes.route('/<name>')
def view(name): # name should be passed as an argument
    if valid(name):
        bloodtype = Bloodtype.query.filter_by(name=name).first()
        return render_template('bloodtypes/view.html', bloodtype=bloodtype)
    else:
        return render_template('master/406.html'), 406

def valid(name):
    return re.match(r'^[AaBb0][+-]$', name)

# class BloodtypesController:
#
#     def show(self):
#         pass
#         # return a view with data of bloodtypes
#
#     def view(self, id):
#         pass
#         # return a view for a particular blood type along with transaction data
#
#     def add_quantity(self, id, milliliters_to_add):
#         pass
#         # add quantity of milliliters in the database and return message of success of fault
#
#     def subtract_quantity(self, id, milliliters_to_subtract):
#         pass
#         # subtract quantity of milliliters in the database and return message of success of fault
#