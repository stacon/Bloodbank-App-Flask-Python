from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from sqlalchemy import exc
from werkzeug.security import generate_password_hash
from app import db
from app.mod_bloodtypes.models import Bloodtype
from app.mod_donors.models import Donor
from app.mod_auth.models import User
from app.mod_transactions.models import Transaction
from datetime import date
from random import randint

mod_seeders = Blueprint('seeders', __name__, url_prefix='/seed')

@mod_seeders.route('/')
def index():
    return render_template('main/seeders.html', title="Seeders")

@mod_seeders.route('/bloodtypes')
def bloodtypes():
    bloodtype1 = Bloodtype('0-', 0)
    bloodtype2 = Bloodtype('0+', 0)
    bloodtype3 = Bloodtype('A-', 0)
    bloodtype4 = Bloodtype('A+', 0)
    bloodtype5 = Bloodtype('B-', )
    bloodtype6 = Bloodtype('B+', 0)
    bloodtype7 = Bloodtype('AB-', 0)
    bloodtype8 = Bloodtype('AB+', 0)

    try:
        db.session.add(bloodtype1)
        db.session.add(bloodtype2)
        db.session.add(bloodtype3)
        db.session.add(bloodtype4)
        db.session.add(bloodtype5)
        db.session.add(bloodtype6)
        db.session.add(bloodtype7)
        db.session.add(bloodtype8)
        db.session.commit()
    except exc.IntegrityError:
        flash('Failed to seed Bloodtypes in database, they probably already exist', 'error')
        return redirect(url_for('seeders.index'))
    flash('Bloodtypes seeded', 'success')
    return redirect(url_for('seeders.index'))

@mod_seeders.route('/users')
def users():
    user1 = User('stacon'   , 'secret', 100)
    user2 = User('filgeo'   , 'secret', 100)
    user3 = User('lirnik'   , 'secret', 85)
    user4 = User('tasmas'   , 'secret', 1)
    user5 = User('liknik'   , 'secret', 1)
    user6 = User('biktik'   , 'secret', 1)
    user7 = User('sikpap'   , 'secret', 1)
    user8 = User('paptap'   , 'secret', 1)
    user9 = User('lamtam'   , 'secret', 1)
    user10 = User('aimfak'  , 'secret', 1)

    try:
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.add(user4)
        db.session.add(user5)
        db.session.add(user6)
        db.session.add(user7)
        db.session.add(user8)
        db.session.add(user9)
        db.session.add(user10)
        db.session.commit()
    except exc.IntegrityError:
        flash('Failed to seed Users in database, they probably already exist', 'error')
        return redirect(url_for('seeders.index'))
    flash('Users seeded', 'success')
    return redirect(url_for('seeders.index'))

    return redirect(url_for('seeders.index'))

