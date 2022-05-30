import sys
from sqlalchemy.exc import IntegrityError
from Model import User, Demand, Category
from application import DB
from flask import jsonify

class UserId:
    def user_id(user_id):
        return User.query.get(user_id)

class Login:
    def login(email,psw):
        query = User.query.filter_by(email=email).first()
        if query:
            if email == query.email and psw == query.psw:
                return query
        return False

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

class ViewDemands:
    def get_demands():

        query = Demand.query.filter(Demand.user_id==User.id)\
            .join(User, User.id==Demand.user_id)\
            .add_columns(User.first_name)\
            .join(Category, Category.id==Demand.category_id)\
            .add_columns(Category.name_cat)\
            .with_entities(Demand.id,Demand.demand_name, Demand.desc, User.first_name,Category.name_cat).all()
        return query
    def get_demand(id):
        query = Demand.query.filter(Demand.id == id)
        return query[0]

    def post_demand():
        pass

class ViewCategories:
    def get_categories():
        query = Category.query.all()
        return query

    def get_by_categories(id_cat):
        query = Demand.query.filter(Demand.category_id == id_cat).all()##
    
        return query
    
