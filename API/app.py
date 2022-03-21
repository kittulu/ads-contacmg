from flask import Flask, request
from routes.login import Login

app = Flask(__name__)

def autenticate(batatoken):
    if batatoken == '~shuu':
        return True
    else:
        return False

@app.route("/login", methods=['POST'])
def hello_world():
    print(request.headers)
    if autenticate(request.headers.get('token')):
        print(request.form)
        user = request.form.get('user')
        #print(request.form.get('batatinha'))
        password = request.form.get('pass') 
        print(request.headers)
        return Login.login(user,password)
        #return 'shuu'
    else:
        return 'deu ruim'
