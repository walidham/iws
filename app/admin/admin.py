# Import flask dependencies
from flask import request, render_template, \
                  flash, g, session, redirect, url_for, jsonify



# Import the database object from the main app module
from app import db_session as db

from app import app

from app.client import Client

# Set the route and accepted methods
@app.route('/admin/', methods=['GET', 'POST'])
def admin():

    return render_template("admin/admin.html")

# Set the route and accepted methods
@app.route('/admin/clients/', methods=['GET', 'POST'])
def clients():

    return render_template("admin/clients.html")

@app.route('/admin/clients_list')
def clients_list():
    #db = get_db()
    cur = db.execute('select company_name, email, description, id from client order by id asc')
    entries = [dict(company_name=row[0],email=row[1], description=row[2],id=row[3]) for row in cur.fetchall()]
    return jsonify(clients=entries)

@app.route('/admin/new_client', methods=['POST'])
def new_client():
    client = Client(request.json['company_name'],request.json['email'],request.json['description'])
    #cur = db.execute('insert into client (company_name, email, description) values (?, ?, ?)', {'company_name':request.json['company_name']},{'email':request.json['email']},{'description':request.json['description']})
    db.add(client)
    db.commit()
    #id = cur.lastrowid
    return jsonify({"company_name": request.json['company_name'], 
                    "email": request.json['email'],
                    "description": request.json['description'],
                    "id": client.id})