@mod_seeders.route('/donors')
def donors():
    donor1 = Donor('0000000001', 'Petros', 'Lalos', 'M', date(1995, 1, 1), 1, 'Papagou 10', 'Zografou', 'Attica', '11743', '2109216977')
    donor2 = Donor('0000000002', 'Roumpini', 'Meleti', 'F', date(1994, 2, 28), 2, 'Irakleous 20', 'Kalithea', 'Attica', '11723',
                   '2109015877')
    donor3 = Donor('0000000003', 'Nina', 'Mparka', 'TXM', date(1993, 3, 27), 3, 'Nikaias 10', 'Koridallos', 'Attica', '15426',
                   '6948556622')
    donor4 = Donor('0000000004', 'Serj', 'Tankian', 'M', date(1992, 4, 26), 4, 'Armenion 101', 'Neos Kosmos', 'Attica', '16898',
                   '6987451236')
    donor5 = Donor('0000000005', 'Emily', 'Fakou', 'F', date(1991, 5, 25), 5, 'Dima 1', 'Kifisia', 'Attica', '16235', '6987454512')
    donor6 = Donor('0000000006', 'Giorgos', 'Cheliotis', 'M', date(1990, 6, 24), 6, 'Daskalou 10', 'Marousi', 'Attica', '11749',
                   '5584771223')
    donor7 = Donor('0000000007', 'Maria', 'Ntika', 'F', date(1989, 7, 23), 7, 'Iroon 10', 'Galatsi', 'Attica', '12345', '69554411223')
    donor8 = Donor('0000000008', 'Niki', 'Lalou', 'F', date(1988, 8, 22), 8, 'Ious 110', 'Chalandri', 'Attica', '65432', '2105474123')
    donor9 = Donor('0000000009', 'Nikos', 'Spiridis', 'TXF', date(1987, 9, 21), 8, 'Athanatou 10', 'Nea Makri', 'Attica', '11743',
                   '2106214525')
    donor10 = Donor('0000000010', 'Markos', 'Plytas', 'M', date(1986, 10, 20), 8, 'Alexandrou 2', 'Loutsa', 'Attica', '11453',
                    '21062151477')
    donor11 = Donor('0000000011', 'Koula', 'Papadopoulou', 'F', date(1985, 11, 19), 7, 'Athinas 1', 'Vironas', 'Attica', '12301',
                    '2115478965')
    donor12 = Donor('0000000012', 'Kostas', 'Tsakonas', 'M', date(1984, 12, 18), 6, 'Omonoias 13', 'Psichiko', 'Attica', '45678',
                    '2114563214')
    donor13 = Donor('0000000013', 'Antonis', 'Politanos', 'M', date(1983, 1, 17), 1, 'Patsi 44', 'Elliniko', 'Attica', '65421',
                    '2136547745')
    donor14 = Donor('0000000014', 'Tasos', 'Ichos', 'M', date(1982, 2, 16), 1, 'Tatsi 13', 'Glyfada', 'Attica', '32145', '21032326512')
    donor15 = Donor('0000000015', 'Pantelis', 'Seisoglou', 'M', date(1981, 3, 15), 1, 'Sikias 14', 'Varkiza', 'Attica', '7896',
                    '21021515123')
    donor16 = Donor('0000000016', 'Kelly', 'Vagkelly', 'TXM', date(1980, 4, 14), 2, 'Aetofolias 15', 'Vouliagmeni', 'Attica', '45632',
                    '1225153145')
    donor17 = Donor('0000000017', 'Dora', 'Nikolopoulou', 'F', date(1979, 5, 13), 7, 'Eirinis 2', 'Athina', 'Attica', '45678',
                    '1226548321')
    donor18 = Donor('0000000018', 'Amalia', 'Spiropoulou', 'F', date(1978, 6, 12), 8, 'Dilou 2', 'Koliatsou', 'Thessaloniki', '45621',
                    '6958475896')
    donor19 = Donor('0000000019', 'Ntina', 'Stoka', 'TXM', date(1977, 7, 11), 8, 'Arsinois 1', 'Menidi', 'Volos', '45689', '6958478521')
    donor20 = Donor('0000000020', 'Eva', 'Papa', 'F', date(1976, 8, 10), 6, 'Estellas 45', 'Liosia', 'Kriti', '45612', '6936251452')
    donor21 = Donor('0000000021', 'Periklis', 'Bogos', 'M', date(1975, 9, 9), 7, 'Maginas 10', 'Peristeri', 'Attica', '45678',
                    '6936251452')
    donor22 = Donor('0000000022', 'Stratos', 'Tsaknis', 'M', date(1974, 10, 8), 7, 'Aggelon 23', 'Acharnai', 'Attica', '12365',
                    '2102145236')
    donor23 = Donor('0000000023', 'Stavros', 'Mouros', 'M', date(1973, 11, 7), 5, 'Mousikwn 1', 'Peristeri', 'Attica', '87956',
                    '2113214563')
    donor24 = Donor('0000000024', 'Pavlos', 'Fidis', 'M', date(1972, 12, 6), 4, 'Arxigou 15', 'Peiraias', 'Attica', '45678', '2136545649')
    donor25 = Donor('0000000025', 'Markos', 'Ntais', 'M', date(1971, 1, 5), 5, 'Nikis 10', 'Nikaia', 'Attica', '11743', '2102141579')
    donor26 = Donor('0000000026', 'Georgia', 'Leka', 'F', date(1970, 2, 4), 4, 'Parou 65', 'Faliro', 'Attica', '11743', '2145632147')
    donor27 = Donor('0000000027', 'Alexandros', 'Eleftheris', 'M', date(1969, 3, 3), 4, 'Sirou 1', 'Alimos', 'Attica', '65478',
                    '2145654565')
    donor28 = Donor('0000000028', 'Alexandra', 'Nika', 'F', date(1961, 5, 2), 5, 'Manafis 65', 'Voula', 'Attica', '12345',
                    '2144444444')
    donor29 = Donor('0000000029', 'Alexandra', 'Louka', 'F', date(1968, 4, 2), 5, 'Anafis 65', 'Elliniko', 'Attica', '12345',
                    '2144444444')
    donor30 = Donor('0000000030', 'Takis', 'Stakis', 'M', date(1967, 5, 1), 4, 'Samoi 2', 'Elliniko', 'Attica', '12345', '2132132132')
    try:
        db.session.add(donor1)
        db.session.add(donor2)
        db.session.add(donor3)
        db.session.add(donor4)
        db.session.add(donor5)
        db.session.add(donor6)
        db.session.add(donor7)
        db.session.add(donor8)
        db.session.add(donor9)
        db.session.add(donor10)
        db.session.add(donor11)
        db.session.add(donor12)
        db.session.add(donor13)
        db.session.add(donor14)
        db.session.add(donor15)
        db.session.add(donor16)
        db.session.add(donor17)
        db.session.add(donor18)
        db.session.add(donor19)
        db.session.add(donor20)
        db.session.add(donor21)
        db.session.add(donor22)
        db.session.add(donor23)
        db.session.add(donor24)
        db.session.add(donor25)
        db.session.add(donor26)
        db.session.add(donor27)
        db.session.add(donor28)
        db.session.add(donor29)
        db.session.add(donor30)
        db.session.commit()
    except exc.IntegrityError:
        flash('Failed to seed Donors in database, they probably already exist', 'error')
        return redirect(url_for('seeders.index'))
    flash('Donors seeded', 'success')
    return redirect(url_for('seeders.index'))

@mod_seeders.route('/transactions')
def transactions():
    donors = Donor.query.all()

    for donor in donors:
        deposit1 = Transaction(donor.id, 'D', donor.bloodtype_id, randint(800, 1200), donor)
        withdraw1 = Transaction(donor.id, 'W', randint(1, 8), randint(500, 800), donor)
        deposit2 = Transaction(donor.id, 'D', donor.bloodtype_id, randint(500, 800), donor)
        withdraw2 = Transaction(donor.id, 'W', randint(1, 8), randint(200, 500), donor)
        deposit3 = Transaction(donor.id, 'D', donor.bloodtype_id, randint(600, 1200), donor)

        try:
            db.session.add(deposit1)
            db.session.add(withdraw1)
            db.session.add(deposit2)
            db.session.add(withdraw2)
            db.session.add(deposit3)
            db.session.commit()
        except exc.IntegrityError:
            flash('Failed to seed Transactions in database, they probably already exist', 'error')
            return redirect(url_for('seeders.index'))
    flash('Transactions seeded', 'success')
    return redirect(url_for('seeders.index'))
