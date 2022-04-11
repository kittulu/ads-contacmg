from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/myDbName'
db = SQLAlchemy(app)

#usuario
class UsuarioModel(db.Model):
    __tablename__ = "usuario"
 
    id = db.Column(db.Integer, primary_key=True, autoincrement = true)
    user_login = db.Column(db.String(),unique = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
     
    def __init__(self, user_login ,name,age):
        self.user_login = user_login
        self.name = name
        self.age = age
 
    def __repr__(self):
        return f"{self.name}:{self.employee_id}"

        