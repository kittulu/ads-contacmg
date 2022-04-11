import sys
sys.path.append("/home/kitullu/Documentos/ads-contacmg/API/")
from application import App, DB
from flask_sqlalchemy import SQLAlchemy

db = DB.db()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_cat = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return '<Category %r>' % self.name_cat

