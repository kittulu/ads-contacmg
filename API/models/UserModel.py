import sys
sys.path.append("/home/kitullu/Documentos/ads-contacmg/API/")
from application import App, DB
from flask_sqlalchemy import SQLAlchemy

db = DB.db()

#app = App.app()
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor@localhost/teste'
#db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    psw = db.Column(db.String(11), nullable=False)
    #endereco = db.relationship('Endereço', backref='Usuário', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

