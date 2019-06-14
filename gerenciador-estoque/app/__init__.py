import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from app.config import Config

app = Flask(__name__)
#app.config.from_object(Config)
app.config['SECRET_KEY'] = '98eaae3046f8e06f7de304c1ef160c69'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from app import routes
