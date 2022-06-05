from flask import Flask, request, render_template, redirect, flash
from View import UserId, Login, ViewDemands, Images, ViewCategories
from application import App
from flask_login import LoginManager, login_required,current_user,login_user, logout_user,login_required
import random, string

app = App.app()
app.secret_key = 'Innalhamdulillah.nahmaduhu.taalanastainubihi.wanastagfiruh!'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config['MAX_CONTENT_LENGTH'] = 160 * 1000 * 1000
app.config['UPLOAD_FOLDER'] = "static/assets/images/upload"

def name_gen():
    return ''.join((random.choice(string.ascii_letters + string.digits) for i in range(16)))

@login_manager.user_loader
def load_user(user_id):
    return UserId.user_id(user_id)

@app.route("/")
@login_required
def index():
    categories = ViewCategories.get_categories()
    demands = ViewDemands.get_demands()[:4]
    print(demands)
    return render_template('index.html', cats=categories, dems=demands)


@app.route("/<id>")
@login_required
def index_by(id):
    if id == "0":
        categories = ViewCategories.get_categories()
        demands = ViewDemands.get_demands()
    else:
        categories = ViewCategories.get_categories()
        demands = ViewCategories.get_by_categories(id)

    return render_template('index_all.html', cats=categories, dems=demands)

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
            return render_template("login.html", error="Usuario e/ou senha incorretos!")
    else:
        return render_template('login.html')

#@app.route('/user/')
#def profile(): pass

@app.route("/register", methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('name')
        last_name = request.form.get('lname')
        email = request.form.get('email')
        cpf = request.form.get('cpfcnpj')
        psw = request.form.get('psw') 
        img= name_gen()
        f = request.files.get('file')
        f.save(dst=f"static/assets/images/uploads/{img}")
        
        
        reg = Login.register(first_name,last_name, email, cpf, psw, img)
        if reg == 'shuu':
            return redirect("/login", code=302)
        else:
            return render_template('register.html', error=reg)
    else:
        return render_template('register.html')


@app.route("/demand/<id>", methods = ['GET'])
def ViewDemand(id):
    current = ViewDemands.get_demand(id)
    content = ViewDemands.get_demands()
    proposal = ViewDemands.get_proposal(int(id))
    print(proposal)
    return render_template('product.html', content=content, proposal=proposal, curr= current)

@app.route("/cadastrodemanda", methods = ['GET','POST'])
@login_required
def cadastrodemandas():
    if request.method == 'POST':
        demand_name = request.form.get('name')
        desc = request.form.get('desc')
        category_id = int(request.form.get('cat'))-1
        user_id = current_user.id
        img= name_gen()
        f = request.files.get('file')
        f.save(dst=f"static/assets/images/uploads/{img}")
        print(request.form)
        reg = ViewDemands.post_demand(demand_name,desc,category_id,user_id,img)
        return render_template('cadservice.html', error="Cadastrado com sucesso!")
    else:
        return  render_template('cadservice.html')


@app.route("/criarproposta/<id>", methods = ['GET','POST'])
@login_required
def criarproposta(id):

    if request.method == 'POST':
        desc = request.form.get('desc')
        user_id = current_user.id
        demand_id = id
        ViewDemands.post_proposal(desc, demand_id, user_id)
        returnvalue = ViewDemands.get_demand(int(id))
        return render_template('cadproposta.html', error="Cadastrado com sucesso!", value=returnvalue)
    else:
        returnvalue = ViewDemands.get_demand(int(id))
        print(returnvalue)
        return  render_template('cadproposta.html', value=returnvalue)

##
# @app.route("/proposta", methods = ['GET','POST'])
# @login_required
# def cadastroproposta():
#     if request.method == 'POST':
#         desc = request.form.get('desc')
#         desc = request.form.get('desc')
#         category_id = int(request.form.get('cat'))-1
#         user_id = current_user.id
#         print(request.form)
#         reg = ViewDemands.post_demand(demand_name,desc,category_id,user_id)
#         return render_template('cadservice.html', error="Cadastrado com sucesso!")

#     else:
#         return  render_template('cadservice.html')
