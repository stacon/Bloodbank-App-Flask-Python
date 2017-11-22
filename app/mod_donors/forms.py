from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, DateField
from wtforms.validators import InputRequired, ValidationError
from app.mod_donors.models import Donor


class RegistrationForm(FlaskForm):
    insurance_number = StringField(
        'Insurance ID',
        [
            InputRequired(message='Please provide an insurance ID')
        ]
        , render_kw={"placeholder": "Insurance ID (required)"}
    )

    first_name = StringField(
        'First Name',
        [
            InputRequired(message='Please provide a First name'),

        ]
        , render_kw={"placeholder": "First name (required)"}
    )

    last_name = StringField(
        'Last Name',
        [
            InputRequired(message='Please provide a Last name'),
        ]
        , render_kw={"placeholder": "Last name (required)"}
    )

    gender = SelectField(
        'Gender',
        choices=[('M', 'Male'), ('F', 'Female'), ('TXM', 'Transgender ex-Male'), ('TXF', 'Transgender ex-Female')]
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
        render_kw={'placeholder':'Blood type'}
    )

    dob = DateField(
        'Birth date',
        format='%d/%m/%Y',
        render_kw={'id':'datepicker', 'placeholder':'Birthdate dd/mm/yyyy (required)'},
    )

    address = StringField(
        'Address',
        [
            InputRequired(message='Please provide an Address'),
        ],
        render_kw={'placeholder': 'Address (required)'}

    )

    city = StringField(
        'Address',
        [
            InputRequired(message='Please provide a city name'),
        ],
        render_kw={'placeholder':'City (required)'}

    )

    state = StringField(
        'State',
        [
            InputRequired(message='Please provide a state'),
        ],
        render_kw={'placeholder':'State (required)'}

    )

    zip_code = StringField(
        'Zip Code',
        render_kw={'placeholder':'Zip Code (required)'}
    )

    contact_number = StringField(
        'Phone Number',
        [
            InputRequired(message='Please provide a zip code')
        ],
        render_kw={'placeholder':'Phone number (required)'}
    )

    submit = SubmitField('Register')

    def validate_insurance_number(self, field):
        if Donor.query.filter_by(insurance_number=field.data).first():
            raise ValidationError('Insurance ID is already in use.')

class UpdateForm(FlaskForm):
    insurance_number = StringField(
        'Insurance ID',
        render_kw={"disabled": "True"}
    )

    first_name = StringField(
        'First Name',
        render_kw={"disabled": "True"}
    )

    last_name = StringField(
        'Last Name',
        render_kw={"disabled": "True"}
    )

    gender = SelectField(
        'Gender',
        choices=[('M', 'Male'), ('F', 'Female'), ('TXM', 'Transgender ex-Male'), ('TXF', 'Transgender ex-Female')]
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
        render_kw={'placeholder':'Blood type'}
    )

    dob = DateField(
        'Birth date',
        format='%d/%m/%Y',
        render_kw={'id':'datepicker', 'placeholder':'Birthdate dd/mm/yyyy (required)'},
    )

    address = StringField(
        'Address',
        [
            InputRequired(message='Please provide an Address'),
        ],
        render_kw={'placeholder': 'Address (required)'}

    )

    city = StringField(
        'Address',
        [
            InputRequired(message='Please provide a city name'),
        ],
        render_kw={'placeholder':'City (required)'}

    )

    state = StringField(
        'State',
        [
            InputRequired(message='Please provide a state'),
        ],
        render_kw={'placeholder':'State (required)'}

    )

    zip_code = StringField(
        'Zip Code',
        render_kw={'placeholder':'Zip Code (required)'}
    )

    contact_number = StringField(
        'Phone Number',
        [
            InputRequired(message='Please provide a zip code')
        ],
        render_kw={'placeholder':'Phone number (required)'}
    )

    submit = SubmitField('Update')