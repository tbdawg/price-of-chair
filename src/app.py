from flask import Flask, render_template

import src.models.alerts.views
import src.models.stores.views
import src.models.users.views
from src.common.database import Database
import os

__author__ = 'jslvtr'


app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = "123"


@app.before_first_request
def init_db():
    Database.initialize()


@app.route('/')
def home():
    mlab_uri = os.environ.get('MONGOLAB_URI')
    return render_template('home.jinja2', mLab_Uri=mlab_uri)

app.register_blueprint(src.models.users.views.user_blueprint, url_prefix="/users")
app.register_blueprint(src.models.stores.views.store_blueprint, url_prefix="/stores")
app.register_blueprint(src.models.alerts.views.alert_blueprint, url_prefix="/alerts")
