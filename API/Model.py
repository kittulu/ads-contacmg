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
    img_id:int

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    psw = db.Column(db.String(11), nullable=False)
    img_id = db.Column(db.Integer, db.ForeignKey('images.id'),nullable=True)

    proposal = db.relationship('Proposal', backref='User', lazy=True)
    demands = db.relationship('Demand', backref='User', lazy=True)
    #endereco = db.relationship('Endereço', backref='Usuário', lazy=True)
    # def __repr__(self):
    #     return '<User %r>' % self.username
    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)

@dataclass
class Category(db.Model):
    id:int
    name_cat:str
    desc:str
    img_id:int
    
    #demands:str 

    id = db.Column(db.Integer, primary_key=True)
    name_cat = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(80), nullable=False)
    img_id = db.Column(db.Integer, db.ForeignKey('images.id'),nullable=True)
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
    img_id:int
    
    id = db.Column(db.Integer, primary_key=True)
    demand_name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(80), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    img_id = db.Column(db.Integer, db.ForeignKey('images.id'),nullable=True)
    propostas = db.relationship('Proposal', backref='Demand', lazy = True)
    # def __repr__(self):
    #     return '<Demand %r>' % self.desc

@dataclass
class Proposal(db.Model):
    id:int
    desc:str
    demand_fk:str
    user_id:int
    img_id:int
        
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(80), nullable=False)
    demand_fk = db.Column(db.Integer, db.ForeignKey('demand.id'),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    img_id = db.Column(db.Integer, db.ForeignKey('images.id'),nullable=True)

    # def __repr__(self):
    # return '<Proposal %r>' % self.desc


@dataclass
class Images(db.Model):
    id:int
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
   
    user_fk = db.relationship('User', backref='Images', lazy=True)
    category = db.relationship('Category', backref='Images', lazy=True)
    proposal = db.relationship('Proposal', backref='Images', lazy=True)
    demands = db.relationship('Demand', backref='Images', lazy=True)