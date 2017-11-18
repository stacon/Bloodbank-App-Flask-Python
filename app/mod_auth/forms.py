from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import InputRequired, regexp, ValidationError, EqualTo
from app.mod_auth.models import User


class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        [
            InputRequired(message='You need to provide a username.')
        ]
        , render_kw={"placeholder": "username"}

    )

    password = PasswordField(
            'Password',
            [
                InputRequired(message='You need to provide a password.')
            ]
            , render_kw={"placeholder": "password"}
        )


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        [
            InputRequired(message='Please provide a username'),
            regexp('^[A-z][A-z,\d]{1,}$', message="Only characters and numbers allowed")

        ]
        , render_kw={"placeholder": "Username (required)"}
    )

    password = PasswordField(
        'Password',
        [
            InputRequired(message='You need to provide a password_hash.'),
            regexp('^[A-z,\d]{1,}$', message="Only characters and numbers allowed"),
            EqualTo('confirm_password', message ="Password fields don't match")
        ]
        , render_kw={"placeholder": "Password (required)"}
    )

    confirm_password = PasswordField(
        'Confirm Password',
        render_kw = {"placeholder": "Repeat Password (required)"}
    )

    privilege_level = IntegerField(
        'PrivilegeLevel',
        [
            InputRequired(message='Please provide a privilege level')
        ]
        , render_kw={"placeholder": "Privilege Level (required)"}
    )

    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')


class UpdateForm(FlaskForm):
    username = StringField(
        'Username', render_kw={"disabled": "True"}
    )

    password = PasswordField(
        'Password', render_kw={"placeholder": "Password (required)"}
    )

    privilege_level = IntegerField(
        'PrivilegeLevel', render_kw={"placeholder": "Privilege Level (required)"}
    )

    submit = SubmitField('Submit')