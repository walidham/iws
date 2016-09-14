# Import flask and template operators
from flask import Flask, render_template, _app_ctx_stack

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

from app.database import db_session

from app.database import init_db

from app.client import Client

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')



# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
#from app.mod_auth.controllers import mod_auth as auth_module
import app.admin.admin as admin_panel
import app.feature_req.feature as feature


# Register blueprint(s)
#app.register_blueprint(auth_module)


# Build the database:
# This will create the database file using SQLAlchemy
init_db()
#client = Client('ISET 2', 'admin@localhost 2','ISET Gafsa 2')
#db_session.add(client)
#db_session.commit()
#Client.query.all()
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

