from flask import Flask, request, render_template, redirect, flash
from View import UserId, Login, ViewDemands, ViewCategories
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
@app.route("/<id>")
@login_required
def index_by(id):
    categories = ViewCategories.get_categories()
    demands = ViewCategories.get_by_categories(id)
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
            flash('Login Fail.')
            return redirect("/login", code=302)
    else:
        return render_template('login.html')

#@app.route('/user/')
#def profile(): pass

@app.route("/register", methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        r_json = request.json
        first_name = r_json['first_name']
        last_name = r_json['last_name']
        email = r_json['email']
        cpf =r_json['cpf']
        psw =r_json['psw'] 
        #print (request.json)
        return Login.register(user, email, cpf, psw)
    else:
        return render_template('register.html')


@app.route("/demand/<id>", methods = ['GET'])
def ViewDemand(id):
    content = ViewDemands.get_demand(int(id))
    return render_template('product.html', content=content)



@app.route("/cadastrodemanda", methods = ['GET'])
@login_required
def cadastrodemandas():
    return  render_template('cadservice.html')
