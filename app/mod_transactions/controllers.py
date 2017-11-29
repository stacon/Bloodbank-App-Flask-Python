from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.mod_transactions.models import Transaction
from app.mod_donors.models import Donor
from app.mod_bloodtypes.models import Bloodtype
from app.mod_transactions.forms import DonationForm, WithdrawalForm
from flask_login import login_required

mod_transactions = Blueprint('transactions', __name__, url_prefix='/transactions')

@mod_transactions.route('/donate/<int:id>', methods=['GET', 'POST'])
@login_required
def donate(id):
    donor = Donor.query.get_or_404(id)
    form = DonationForm()

    if  form.validate_on_submit():
        new_transaction = Transaction(
            donor_id=donor.id,
            type='D',
            bloodtype_id=donor.bloodtype_id,
            milliliters=form.milliliters.data,
            donor=donor
        )

        # add transaction to database
        db.session.add(new_transaction)
        db.session.commit()

        # # add donated amount to donors info (DEPRECATED)
        # donor.donate(form.milliliters.data) (DEPRECATED)


        flash(u'You have successfully donated {} milliliters'.format(form.milliliters.data))
        return redirect(url_for('donors.view', id=donor.id))
    return render_template(
        'transactions/donate.html',
        donor=donor,
        form=form,
        title=u"Donation Form Donor:{} {}".format(donor.first_name, donor.last_name)
    )


@mod_transactions.route('/withdraw/<int:id>', methods=['GET', 'POST'])
@login_required
def withdraw(id):
    donor = Donor.query.get_or_404(id)
    form = WithdrawalForm()

    if form.validate_on_submit():
        new_transaction = Transaction(
            donor_id=donor.id,
            type='W',
            bloodtype_id=form.bloodtype.data,
            milliliters=form.milliliters.data,
            donor=donor
        )

        # add transaction to database
        db.session.add(new_transaction)
        db.session.commit()

        # # add withdrawn amount to donors info (DEPRECATED)
        # donor.withdraw(form.milliliters.data) (DEPRECATED)


        flash(u'You have successfully donated {} milliliters'.format(form.milliliters.data))
        return redirect(url_for('donors.view', id=donor.id))
    return render_template('transactions/withdraw.html',
                           donor=donor,
                           form=form,
                           title=u"Withdrawal Form Donor:{} {}".format(donor.first_name, donor.last_name)
                           )