#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Routes file: specifies http routes """

from flask import g, request, render_template, url_for, redirect
from app import app
from app.forms import NewProductForm, UpdateProductForm, RemoveProductForm, AddUserForm
import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy
from app.users import get_all_users, create_user, update_user
from app.products import get_all_products, create_product, modify_product, remove_product
from app.db import get_db
# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY

DATABASE = "online_store"



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
            
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/products', methods=["GET","POST","PUT"])
def get_products():
    body_list = []
    if "DELETE" in request.method:
        form=request.form
        return remove_product(form["name_to_remove"])
    if "PUT" in request.method:
        form=request.form
        return modify_product(form["old_name"], form["select"], form["change_to"])
    if "POST" in request.method:
        form=request.form
        return create_product(form["name"], form["category"], form["price"], form["stock"], form["img"])
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

@app.route('/products/<product_name>', methods=["GET"])
def get_specific_product(product_name):
    body_list = []
    found = False
    raw_data = get_all_products()
    for item in raw_data:
        if item[0] == product_name:
            temp_dict = {
                "name": item[0],
                "category": item[1],
                "price": item[2],
                "stock": item[3],
                "img": item[4]
                }
            body_list.append(temp_dict)
            found = True
            return render_template("catalog.html", products = body_list)
    if found is False:
        return "Not found, try again..."
        
@app.route('/users', methods=["GET", "POST"])
def get_users():
    out = {"ok": True, "body": ""}
    body_list = []
    if "GET" in request.method:
        raw_data = get_all_users()
        for item in raw_data:
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2],
                }
            body_list.append(temp_dict)
        out["body"] = body_list
        return render_template("about_me.html", first_name=out["body"][0].get("first_name"), last_name=out["body"][0].get("last_name"), hobbies=out["body"][0].get("hobbies"), results=body_list)
    if "POST" in request.method:
        form=request.form
        create_user(form["first_name"], form["last_name"], form["hobbies"])
        return "User added!"
    # if "PUT" in request.method:
    #     update_user("last_name","Test","first_name", "Colin")

@app.route('/adduser', methods=["GET", "POST"])
def new_user():
    form = AddUserForm()
    return render_template('adduser.html', form=form)


@app.route('/countdown/<int:number>')
def countdown(number):
    return "</br>".join([str(i) for i in range(number, 0, -1)])

@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent

@app.route('/addproduct', methods=["GET", "POST"])
def new_product():
    form = NewProductForm()
    return render_template('addproduct.html', form=form)

@app.route('/updateproduct', methods=["GET", "PUT"])
def update_product():
    form = UpdateProductForm()
    return render_template('updateproduct.html', form=form)

@app.route('/removeproduct', methods=["GET", "DELETE"])
def delete_product():
    form=RemoveProductForm()
    return render_template('removeproduct.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/user/<name>')
def user(name):
    return "<h1>Hello, %s!</h1>" % name