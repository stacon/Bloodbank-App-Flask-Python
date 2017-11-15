from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.mod_transactions.models import Transaction

mod_transactions = Blueprint('transactions', __name__, url_prefix='/transactions')

# @mod_auth.route('/login/', methods=['GET', 'POST'])
# class TransactionsController:
#
#     def record(self, donor_id, transaction_type, milliliters, bloodtype_id):
#         pass
#         # record a blood transaction and update users blood view and bloodtypes inventory
#
#     def history(self, bloodtype_id=False):
#         pass
#         # return a transaction history (maybe paginated)
#         # if bloodtype_id is passed as argument fetch transactions of this particular bloodtype database
#
#     def delete(self, id):
#         pass
#         # soft delete a transaction by rolling the blood to user AND inventory bloodtypes database