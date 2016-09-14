# Import flask dependencies
from flask import request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

from datetime import datetime

# Import the database object from the main app module
from app import db_session as db

from app import app
from app.client import Client
from app.feature import Feature

# Set the route and accepted methods
@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template("feat_req/index.html")

@app.route('/features_list')
def features_list():

    cur = db.execute('select title, target_date, ticket_url, client_id, client_priority, description, id from feature order by id asc')
    entries = [dict(title=row[0],target_date=row[1], ticket_url=row[2],client_id=row[3],client_priority=row[4],description=row[5],id=row[6]) for row in cur.fetchall()]
    return jsonify(features=entries)

@app.route('/new_feature', methods=['POST'])
def new_feature():
    date_object = datetime.strptime(request.json['target_date'], '%m-%d-%Y')
    feature = Feature(request.json['title'],request.json['description'],request.json['client_priority'],date_object,request.json['ticket_url'],request.json['client_id'])

    db.add(feature)
    db.commit()
    #id = cur.lastrowid
    return jsonify({"title": request.json['title'], 
                    "description": request.json['description'],
                    "client_priority": request.json['client_priority'],
                    "target_date": request.json['target_date'],
                    "ticket_url": request.json['ticket_url'],
                    "client_id": request.json['client_id'],
                    "id": feature.id})
