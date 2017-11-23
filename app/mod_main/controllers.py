from flask import Blueprint, render_template
from app.mod_transactions.models import Transaction
from app.mod_donors.models import Donor
from app.mod_bloodtypes.models import Bloodtype
from flask_login import login_required

mod_main = Blueprint('main', __name__)

@mod_main.route('/')
@login_required
def index():
    bloodTypes = Bloodtype.query.order_by(Bloodtype.name).all()
    recent_transactions = Transaction.query.order_by(Transaction.date_created.desc()).limit(10).all()
    recent_donors = Donor.query.order_by(Donor.date_created.desc()).limit(10)
    return render_template(
        'main/dashboard.html',
        bloodTypes=bloodTypes,
        recent_donors=recent_donors,
        recent_transactions=recent_transactions,
        title="Dashboard"
    )

def notAllowed():
    return render_template('master/406.html', title='Error 406')