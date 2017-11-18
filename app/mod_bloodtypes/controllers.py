from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
import re
from app.mod_bloodtypes.models import Bloodtype
from flask_login import login_required
from app import db

mod_bloodtypes = Blueprint('inventory', __name__, url_prefix='/inventory')

@mod_bloodtypes.route('/')
@login_required
def index():
    bloodTypes = Bloodtype.query.order_by(Bloodtype.name).all()
    return render_template('bloodtypes/index.html', bloodTypes = bloodTypes)

@mod_bloodtypes.route('/<name>')
@login_required
def view(name): # name should be passed as an argument
    if valid(name):
        bloodtype = Bloodtype.query.filter_by(name=name).first()
        return render_template('bloodtypes/view.html', bloodtype=bloodtype)
    else:
        return render_template('master/406.html'), 406

# Validating Input to avoid injection
def valid(name):
    return re.match(r'^[AaBb0]{1,2}[+-]$', name)


#
#     def add_quantity(self, id, milliliters_to_add):
#         pass
#         # add quantity of milliliters in the database and return message of success of fault
#
#     def subtract_quantity(self, id, milliliters_to_subtract):
#         pass
#         # subtract quantity of milliliters in the database and return message of success of fault
#