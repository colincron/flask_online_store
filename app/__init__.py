#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Flask init """

from flask import Flask # from flask module import Flask class
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

from app import routes