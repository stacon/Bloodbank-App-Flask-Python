from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField,HiddenField
from wtforms.validators import InputRequired

class DonationForm(FlaskForm):
    milliliters = IntegerField(
        'Milliliters',
        [
            InputRequired(message='Please enter a valid quantity'),
        ],
        render_kw={'placeholder': 'donation amount in milliliters'}

    )


    submit = SubmitField('Donate')


class WithdrawalForm(FlaskForm):
    milliliters = IntegerField(
        'Milliliters',
        [
            InputRequired(message='Please enter a valid quantity'),
        ],
        render_kw={'placeholder': 'withdrawal amount in milliliters'}
    )

    bloodtype = SelectField(
        'Blood Type',
        choices=[
            ('1', '0-'),
            ('2', '0+'),
            ('3', 'A-'),
            ('4', 'A+'),
            ('5', 'B-'),
            ('6', 'B+'),
            ('7', 'AB-'),
            ('8', 'AB+')
        ],
        render_kw={'placeholder': 'Blood type'}
    )

    submit = SubmitField('Withdraw')