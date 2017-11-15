from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db

from app.mod_bloodtypes.models import Bloodtype

mod_bloodtypes = Blueprint('inventory', __name__, url_prefix='/inventory')

# @mod_bloodtypes.route('/', methods=['GET', 'POST'])

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
#     def remove_quantity(self, id, milliliters_to_subtract):
#         pass
#         # remove quantity of milliliters in the database and return message of success of fault
#