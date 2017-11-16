from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask_login import user_logged_in
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.mod_auth.models import User

mod_main = Blueprint('main', __name__)

@mod_main.route('/')
def index():
    return render_template('main/dashboard.html')
   # if user_logged_in:
   #     redirect('/dashboard', 302)
   # else:
   #     redirect('/auth/login', 302)

# @mod_main.route('/dashboard')
# def dashboard():
#     return render_template('')