#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Flask init """

from flask import Flask # from flask module import Flask class

app = Flask(__name__)

from app import routes