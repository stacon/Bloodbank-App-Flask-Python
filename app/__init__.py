from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('master/404.html'), 404


from app.mod_auth.controllers import mod_auth as auth_module
from app.mod_donors.controllers import mod_donors as donors_module
from app.mod_bloodtypes.controllers import mod_bloodtypes as bloodtypes_module
from app.mod_transactions.controllers import mod_transactions as transactions_module
from app.mod_main.controllers import mod_main as main_module
from app.mod_seeders.controllers import mod_seeders as seeders_module

# Register blueprint(s)
app.register_blueprint(main_module)
app.register_blueprint(auth_module)
app.register_blueprint(donors_module)
app.register_blueprint(bloodtypes_module)
app.register_blueprint(transactions_module)
app.register_blueprint(seeders_module)


# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
