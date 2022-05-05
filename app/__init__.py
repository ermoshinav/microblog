from flask import Flask
from flask.ext import foo
from config import Config

app = Flask(__name__)
app.config.from_object('Config')
db=SQLAlchemy(app)
from app import routes, views, models
