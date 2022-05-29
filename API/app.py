from flask import Flask, request, render_template, redirect
from View import UserId, Login, Register, ViewDemands, ViewCategories
from application import App
from flask_login import LoginManager, login_required,current_user,login_user, logout_user,login_required


app = App.app()
app.secret_key = 'Innalhamdulillah.nahmaduhu.taalanastainubihi.wanastagfiruh!'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return UserId.user_id(user_id)

@app.route("/")
@login_required
def index():
    categories = ViewCategories.get_categories()
    demands = ViewDemands.get_demands()
    return render_template('index.html', cats=categories, dems=demands)

@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        psw = request.form.get('psw')
        query_id = Login.login(email, psw) 
        if query_id:
            login_user(query_id)
            return redirect("/", code=302)
        else:
            print('login_fail')
            return redirect("/login", code=302)
    else:
        return render_template('login.html')

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

@app.route("/demands", methods = ['GET'])
def demands():
    return ViewDemands.get_demands()

@app.route("/categories", methods = ['GET'])
def categories():
    return 

@app.route("/categories", methods = ['POST'])
def category():
    r_json = request.json
    id_cat = r_json['id']
    return ViewCategories.get_by_categories(id_cat)

@app.route("/cadastrodemanda", methods = ['GET'])
@login_required
def cadastrodemandas():
    return

@app.route("/cadastrodemanda", methods = ['POST'])
@login_required
def cadastrodemandas():
    r_json = request.json
    id_cat = r_json['']##request aqui
    return ViewCategories.get_by_categories(id_cat)
    
#https://bastter.com/mercado/forum/873006/extra-22--projeto-web-parte-3--fazendo-upload-de-arquivos-de-imagens-e-renderizando-as-imagens