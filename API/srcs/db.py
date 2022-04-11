from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

db_name = 'conta_cmg.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conta_cmg.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)






#class User(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  username = db.Column(db.String(80), unique=True, nullable=False)
   # email = db.Column(db.String(120), unique=True, nullable=False)
#class Person(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  name = db.Column(db.String(50), nullable=False)
   # addresses = db.relationship('Address', backref='person', lazy=True)
    #def __repr__(self):
     #   return '<User %r>' % self.username
