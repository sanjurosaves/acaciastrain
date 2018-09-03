#!/home/cadilla1/virtualenv/acaciastrain.cadillacabe.com_web__flask/3.6/bin/python
import os
from flask import Flask, render_template, Blueprint
from datetime import datetime
from flaskapp.bitac import *

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/datetime')
def current_datetim():
    return str(datetime.now())

@app.route('/time')
def current_time():
    return str("Sometime this will work. Sometime is now! The last push was at 20:00.")

@app.route('/tour')
def current_tour():
    shows = dates_to_dict()
    return render_template('tour.html', shows=shows)

@app.route('/')
def get_index():
    return 'The index will live here'

@app.route('/tweets')
def get_tweets():
    return 'The twitter feed will live here'
