from application import DB
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = DB.db()

##Tabela armazena caminho para recuperar as imagens
@dataclass
class Images(db.Model):
    id:int
    path:str
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(80), nullable=False)

##Tabela usuário
@dataclass
class User(db.Model):
    id:int
    first_name:str
    last_name:str
    telefone:str
    email:str
    cpf:str
    psw:str
    img_path:str

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    telefone = db.Column(db.String(14), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    psw = db.Column(db.String(11), nullable=False)
    img_path = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.first_name
    
    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)

##Tabela Categoria
@dataclass
class Category(db.Model):
    id:int
    name_cat:str
    desc:str
    img_path:str

    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name_cat = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(80), nullable=False)
    img_path = db.Column(db.String(200),nullable=True)
    
    def __repr__(self):
        return '<Category %r>' % self.name_cat

#Tabela de demandas
@dataclass
class Demand(db.Model):
    id:int
    demand_name:str
    desc:str
    category_id:int
    user_id:int
    img_path:str
    
    __tablename__ = 'demand'
    id = db.Column(db.Integer, primary_key=True)
    demand_name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(80), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    img_path = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<Demand %r>' % self.desc

#Tabela de propostas
@dataclass
class Proposal(db.Model):
    id:int
    desc:str
    demand_id:int
    user_id:int
    
    
    __tablename__ = 'proposal'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(80), nullable=False)
    demand_id = db.Column(db.Integer, db.ForeignKey('demand.id'),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    

    def __repr__(self):
        return '<Proposal %r>' % self.desc
