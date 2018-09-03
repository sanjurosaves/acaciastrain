import os
from flask import Flask, render_template
from datetime import datetime
from flaskapp.bitac import *

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/music')
def get_music():
    return render_template('music.html')

@app.route('/tour')
def get_tour():
    shows = dates_to_dict()
    return render_template('tour.html', shows=shows)

@app.route('/tweets')
def get_tweets():
    return render_template('tweets.html')

@app.route('/log')
def get_log():
    return render_template('log.html')

@app.route('/buy')
def get_buy():
    return render_template('buy.html')

@app.route('/datetime')
def current_datetim():
    return str(datetime.now())

@app.route('/time')
def current_time():
    return str("Sometime this will work. Sometime is now! The last push was at 22:15.")
