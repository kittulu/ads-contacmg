import sys
sys.path.append("/home/kitullu/Documentos/ads-contacmg/API/")
from models.UserModel import db

db.create_all()
