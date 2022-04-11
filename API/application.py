from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


class App:
    def app():
        app = Flask(__name__) 
        return app

class DB:
    def db():
        app = App.app()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor@localhost/teste'
        return SQLAlchemy(app)

        