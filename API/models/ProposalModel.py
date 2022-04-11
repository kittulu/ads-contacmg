import sys
sys.path.append("/home/kitullu/Documentos/ads-contacmg/API/")
from application import App, DB
from flask_sqlalchemy import SQLAlchemy
#from DemandModel import Demand

db = DB.db()

class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(80), nullable=False)
    fk_demand = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return '<Proposal %r>' % self.desc
