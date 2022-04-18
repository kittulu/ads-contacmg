from application import DB
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = DB.db()

@dataclass
class User(db.Model):
    id:int
    first_name:str
    last_name:str
    email:str
    cpf:str
    psw:str

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    psw = db.Column(db.String(11), nullable=False)

    proposal = db.relationship('Proposal', backref='User', lazy=True)
    demands = db.relationship('Demand', backref='User', lazy=True)
    #endereco = db.relationship('Endereço', backref='Usuário', lazy=True)
    # def __repr__(self):
    #     return '<User %r>' % self.username

@dataclass
class Category(db.Model):
    id:int
    name_cat:str
    desc:str
    
    #demands:str 

    id = db.Column(db.Integer, primary_key=True)
    name_cat = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(80), nullable=False)
    demands = db.relationship('Demand', backref='Category', lazy=True)
    # def __repr__(self):
    #     return '<Category %r>' % self.name_cat

@dataclass
class Demand(db.Model):
    id:int
    demand_name:str
    desc:str
    category_id:int
    user_id:int

    id = db.Column(db.Integer, primary_key=True)
    demand_name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(80), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    propostas = db.relationship('Proposal', backref='Demand', lazy = True)
    # def __repr__(self):
    #     return '<Demand %r>' % self.desc

@dataclass
class Proposal(db.Model):
    id:int
    desc:str
    demand_fk:str
    user_id:int
        
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(80), nullable=False)
    demand_fk = db.Column(db.Integer, db.ForeignKey('demand.id'),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    # def __repr__(self):
    # return '<Proposal %r>' % self.desc