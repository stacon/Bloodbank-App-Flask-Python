from wtforms import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(Form):
    username = StringField('Username', [
        DataRequired(message='Username appears to be incorrect.')])

    password = PasswordField('Password', [
        DataRequired(message='Password appears to be incorrect.')])