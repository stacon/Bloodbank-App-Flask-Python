from flask import Blueprint, render_template, redirect, url_for
import re
from app.mod_bloodtypes.models import Bloodtype
from app.mod_transactions.models import Transaction
from flask_login import login_required

mod_bloodtypes = Blueprint('inventory', __name__, url_prefix='/inventory')


@mod_bloodtypes.route('/')
@login_required
def index():
    bloodTypes = Bloodtype.query.order_by(Bloodtype.name).all()
    recent_donations = Transaction.query.filter_by(type='D').order_by(Transaction.date_created.desc()).limit(10).all()
    recent_withdrawals = Transaction.query.filter_by(type='W').order_by(Transaction.date_created.desc()).limit(10).all()
    return render_template(
        'bloodtypes/index.html',
        recent_donations=recent_donations,
        recent_withdrawals=recent_withdrawals,
        bloodTypes=bloodTypes,
        title='Inventory'
    )


@mod_bloodtypes.route('/<name>')
@login_required
def view(name):
    if valid(name):
        bloodtype = Bloodtype.query.filter_by(name=name).first()
        recent_donations = Transaction.query.filter_by(bloodtype_id=bloodtype.id, type='D').order_by(
            Transaction.date_created.desc()).limit(10).all()
        recent_withdrawals = Transaction.query.filter_by(bloodtype_id=bloodtype.id, type='W').order_by(
            Transaction.date_created.desc()).limit(10).all()
        return render_template(
            'bloodtypes/view.html',
            recent_donations=recent_donations,
            recent_withdrawals=recent_withdrawals,
            bloodtype=bloodtype,
            title=u'{} info'.format(bloodtype.name))
    return redirect(url_for('main.notAllowed'))


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
