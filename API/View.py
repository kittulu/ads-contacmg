import sys
from sqlalchemy.exc import IntegrityError
from Model import User, Demand, Category
from application import DB
from flask import jsonify


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





# class Demand(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     demand_name = db.Column(db.String(80), nullable=False)
#     desc = db.Column(db.String(80), nullable=False)
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
#     propostas = db.relationship('Proposal', backref='Demand', lazy = True)
#     def __repr__(self):
#         return '<Demand %r>' % self.desc

class ViewDemands:
    def get_demands():
        #query =Demand.query.all()
        #json = jsonify(query)

        query = Demand.query.filter(Demand.user_id==User.id)\
            .join(User, User.id==Demand.user_id)\
            .add_columns(User.first_name)\
            .join(Category, Category.id==Demand.category_id)\
            .add_columns(Category.name_cat)\
            .with_entities(Demand.demand_name, Demand.desc, User.first_name,Category.name_cat).all()
        print (query)
        return jsonify(query)
        
        # sla = Demand.query.filter(Demand.name==User.id).all()
        # print ([i for i in query])
        #query = json.dumps(query)
        # query[0]

    def post_demand():
        pass

class ViewCategories:
    def get_categories():
        #query =Demand.query.all()
        #json = jsonify(query)
        query = Category.query.all()
        print (query)
        return jsonify(query)
        
    #    id:int
    # demand_name:str
    # desc:str
    # category_id:int
    # user_id:int

    def get_by_categories(id_cat):
        query = Demand.query.filter(Demand.category_id == id_cat).all()##
        print (query)
        return jsonify(query)
    
