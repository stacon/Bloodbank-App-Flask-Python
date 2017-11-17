from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired, regexp


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
            InputRequired(message='You need to provide a password.'),
            regexp('^[A-z,\d]{1,}$', message="Only characters and numbers allowed")
        ]
        , render_kw={"placeholder": "Password (required)"}
    )

    privilege_level = IntegerField(
        'PrivilegeLevel',
        [
            InputRequired(message='Please provide a privilege level')
        ]
        , render_kw={"placeholder": "Privilege Level (required)"}
    )