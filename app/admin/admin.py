# Import flask dependencies
from flask import request, render_template, \
                  flash, g, session, redirect, url_for



# Import the database object from the main app module
from app import db

from app import app

# Set the route and accepted methods
@app.route('/admin/', methods=['GET', 'POST'])
def admin():

    return render_template("admin/admin.html")


