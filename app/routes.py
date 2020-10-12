#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Routes file: specifies http routes """

from app import app

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/aboutme')
def aboutme():
    return {
        "first_name": "Colin",
        "last_name": "Cron",
        "hobby": "Guitar"
    }