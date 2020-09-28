# app/models.py

from app import db

class Article(db.Model):
	"""
	Create Articles Table
	"""

	__tablename__ = 'article'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	article_data = db.Column(db.Text)
	url = db.Column(db.Text)
	datetime = db.Column(db.Date)

class Post(db.Model):
	"""
	Create Post Table
	"""

	__tablename__ = 'post'
	id = db.Column(db.Integer, primary_key=True)
	page_id = db.Column(db.Integer)
	section = db.Column(db.Text)
	post_data = db.Column(db.Text)
	datetime = db.Column(db.Date)

class Pages(db.Model):
	"""
	Create Articles Table
	"""

	__tablename__ = 'pages'
	id = db.Column(db.Integer, primary_key=True)
	page_data = db.Column(db.Text)
	datetime = db.Column(db.Date)
