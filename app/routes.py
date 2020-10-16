#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Routes file: specifies http routes """

from flask import g, request, render_template, url_for, redirect
from app import app
from forms import NewProductForm
import sqlite3
import os


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

DATABASE = "online_store"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_all_products():
    cursor = get_db().execute("select * from products;", ())
    results = cursor.fetchall()
    cursor.close()
    return results

def create_user():
    cursor = get_db().execute("insert into user values ('Test', 'LastName', 'skiing');")
    cursor.close()

def update_user(toset, string1, whereset, string2  ):
    cursor = get_db().execute('update user set ' + toset + '=' + string1 + ' where ' + whereset + '=' + string2 + ';')
    cursor.close()
 
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
            

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/aboutme', methods=["GET"])
def aboutme():
    return {
        "first_name": "Colin",
        "last_name": "Cron",
        "hobby": "Gardening"
    }

@app.route('/users', methods=["GET"])
def get_products():
    out = {"ok": True, "body": ""}
    body_list = []
    if "GET" in request.method:
        # get_all_users() returns all records from the user table
        raw_data = get_all_products()
        for item in raw_data:
            temp_dict = {
                "Product Name": item[0],
                "Category": item[1],
                "Price": item[2],
                "Stock": item[3],
                "IMG": item[4]
                }
            body_list.append(temp_dict)
        out["body"] = body_list
        return render_template("base.html", name=out["body"][0].get("Product Name"), category=out["body"][0].get("Category"), price=out["body"][0].get("Price"), stock=out["body"][0].get("Stock"), img_url=out["body"][0].get("IMG"))
    # if "POST" in request.method:
    #     create_user()
    # if "PUT" in request.method:
    #     update_user("last_name","Test","first_name", "Colin")
    
@app.route('/countdown/<int:number>')
def countdown(number):
    return "</br>".join([str(i) for i in range(number, 0, -1)])

@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent

@app.route('/adminconsole', methods=["GET", "POST"])
def new_product():
    form = NewProductForm()
    return render_template('adminconsole.html', form=form)