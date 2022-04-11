from flask import Flask, request
from view.User import Login, Register
from application import App

app = App.app()

@app.route("/")
def index(): pass

@app.route("/login", methods=['POST'])
def login():
    email = request.form.get('email')
    psw = request.form.get('psw') 
    return Login.login(email, psw)
 
#@app.route('/user/')
#def profile(): pass

@app.route("/register", methods = ['POST'])
def register():
    r_json = request.json
    first_name = r_json['first_name']
    last_name = r_json['last_name']
    email = r_json['email']
    cpf =r_json['cpf']
    psw =r_json['psw'] 
    #print (request.json)
    return Register.register(user, email, cpf, psw)
   