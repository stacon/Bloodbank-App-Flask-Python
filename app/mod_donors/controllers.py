from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.mod_donors.models import Donor

mod_donors = Blueprint('donors', __name__, url_prefix='/donors')

# @mod_donors.route('/login/', methods=['GET', 'POST'])

# class DonorsController:
#
#     def index(self):
#         pass
#         # return a view of donors
#
#     def view(self,id):
#         pass
#         # return a view with the information of a particular donor along his blood transactions
#
#     def register(self):
#         pass
#         # return a view to register a donor
#
#     def create(self, data):
#         pass
#         # attempt to create a donor in the database and return success or error
#
#     def edit(self, id):
#         pass
#         # return a view to edit donor's data
#
#     def update(self, data):
#         pass
#         # attempt to update the donor's data based on his id, returning error or success message
#
#     def donate(self, id, milliliters, bloodtype_id):
#         pass
#         # attemp a blood deposit transaction for the given donor
#
#     def withdraw(self, id, milliliters, bloodtype_id):
#         pass
#         # attemp a blood withdraw transaction for the given donor
#
#     def transaction_history(self, id, transaction_type = False):
#         pass
#         # return a list with donors history of transactions
#         # if transaction type is provided use it as a filter
