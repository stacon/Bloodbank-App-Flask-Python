from flask import Blueprint, render_template, flash, redirect, url_for
from app.mod_auth.forms import LoginForm, RegistrationForm, UpdateForm
from app.mod_auth.models import User
from app import db, login_manager
from flask_login import login_user,logout_user, login_required, current_user
from werkzeug.security import generate_password_hash

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/users')
@login_required
def index():

    # restrict access for non admins
    if not current_user.is_admin:
        flash('You need to have admin access level for this page', 'error')
        return redirect(url_for('main.index'))


    users = User.query.order_by(User.privileges_level.desc()).all()
    return render_template("auth/index.html", users=users, title="Users")


@mod_auth.route('/users/register', methods=['GET' ,'POST'])
@login_required
def register():


    # restrict access for non admins
    if not current_user.is_admin:
        flash('You need to have admin access level for this page', 'error')
        return redirect(url_for('main.index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            password=form.password.data,
            privileges_level=form.privilege_level.data
        )

        # add user to database
        db.session.add(new_user)
        db.session.commit()
        flash(u'User {} created successfully'.format(form.username.data), 'success')

        # redirect to users panel
        return redirect(url_for('auth.index'))

    # load registration template
    return render_template("auth/register.html", form=form, title='User registation')


@mod_auth.route('/users/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):

    # restrict access for non admins
    if not current_user.is_admin:
        flash('You need to have admin access level for this page', 'error')
        return redirect(url_for('main.index'))

    user = User.query.get_or_404(id)
    form = UpdateForm(obj=user)
    if form.validate_on_submit():
        if form.password.data:
            user.password = generate_password_hash(form.password.data)
        user.privileges_level = form.privilege_level.data
        db.session.commit()
        flash('You have successfully updated user information', 'success')

        # redirect to users page
        return redirect(url_for('auth.index'))

    form.username.data = user.username
    form.privilege_level.data = user.privileges_level
    return render_template("auth/edit.html", form=form, user=user, action="Edit", title=u"Edit #{} {}".format(user.id, user.username))


@mod_auth.route('/users/delete/<int:id>')
def delete(id):

    # restrict access for non admins
    if not current_user.is_admin:
        flash('You need to have admin access level for this page', 'error')
        return redirect(url_for('main.index'))

    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
    except:
        flash('Unexpected database error')
        return redirect(url_for('auth.index'))
    flash(u'User {} has been successfully deleted!'.format(user.username), 'success')
    return redirect(url_for('auth.index'))

@mod_auth.route('/login', methods=['GET', 'POST'])
def login():

    # if the user is logged in redirect to the dashboard
    if current_user.is_authenticated and current_user.is_active:
        flash('You are already logged in', 'warning')
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():

        # try fetching the corresponding user and check password match
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):

            # log user in
            login_user(user)
            flash('You have successfully logged in', 'success')

            # redirect after successful login
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password!', 'error')

    # load sign in template
    return render_template("auth/signin.html", form=form, title="Sign in")

@mod_auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out', 'success')
    return redirect(url_for('auth.login'))


@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('You need to be logged in for this view', 'error')
    return redirect(url_for('auth.login'))