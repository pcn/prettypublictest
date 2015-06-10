#!/usr/bin/env python

from flask import Flask, request, jsonify
import sys, json
import logging
import logging.handlers

from prettypublictest.version import __version__

app = Flask(__name__)

# load the following from a settings file
app.config.from_envvar('DB_SETTINGS', silent=True)

if app.config['DB_TYPE'].lower() == 'none':
    pass
else:
    from flaskext.mysql import MySQL
    mysql = MySQL()
    mysql.init_app(app)

@app.route('/')
def hello_world():
    return 'These are not the droids you are looking for'
