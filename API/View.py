import sys, random, string
import datetime
from tokenize import Pointfloat
from sqlalchemy import or_, asc, desc
from sqlalchemy.exc import IntegrityError
from Model import User, Demand, Category, Proposal, Message
from application import DB, App
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


    def register(first_name, last_name, telefone, email, cpf, psw, img_path):
        db = DB.db()
        #MySQLdb._exceptions.IntegrityError: (1062, "Duplicate entry 'admin' for key 'username'")
        try:
            query = User(first_name=first_name,last_name = last_name, telefone=telefone,email=email,cpf=cpf,psw=psw, img_path = img_path)
            db.session.add(query)
            db.session.commit()
            return 'shuu'
        except IntegrityError as e:
            #print(f"(1062, \"Duplicate entry '{user}' for key 'username'\")")
            print(e.__cause__)
            if str(e.__cause__) == f"""UNIQUE constraint failed: user.email""":
                return "Email já cadastrado."
            elif str(e.__cause__) == f"""UNIQUE constraint failed: user.cpf""":
                return "Cpf já cadastrado."
            return "Erro no sistema! entre em contato com o administrador."

    def update(idz, first_name, last_name,telefone,  email, cpf, psw, img_path):
        db = DB.db()
        #MySQLdb._exceptions.IntegrityError: (1062, "Duplicate entry 'admin' for key 'username'")
        try:
            query = db.session.query(User).get(idz)
            query.first_name = first_name
            query.last_name = last_name
            query.telefone = telefone
            query.cpf=cpf
            query.email=email
            query.psw = psw
            query.img_path=img_path
            db.session.add(query)
            db.session.commit()
            return 'shuu'
        except IntegrityError as e:
            #print(f"(1062, \"Duplicate entry '{user}' for key 'username'\")")
            print(e.__cause__)
            if str(e.__cause__) == f"""UNIQUE constraint failed: user.email""":
                return "Email já esta sendo utilizado."
            elif str(e.__cause__) == f"""UNIQUE constraint failed: user.cpf""":
                return "Cpf em conflito."
            return "Erro no sistema! entre em contato com o administrador."

class ViewDemands:
    def get_demands():
        query = Demand.query.filter(Demand.user_id==User.id)\
            .join(User, User.id==Demand.user_id)\
            .add_columns(User.first_name)\
            .join(Category, Category.id==Demand.category_id)\
            .add_columns(Demand.img_path)\
            .add_columns(Category.name_cat)\
            .with_entities(Demand.id,Demand.demand_name, Demand.img_path, Demand.desc, User.first_name,Category.name_cat).all()
        return query


    def get_demand(id):
        #query = Demand.query.filter(Demand.id == id)
        query = Demand.query.filter(Demand.id == id)\
            .join(User, User.id==Demand.user_id)\
            .add_columns(User.first_name)\
            .add_columns(User.id.label('user_id'))\
            .add_columns(Demand.img_path)\
            .join(Category, Category.id==Demand.category_id)\
            .add_columns(Category.name_cat)\
            .with_entities(Demand.id,Demand.demand_name,Demand.img_path,Demand.desc, User.id, User.first_name,Category.name_cat).all()
        print(query[0])
        return query[0]

    def post_demand(demand_name,desc,category_id,user_id,image):
        db = DB.db()
        query = Demand(demand_name=demand_name,desc=desc,category_id=category_id,user_id=user_id,img_path = image)
        db.session.add(query)
        db.session.commit()
        return 'shuu'

    def post_proposal(desc,demand_id,user_id):
        db = DB.db()
        query = Proposal(desc=desc, demand_id=demand_id, user_id=user_id)
        db.session.add(query)
        db.session.commit()

    def get_proposal(id):
        query = Proposal.query.filter(Proposal.demand_id==id)\
            .join(User, User.id==Proposal.user_id)\
            .add_columns(User.id)\
            .add_columns(User.first_name)\
            .add_columns(User.last_name)\
            .add_columns(User.img_path)\
            .with_entities(Proposal.desc,User.id, User.first_name,User.last_name,User.img_path).all()
        return query

class ViewCategories:
    def get_categories():
        query = Category.query.all()
        return query
    def get_by_categories(id_cat):
        query = Demand.query.filter(Demand.category_id == id_cat).all()##
        return query
    
class Images:

    ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def createfilename():
        shu = ''.join((random.choice(string.ascii_letters, string.digits) for i in range(16)))
        return shu

    def imagesdb(pathz):
        db = DB.db()
        query = Images(path=pathz)
        db.session.add(query)
        db.session.commit()
        return query

    def upload_file(file):
        ##enviar como:    local/
        UPLOAD_FOLDER = 'assets/images/uploads/'
        if file and allowed_file(file.filename):
            filename = secure_filename( createfilename() )
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('download_file', name=filename))
            imagesdb( f"{app.config['UPLOAD_FOLDER']}{filename}" )
        return (f"{app.config['UPLOAD_FOLDER']}{filename}")
        
    
class viewMessage:
    def get_message(n,m):
        print (m)
        #query = Message.query.all()
        query1 = Message.query.filter(or_\
        ((Message.sender_id == n) & (Message.reciever_id == m),\
        ((Message.sender_id == m) & (Message.reciever_id == n))))\
        .order_by(asc(Message.server_timestamp)).all()
        return query1
        
    def chats(n):
        query1 = Message.query.filter(or_\
        ((Message.sender_id == 1) , (Message.reciever_id == 1)))\
        .all()
        shu=[]
        for i in query1:
            if i.sender_id not in shu:
                shu.append(i.sender_id)
            if i.reciever_id not in shu: 
                shu.append(i.reciever_id)
        print(shu)
        #[1,2]#
        return shu

    def sendmessage(sender_id,reciever_id,content):
        db = DB.db()
        a  = datetime.datetime.now()
        query = Message(sender_id=sender_id, reciever_id =reciever_id, content=content, server_timestamp=a)
        db.session.add(query)
        db.session.commit()
        return ''
    
