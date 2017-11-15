from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.mod_auth.forms import LoginForm
from app.mod_auth.models import User

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route('/login/', methods=['GET', 'POST'])
def login():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate():

        user = User.query.filter_by(username=form.username.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            return redirect(url_for('mod_auth.home'))

        flash('Wrong username or password', 'error-message')

    return render_template("auth/login.html", form=form)


# class UsersController:
#
#     def show(self):
#         pass
#         # return a view with applications users info and level
#
#     def register(self):
#         pass
#         # retirm a view to register a new application user
#
#     def create(self, data):
#         pass
#         # attempt to create a user database entry, return message of error or success
#
#     def edit(self, id):
#         pass
#         # return a view to edit a specific user
#
#     def update(self, id, data):
#         pass
#         # attempt to update a specific user's data from the database through query and return success or error
#
#     def delete(self, id):
#         pass
#         # attempt to soft_delete a user by adding timestamp to soft_deleted field
#
#     def login(self):
#         pass
#         # return a view to login
#
#     def logout(self):
#         pass
#         # destroy session and redirect to login()