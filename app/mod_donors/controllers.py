from flask import Blueprint, render_template, flash, redirect, url_for
from app.mod_donors.forms import RegistrationForm, UpdateForm, SearchForm
from app.mod_donors.models import Donor
from app.mod_donors.models import Transaction
from flask_login import login_required
from app import db
from sqlalchemy import or_

mod_donors = Blueprint('donors', __name__, url_prefix='/donors')

@mod_donors.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = SearchForm()

    if form.validate_on_submit():
            donors = db.session.query(Donor).filter(or_(
                Donor.last_name.contains(form.input.data),
                Donor.contact_number.contains(form.input.data),
                Donor.insurance_number.contains(form.input.data)
            )
        )
    else:
        donors = None
    return render_template('donors/index.html', form=form, donors=donors, title='Donors')


@mod_donors.route('/view/<int:id>', methods=['GET', 'POST'])
@login_required
def view(id):
    donor = Donor.query.get_or_404(id)
    donations = Transaction.query.filter_by(donor_id=donor.id, type='D').limit(10).all()
    withdrawals = Transaction.query.filter_by(donor_id=donor.id, type='W').limit(10).all()

    return render_template(
        'donors/view.html',
        donor=donor,
        donations=donations,
        withdrawals=withdrawals,
        title=u"{}'s information".format(donor.last_name)
    )

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


@mod_donors.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
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
        return redirect(url_for('donors.view', id=donor.id))

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
    form.contact_number.data = donor.contact_number
    return render_template("donors/edit.html", form=form, donor=donor, action="Edit",
                           title=u"Edit #{} {} {}".format(donor.insurance_number, donor.first_name, donor.last_name))


@mod_donors.route('/delete/<int:id>')
@login_required
def delete(id):

    donor = Donor.query.get_or_404(id)
    try:
        db.session.delete(donor)
        db.session.commit()
    except:
        flash('Unexpected database error')
        return redirect(url_for('donors.index'))
    flash(u'Donor {} {} has been successfully deleted!'.format(donor.first_name, donor.last_name), 'success')
    return redirect(url_for('donors.index'))