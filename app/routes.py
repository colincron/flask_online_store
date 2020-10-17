#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Routes file: specifies http routes """

from flask import g, request, render_template, url_for, redirect
from app import app
from app.forms import NewProductForm
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

def get_all_users():
    cursor = get_db().execute("select * from user;", ())
    results = cursor.fetchall()
    cursor.close()
    return results

def create_user():
    cursor = get_db().execute("insert into user values ('Test', 'LastName', 'skiing');")
    cursor.close()

def create_product(name, category, price, stock, img):
    cursor = get_db().execute("insert into products(prod_name, prod_cat, prod_price, prod_stock, prod_img) values ('%s', '%s','%s','%s','%s');" % (name, category, price, stock, img)) 
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

@app.route('/products', methods=["GET","POST"])
def get_products():
    body_list = []
    if "GET" in request.method:
        # get_all_users() returns all records from the user table
        raw_data = get_all_products()
        for item in raw_data:
            temp_dict = {
                "name": item[0],
                "category": item[1],
                "price": item[2],
                "stock": item[3],
                "img": item[4]
                }
            body_list.append(temp_dict)
        return render_template("catalog.html", products = body_list)

    if "POST" in request.method:
        form=request.form
        create_product(form["name"], form["category"], form["price"], form["stock"], form["img"])
        return "Hello world!"
    
@app.route('/users', methods=["GET"])
def get_users():
    out = {"ok": True, "body": ""}
    body_list = []
    if "GET" in request.method:
        # get_all_users() returns all records from the user table
        raw_data = get_all_users()
        for item in raw_data:
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2],
                }
            body_list.append(temp_dict)
        out["body"] = body_list
        return render_template("about_me.html", first_name=out["body"][0].get("first_name"), last_name=out["body"][0].get("last_name"), hobbies=out["body"][0].get("hobbies"))
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
    # if request.method == 'POST':
    #     name = request.form.get('name')
    #     category = request.form.get('category')
    #     price = request.form.get('price')
    #     stock = request.form.get('stock')
    #     img = request.form.get('img')

    return render_template('adminconsole.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/user/<name>')
def user(name):
    return "<h1>Hello, %s!</h1>" % name