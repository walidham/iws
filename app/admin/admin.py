# Import flask dependencies
from flask import request, render_template, \
                  flash, g, session, redirect, url_for, jsonify



# Import the database object from the main app module
from app import db_session as db

from app import app

#Imports Models
from app.client import Client
from app.product import Product

# Set the route for admin home page
@app.route('/admin/', methods=['GET', 'POST'])
def admin():

    return render_template("admin/admin.html")

#********************************************
#************* Start client root ************
#********************************************
@app.route('/admin/clients/', methods=['GET', 'POST'])
def clients():

    return render_template("admin/clients.html")

@app.route('/admin/clients_list')
def clients_list():

    cur = db.execute('select company_name, email, description, id from client order by id asc')
    entries = [dict(company_name=row[0],email=row[1], description=row[2],id=row[3]) for row in cur.fetchall()]
    return jsonify(clients=entries)

@app.route('/admin/new_client', methods=['POST'])
def new_client():
    client = Client(request.json['company_name'],request.json['email'],request.json['description'])
    
    db.add(client)
    db.commit()
    #id = cur.lastrowid
    return jsonify({"company_name": request.json['company_name'], 
                    "email": request.json['email'],
                    "description": request.json['description'],
                    "id": client.id})
#********************************************
#************* End client root **************
#********************************************


#********************************************
#************* Start product root ***********
#********************************************
@app.route('/admin/products/', methods=['GET', 'POST'])
def products():

    return render_template("admin/products.html")

@app.route('/admin/products_list')
def product_list():

    cur = db.execute('select product_name, description, id from product order by id asc')
    entries = [dict(product_name=row[0], description=row[1],id=row[2]) for row in cur.fetchall()]
    return jsonify(products=entries)

@app.route('/admin/new_product', methods=['POST'])
def new_product():
    product = Product(request.json['product_name'],request.json['description'])
    
    db.add(product)
    db.commit()
    #id = cur.lastrowid
    return jsonify({"product_name": request.json['product_name'], 
                    
                    "description": request.json['description'],
                    "id": product.id})

#********************************************
#************* End product root *************
#********************************************


