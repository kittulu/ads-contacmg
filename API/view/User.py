import sys
sys.path.append("/home/kitullu/Documentos/ads-contacmg/API/")
from sqlalchemy.exc import IntegrityError
from models.UserModel import User
from application import DB

class Login:
    def login(email,psw):
        if User.query.filter_by(email=email).first():
            query = User.query.filter_by(email=email).first()
            if email == query.email and psw == query.psw:
                #return token
                return 'usuarios aq'
        return 'fail'
            #print(query.username)
            #query = User.query.all()


class Register:
    def register(first_name, last_name, email, cpf, psw):
        db = DB.db()
        #MySQLdb._exceptions.IntegrityError: (1062, "Duplicate entry 'admin' for key 'username'")
        try:
            query = User(first_name=first_name,last_name = last_name, email=email,cpf=cpf,psw=psw)
            db.session.add(query)
            db.session.commit()
            return 'shuu'
        except IntegrityError as e:
            #print(f"(1062, \"Duplicate entry '{user}' for key 'username'\")")
            #print(e.__cause__)
            if str(e.__cause__) == f"""(1062, "Duplicate entry '{email}' for key 'email'")""":
                return "Email Exists"
            elif str(e.__cause__) == f"""(1062, "Duplicate entry '{cpf}' for key 'cpf'")""":
                return "cpf Exists"
            return "ERRU"
