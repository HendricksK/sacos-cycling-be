# app/__init__.py

from flask import Flask #import flask 
from flask_sqlalchemy import SQLAlchemy #import flask_sqlalchemy
from flask_migrate import Migrate

from config import app_config


# db variable initialization
db = SQLAlchemy()

def create_app(config_name):

	app = Flask(__name__, instance_relative_config=True)
	print(app_config)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')

	db.init_app(app)

	# models were alreadt defined for BE app
	# migrate = Migrate(app, db)
	# from app import models

	# TODO: define URLs, would like to move this to a routes file but will see if that is possible in future

	@app.route('/')
	def index():
		return 'last night I lost all my patience'

	@app.route('/articles')
	def get_articles():
		return 'compensating for my feelings'

	@app.route('/article')
	def get_article():
		return 'compensating for my feelings {id}'

	# return app really is require
	return app
