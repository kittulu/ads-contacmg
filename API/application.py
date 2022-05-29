from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

class App:
    def app():
        app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')  
        return app

class DB:
    def db():
        app = App.app()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lite.db'
        return SQLAlchemy(app)