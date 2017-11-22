from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.mod_donors.forms import RegistrationForm, UpdateForm
from app.mod_donors.models import Donor
from flask_login import login_required
from app import db

mod_donors = Blueprint('donors', __name__, url_prefix='/donors')

@mod_donors.route('/')
@login_required
def index():
    return render_template('donors/index.html', title='Donors')


@mod_donors.route('/view')
@login_required
def view():
    return render_template('donors/view.html', title="#name's info ")

@mod_donors.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        new_donor = Donor(
            insurance_number=form.insurance_number.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            gender=form.gender.data,
            bloodtype_id=form.bloodtype.data,
            dob=form.dob.data,
            address=form.address.data,
            city=form.city.data,
            state=form.state.data,
            zip_code=form.zip_code.data,
            contact_number=form.contact_number.data
        )

        # add user to database
        db.session.add(new_donor)
        db.session.commit()
        flash(u'Donor: {} {} registered successfully'.format(form.first_name.data, form.last_name.data), 'success')

        # redirect to users panel
        return redirect(url_for('donors.index'))

    # load registration template
    return render_template("donors/register.html", form=form, title='Donor registration')

@mod_donors.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    return render_template('donors/edit.html', title='Edit #name')

    donor = Donor.query.get_or_404(id)
    form =UpdateForm(obj=donor)
    if form.validate_on_submit():
        donor.gender = form.gender.data
        donor.bloodtype_id = form.bloodtype.data
        donor.address = form.address.data
        donor.city = form.city.data
        donor.state = form.state.data
        donor.zip_code = form.zip_code.data
        donor.contact_number = form.contact_number.data
        db.session.commit()
        flash('You have successfully updated user information', 'success')

        # redirect to donors view page
        return redirect(url_for('donors.view'), id=id)

    form.insurance_number.data = donor.insurance_number
    form.first_name.data = donor.first_name
    form.last_name.data = donor.last_name
    form.gender.data = donor.gender
    form.bloodtype.data = donor.bloodtype_id
    form.dob.data = donor.dob
    form.address.data = donor.address
    form.city.data = donor.city
    form.state.data = donor.state
    form.zip_code.data = donor.zip_code
    form.contact_number = donor.contact_number
    return render_template("donors/edit.html", form=form, donor=donor, action="Edit",
                           title=u"Edit #{} {} {}".format(donor.insurance_number, donor.first_name, donor.last_name))


# class DonorsController:
#
#     def view(self,id):
#         pass
#         # return a view with the information of a particular donor along his blood transactions
#
#     def register(self):
#         pass
#         # return a view to register a donor
#
#     def create(self, data):
#         pass
#         # attempt to create a donor in the database and return success or error
#
#     def edit(self, id):
#         pass
#         # return a view to edit donor's data
#
#     def update(self, data):
#         pass
#         # attempt to update the donor's data based on his id, returning error or success message
#
#     def donate(self, id, milliliters, bloodtype_id):
#         pass
#         # attemp a blood deposit transaction for the given donor
#
#     def withdraw(self, id, milliliters, bloodtype_id):
#         pass
#         # attemp a blood withdraw transaction for the given donor
#
#     def transaction_history(self, id, transaction_type = False):
#         pass
#         # return a list with donors history of transactions
#         # if transaction type is provided use it as a filter
