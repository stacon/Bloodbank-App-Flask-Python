from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.mod_auth.forms import LoginForm, RegistrationForm
from app.mod_auth.models import User
from app import db, login_manager
from flask_login import login_user,logout_user, login_required, current_user
from sqlalchemy import exc
from bcrypt import hashpw,checkpw

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route('/users/', methods=['GET' ,'POST'])
@login_required
def index():
    users = User.query.order_by(User.privileges_level).all()
    return render_template("auth/index.html", users=users)

@mod_auth.route('/register/', methods=['GET' ,'POST'])
@login_required
def register():
    if not request.form:
        form = RegistrationForm()
    form = RegistrationForm(request.form)

    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            password=form.password.data,
            privileges_level=form.privilege_level.data
        )
        db.session.add(new_user)
        try:
            db.session.commit()
        except exc.IntegrityError:
            flash(u'Username {} already exists'.format(form.username.data), 'error')
            return render_template("auth/register.html", form=form)
        flash(u'User {} created successfully'.format(form.username.data), 'success')
        return redirect(url_for('auth.index'))
    return render_template("auth/register.html", form=form)

@mod_auth.route('/edit/')
@login_required
def edit():
    # user = User.query.filter_by(id=id).first()
    return render_template('auth/edit.html')


@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash('Username not found', 'error')
        elif form.password.data != user.password:
            flash('Invalid password!', 'error')
        else:
            login_user(user)
            flash('You have successfully logged in', 'success')
            return redirect(url_for('main.index'))

        # if user:
        #     login_user(user)
        #     flash(u'Welcome {}, you have successfully logged in'.format(form.username.data), 'success')
        #     return redirect(url_for("main.index"))

    return render_template("auth/signin.html", form=form)

@mod_auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out', 'success')
    return redirect(url_for('auth.signin'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('You need to be logged in for this view', 'error')
    return redirect(url_for('auth.signin'))

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
