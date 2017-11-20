from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask_login import user_logged_in
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.mod_auth.models import User
from app.mod_donors.models import Donor
from app.mod_bloodtypes.models import Bloodtype
from flask_login import login_required

mod_main = Blueprint('main', __name__)

@mod_main.route('/')
@login_required
def index():
    bloodTypes = Bloodtype.query.order_by(Bloodtype.name).all()
    recent_donors = Donor.query.order_by(Donor.date_created.desc()).limit(10)
    return render_template('main/dashboard.html', bloodTypes=bloodTypes, recent_donors=recent_donors, title="Dashboard")

def notAllowed():
    return render_template('master/406.html', title='Error 406')